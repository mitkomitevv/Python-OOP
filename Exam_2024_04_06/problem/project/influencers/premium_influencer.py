from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):
    INITIAL_PAYMENT_PERCENTAGE = 0.85

    def calculate_payment(self, campaign: BaseCampaign):
        return campaign.budget * self.INITIAL_PAYMENT_PERCENTAGE

    def reached_followers(self, campaign_type: str):
        campaign_followers = 0

        if campaign_type == "HighBudgetCampaign":
            campaign_followers = self.followers * self.engagement_rate * 1.5

        elif campaign_type == "LowBudgetCampaign":
            campaign_followers = self.followers * self.engagement_rate * 0.8

        return int(campaign_followers)
