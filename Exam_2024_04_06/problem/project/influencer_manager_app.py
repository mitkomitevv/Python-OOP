from typing import List
from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    VALID_INFLUENCERS = {"PremiumInfluencer": PremiumInfluencer, "StandardInfluencer": StandardInfluencer}
    VALID_CAMPAIGNS = {"HighBudgetCampaign": HighBudgetCampaign, "LowBudgetCampaign": LowBudgetCampaign}

    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.VALID_INFLUENCERS:
            return f"{influencer_type} is not an allowed influencer type."

        for influencer in self.influencers:
            if influencer.username == username:
                return f"{username} is already registered."

        influencer = self.VALID_INFLUENCERS[influencer_type](username, followers, engagement_rate)
        self.influencers.append(influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.VALID_CAMPAIGNS:
            return f"{campaign_type} is not a valid campaign type."

        for campaign in self.campaigns:
            if campaign.campaign_id == campaign_id:
                return f"Campaign ID {campaign_id} has already been created."

        campaign = self.VALID_CAMPAIGNS[campaign_type](campaign_id, brand, required_engagement)
        self.campaigns.append(campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer = self.get_influencer(influencer_username)
        campaign = self.get_campaign(campaign_id)

        if not influencer:
            return f"Influencer '{influencer_username}' not found."

        if not campaign:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        infuencer_payment = influencer.calculate_payment(campaign)
        if infuencer_payment > 0.0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= infuencer_payment
            influencer.campaigns_participated.append(campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        campaigns_followers = {}

        for campaign in self.campaigns:
            for influencer in campaign.approved_influencers:
                if campaign not in campaigns_followers:
                    campaigns_followers[campaign] = 0
                campaigns_followers[campaign] += influencer.reached_followers(type(campaign).__name__)

        return campaigns_followers

    def influencer_campaign_report(self, username: str):
        influencer = self.get_influencer(username)

        if not influencer.campaigns_participated:
            return f"{username} has not participated in any campaigns."

        return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        sorted_campaigns = sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), -c.budget))
        result = "$$ Campaign Statistics $$"

        for campaign in sorted_campaigns:
            result += "\n" + (f"  * Brand: {campaign.brand}, "
                              f"Total influencers: {len(campaign.approved_influencers)}, "
                              f"Total budget: ${campaign.budget:.2f}, "
                              f"Total reached followers: {self.calculate_total_reached_followers()[campaign]}")

        return result

    def get_influencer(self, username):
        return next(filter(lambda i: i.username == username, self.influencers), None)

    def get_campaign(self, campaign_id):
        return next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns), None)
