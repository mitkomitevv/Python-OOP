from project.campaigns.base_campaign import BaseCampaign


class LowBudgetCampaign(BaseCampaign):

    def __init__(self,  campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, 2500.0, required_engagement)

    def check_eligibility(self, engagement_rate: float):
        engagement_to_meet = self.required_engagement * 0.90
        if engagement_rate >= engagement_to_meet:
            return True
        return False
