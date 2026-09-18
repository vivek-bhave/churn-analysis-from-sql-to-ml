USE churn_db;

-- ==========================================================
-- TABLE 1 : MASTER RECOMMENDATION CATALOG
-- ==========================================================

DROP TABLE IF EXISTS recommendation_actions;


CREATE TABLE recommendation_actions (
    action_id VARCHAR(5) PRIMARY KEY,
    action_category VARCHAR(50) NOT NULL,
    service_category ENUM('Reactive','Proactive') NOT NULL,
    cost ENUM('Low','Medium','High') NOT NULL,
    recommendation TEXT NOT NULL
);

-- ==========================================================
-- TABLE 2 : RECOMMENDATION RULES
-- ==========================================================

DROP TABLE IF EXISTS recommendation_rules;

CREATE TABLE recommendation_rules (
    rule_id VARCHAR(5) PRIMARY KEY,

    payment_delay ENUM('Low','Medium','High') NOT NULL,
    support_calls ENUM('Low','Medium','High') NOT NULL,

    contract_length ENUM('Monthly','Quarterly','Annual') NOT NULL,

    spend_level ENUM('Low','High') NOT NULL,

    tenure_level ENUM('Any','Non-High','High') NOT NULL,

    actions VARCHAR(255) NOT NULL
);


INSERT INTO recommendation_actions VALUES
('A01','Baseline Engagement','Reactive','Medium','Monitor their social media.'),
('A02','Baseline Engagement','Proactive','Low','Send post-event emails.'),
('A03','Baseline Engagement','Proactive','Low','Give prior video solutions for complex problems.'),
('A04','Baseline Engagement','Proactive','Medium','Provide AI Chatbot FAQ knowledge base.'),
('A05','Early Intervention','Proactive','Low','Respond before 4 support calls.'),
('A06','Early Intervention','Proactive','Low','Respond before 20 days of payment delay.'),
('A07','Reactive Recovery','Reactive','Low','Resolve queries through AI chatbot.'),
('A08','Reactive Recovery','Reactive','Low','Provide asynchronous email.'),
('A09','Reactive Recovery','Reactive','High','Provide text and calls with human (if necessary).'),
('A10','VIP Engagement','Proactive','High','Increase Multi-Channel Issue Alerts.'),
('A11','Loyalty Reward','Proactive','High','Recognition: Top 3% customers.'),
('A12','Loyalty Reward','Proactive','High','Recognition: Top 2% customers.'),
('A13','Loyalty Reward','Proactive','High','Recognition: Top 1% customers.'),
('A14','Loyalty Reward','Proactive','High','Offer Low discounts on subscriptions and other services.'),
('A15','Loyalty Reward','Proactive','High','Offer Medium discounts on subscriptions and other services.'),
('A16','Loyalty Reward','Proactive','High','Offer High discounts on subscriptions and other services.'),
('A17','VIP Engagement','Proactive','High','Invite platform events and forums.'),
('A18','Feedback','Reactive','Medium','Take feedback after issue resolution.');


INSERT INTO recommendation_rules VALUES

('R01','Low','Low','Monthly','Low','Any',
'A01,A02,A03,A04'),

('R02','Low','Low','Monthly','High','Any',
'A01,A02,A03,A04,A11,A14'),

('R03','Low','Low','Annual','High','Non-High',
'A01,A02,A03,A04,A12,A15'),

('R04','Low','Low','Quarterly','High','Non-High',
'A01,A02,A03,A04,A12,A15'),

('R05','Low','Low','Annual','High','High',
'A01,A02,A03,A04,A13,A16,A17,A10'),

('R06','Low','Low','Quarterly','High','High',
'A01,A02,A03,A04,A13,A16,A17,A10'),

('R07','Medium','Low','Monthly','Low','Any',
'A06,A07,A08'),

('R08','Low','Medium','Monthly','Low','Any',
'A05,A07,A08'),

('R09','Medium','Medium','Monthly','Low','Any',
'A05,A06,A07,A08'),

('R10','Medium','Medium','Monthly','High','Any',
'A05,A06,A07,A08,A09,A03,A04'),

('R11','Medium','Low','Monthly','High','Any',
'A06,A07,A08,A09,A03,A04'),

('R12','Low','Medium','Monthly','High','Any',
'A05,A07,A08,A09,A03,A04'),

('R13','Medium','Medium','Annual','High','Any',
'A05,A06,A07,A08,A09,A03,A04,A10,A02,A15'),

('R14','Medium','Medium','Quarterly','High','Any',
'A05,A06,A07,A08,A09,A03,A04,A10,A02,A15'),

('R15','Medium','Low','Annual','High','Any',
'A06,A07,A08,A09,A03,A04,A10,A02,A15'),

('R16','Medium','Low','Quarterly','High','Any',
'A06,A07,A08,A09,A03,A04,A10,A02,A15'),

('R17','Low','Medium','Annual','High','Any',
'A05,A07,A08,A09,A03,A04,A10,A02,A15'),

('R18','Low','Medium','Quarterly','High','Any',
'A05,A07,A08,A09,A03,A04,A10,A02,A15'),

('R19','High','High','Monthly','Low','Any',
'A07,A08'),

('R20','High','High','Monthly','High','Any',
'A10,A09,A18,A16'),

('R21','High','High','Annual','High','Any',
'A10,A09,A18,A16'),

('R22','High','High','Quarterly','High','Any',
'A10,A09,A18,A16');

