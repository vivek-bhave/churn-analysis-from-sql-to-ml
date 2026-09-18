from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated


class HighValueCustomerLossInput(BaseModel):
    Age: Annotated[float, Field(..., ge=0, lt=120, description="Age of the customer")]
    Gender: Annotated[Literal["Female", "Male"], Field(..., description="Gender of the customer")]
    Tenure: Annotated[float, Field(..., ge=0, description="The amount of time for which the customer has been with the service")]
    Usage_Frequency: Annotated[float, Field(..., ge=0, alias="Usage Frequency", description="The number of times a customer engage with the service in the week")]
    Support_Calls: Annotated[float, Field(..., ge=0, alias="Support Calls", description="The number of times a customer complains in week")]
    Subscription_Type: Annotated[Literal["Basic", "Standard", "Premium"], Field(..., alias="Subscription Type", description="The type of subscription a customer enrolled in", examples=["Basic", "Standard", "Premium"])]
    Contract_Length: Annotated[Literal["Monthly", "Annual", "Quarterly"], Field(..., alias="Contract Length", description="The type of contract length a customer enrolled in", examples=["Monthly", "Standard", "Quarterly"])]
    Total_Spend: Annotated[float, Field(..., ge=0, alias="Total Spend", description="The amount of money spend by a customer")]
    Last_Interaction: Annotated[float, Field(..., ge=0, alias="Last Interaction", description="The number of days since the customer's last interaction with the platform")]
    Payment_Delay: Annotated[float, Field(..., ge=0, alias="Payment Delay", description="The number of days delayed by the customer to renew the subscription")]

    @computed_field(alias="Issue_Level")
    @property
    def issue_level(self) -> str:
        if self.Support_Calls <= 2:
            return "Low Issues"
        elif self.Support_Calls <= 4:
            return "Medium Issues"
        else:
            return "High Issues"

    @computed_field(alias="Delay_Level")
    @property
    def delay_level(self) -> str:
        if self.Payment_Delay <= 15:
            return "Low Delay"
        elif self.Payment_Delay <= 20:
            return "Medium Delay"
        else:
            return "High Delay"

    @computed_field(alias="Spend_Level")
    @property
    def spend_level(self) -> str:
        if self.Total_Spend <= 508:
            return "Low Spend"
        else:
            return "High Spend"

    @computed_field(alias="Age_Group")
    @property
    def age_group(self) -> str:
        if self.Age <= 19:
            return "Very Young"
        elif self.Age <= 29:
            return "Young Adult"
        elif self.Age <= 39:
            return "Old Adult"
        else:
            return "Old"

    @computed_field(alias="LI_Level")
    @property
    def li_level(self) -> str:
        if self.Last_Interaction <= 15:
            return "Low LI"
        else:
            return "High LI"

    @computed_field(alias="UF_Level")
    @property
    def uf_level(self) -> str:
        if self.Usage_Frequency <= 9:
            return "Low UF"
        else:
            return "High UF"

    @computed_field(alias="Tenure_Level")
    @property
    def tenure_level(self) -> str:
        if self.Tenure <= 5:
            return "Very Low Tenure"
        elif self.Tenure <= 11:
            return "Low Tenure"
        elif self.Tenure <= 24:
            return "Medium Tenure"
        else:
            return "High Tenure"

class RetentionCostOptimizationInput(BaseModel):
    Support_Calls: Annotated[float, Field(..., ge=0, alias="Support Calls", description="The number of times a customer complains in week")]
    Contract_Length: Annotated[Literal["Monthly", "Annual", "Quarterly"], Field(..., alias="Contract Length", description="The type of contract length a customer enrolled in", examples=["Monthly", "Standard", "Quarterly"])]
    Total_Spend: Annotated[float, Field(..., ge=0, alias="Total Spend", description="The amount of money spend by a customer")]
    Payment_Delay: Annotated[float, Field(..., ge=0, alias="Payment Delay", description="The number of days delayed by the customer to renew the subscription")]

    @computed_field(alias="Issue_Level")
    @property
    def issue_level(self) -> str:
        if self.Support_Calls <= 2:
            return "Low Issues"
        elif self.Support_Calls <= 4:
            return "Medium Issues"
        else:
            return "High Issues"
    
    @computed_field(alias="Delay_Level")
    @property
    def delay_level(self) -> str:
        if self.Payment_Delay <= 15:
            return "Low Delay"
        elif self.Payment_Delay <= 20:
            return "Medium Delay"
        else:
            return "High Delay"
    
    @computed_field(alias="Spend_Level")
    @property
    def spend_level(self) -> str:
        if self.Total_Spend <= 508:
            return "Low Spend"
        else:
            return "High Spend"

class PredictionRequest(BaseModel):
    client_type: Literal[
        "interaction_client",
        "monitoring_agent",
        "manager"
    ]
    problem: Literal[
        "high_value_customer_loss",
        "retention_cost_optimization"
    ]

    data: dict