import mysql.connector
from collections import defaultdict


# --------------------------------------------------
# MariaDB Connection
# --------------------------------------------------

def get_connection():
    return mysql.connector.connect(
        host="database",
        user="vivek",
        password="password123",
        database="churn_db"
    )


# --------------------------------------------------
# Rule Matching
# --------------------------------------------------

def find_matching_rule(
    delay_level: str,
    issue_level: str,
    contract_length: str,
    spend_level: str,
    tenure_level: str = "Any"
):
    """
    Returns the recommendation rule matching engineered features.
    """

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Convert tenure into business rule category
    # Convert ML feature labels to database labels

    delay_db = delay_level.replace(" Delay", "")
    issue_db = issue_level.replace(" Issues", "")
    spend_db = spend_level.replace(" Spend", "")

    if tenure_level == "High Tenure":
        tenure_group = "High"
    else:
        tenure_group = "Non-High"

    query = """
        SELECT *
        FROM recommendation_rules
        WHERE delay_level = %s
          AND issue_level = %s
          AND contract_length = %s
          AND spend_level = %s
          AND (
                tenure_level = 'Any'
                OR tenure_level = %s
              )
        LIMIT 1;
    """

    cursor.execute(query, (
        delay_db,
        issue_db,
        contract_length,
        spend_db,
        tenure_group
    ))
    rule = cursor.fetchone()

    cursor.close()
    conn.close()

    return rule


# --------------------------------------------------
# Fetch Recommendation Actions
# --------------------------------------------------

def fetch_actions(action_ids):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    placeholders = ",".join(["%s"] * len(action_ids))

    query = f"""
        SELECT *
        FROM recommendation_actions
        WHERE action_id IN ({placeholders});
    """

    cursor.execute(query, action_ids)

    actions = cursor.fetchall()

    cursor.close()
    conn.close()

    # Preserve recommendation order
    action_map = {a["action_id"]: a for a in actions}

    return [action_map[action] for action in action_ids]


# --------------------------------------------------
# Build Recommendation Response
# --------------------------------------------------

def generate_recommendations(
    client_type,
    delay_level,
    issue_level,
    contract_length,
    spend_level,
    tenure_level="Any"
):

    rule = find_matching_rule(
        delay_level,
        issue_level,
        contract_length,
        spend_level,
        tenure_level
    )

    if not rule:
        return {
            "rule_id": None,
            "recommendations": {},
            "escalation_required": False
        }

    action_ids = rule["actions"].split(",")

    actions = fetch_actions(action_ids)
    filtered_actions = []
    escalation_required = False

    for action in actions:

        # Customer Interaction Client
        if client_type == "interaction_client":
            continue

        # Monitoring Agent
        elif client_type == "monitoring_agent":

            if action["authority_level"] == "all":
                filtered_actions.append(action)

            elif action["authority_level"] == "manager":
                escalation_required = True

        # Manager
        elif client_type == "manager":
            filtered_actions.append(action)

    grouped = defaultdict(lambda: defaultdict(list))

    cost_order = {"Low": 1, "Medium": 2, "High": 3}
    service_order = {"Reactive": 1, "Proactive": 2}

    for action in filtered_actions:
        grouped[action["action_category"]][action["service_category"]].append({
            "action_id": action["action_id"],
            "recommendation": action["recommendation"],
            "cost": action["cost"]
        })

    # Sort Low → Medium → High
    final_output = {}

    for category in grouped:

        final_output[category] = {}

        for service in sorted(
            grouped[category],
            key=lambda x: service_order[x]
        ):

            final_output[category][service] = sorted(
                grouped[category][service],
                key=lambda x: cost_order[x["cost"]]
            )

    return {
    "rule_id": rule["rule_id"],
    "recommendations": final_output,
    "escalation_required": escalation_required
}
