"""
Growth-OS Folder Structure Generator
Covers: Business Growth, Lead Generation, Marketing Strategies,
        Growth Hacking, Business Development + more
Run: python3 create_growth_os.py
"""

import os

STRUCTURE = {
    "Growth-OS": {
        ".claude": {
            "System Prompts": ["Growth Strategy Prompts", "Lead Gen Prompts", "Copywriting Prompts", "Outreach Prompts", "Analytics Prompts"],
            "Agents": ["Lead Research Agent", "Outreach Agent", "Content Agent", "SEO Agent", "Analytics Agent"],
            "Workflows": ["Lead Gen Workflow", "Campaign Workflow", "BD Workflow", "Growth Experiment Workflow"],
            "Memory": ["Brand Voice", "ICP Profiles", "Competitor Intel", "Market Context"],
            "MCP Configs": ["CRM Connections", "Email Platform Configs", "Analytics Connections"],
        },
        "Business Growth": {
            "Growth Strategy": ["Growth Vision", "Growth Framework", "Ansoff Matrix", "Market Penetration", "Market Development", "Product Development", "Diversification"],
            "Revenue Growth": ["Revenue Streams", "Upsell Strategy", "Cross Sell Strategy", "Expansion Revenue", "Pricing Optimization", "Revenue Forecasts"],
            "Customer Growth": ["Acquisition Strategy", "Activation Plans", "Retention Programs", "Referral Programs", "Win Back Campaigns"],
            "Market Expansion": ["New Market Research", "Geographic Expansion", "Vertical Expansion", "Entry Strategy", "Localization Plans"],
            "Growth OKRs": ["Company OKRs", "Growth KPIs", "North Star Metric", "Leading Indicators", "Lagging Indicators"],
            "Competitive Positioning": ["Competitor Analysis", "Differentiation Strategy", "Moat Building", "Positioning Maps", "Blue Ocean Strategy"],
            "Funding & Investment": ["Pitch Decks", "Investor Pipeline", "Financial Projections", "Due Diligence Prep", "Cap Table"],
            "AI Workflows": ["Growth Strategy Builder", "Revenue Model Analyzer", "Expansion Planner"],
        },
        "Lead Generation": {
            "ICP & Personas": ["Ideal Customer Profiles", "Buyer Personas", "Pain Point Library", "Job Title Targeting", "Persona Research"],
            "Inbound Lead Gen": ["SEO Strategy", "Content Marketing", "Lead Magnets", "Gated Content", "Webinars", "Free Tools"],
            "Outbound Lead Gen": ["Prospect Lists", "Cold Email", "LinkedIn Outreach", "Cold Calling", "Direct Mail", "Account Based Outreach"],
            "Lead Magnets": ["eBooks & Guides", "Templates", "Checklists", "Free Calculators", "Mini Courses", "Research Reports"],
            "Lead Scoring": ["Scoring Models", "MQL Definition", "SQL Definition", "PQL Definition", "Score Thresholds"],
            "Lead Capture": ["Landing Pages", "Forms & CTAs", "Pop Ups", "Chatbots", "Exit Intent"],
            "Lead Nurturing": ["Drip Sequences", "Nurture Tracks", "Re Engagement", "Lead Warming", "Sales Handoff"],
            "Lead Database": ["Raw Leads", "Qualified Leads", "Disqualified Leads", "Recycled Leads", "Lead Sources"],
            "Tools & Automation": ["Apollo", "Hunter.io", "ZoomInfo", "Clay", "Phantombuster", "Lemlist"],
            "AI Workflows": ["ICP Builder", "Lead Enricher", "Outreach Personalizer"],
        },
        "Marketing Strategies": {
            "Brand Strategy": ["Brand Positioning", "Brand Architecture", "Brand Voice & Tone", "Messaging Framework", "Taglines", "Story Brand"],
            "Content Marketing": ["Content Strategy", "Content Calendar", "Blog", "Video", "Podcast", "Newsletters", "Long Form Content"],
            "Social Media": ["Platform Strategy", "LinkedIn", "Twitter X", "Instagram", "TikTok", "YouTube", "Facebook", "Scheduling & Automation"],
            "Email Marketing": ["List Building", "Segmentation", "Campaigns", "Automation Flows", "A-B Testing", "Deliverability"],
            "SEO": ["Keyword Strategy", "On Page SEO", "Technical SEO", "Link Building", "Local SEO", "SEO Reporting"],
            "Paid Advertising": ["Google Ads", "Meta Ads", "LinkedIn Ads", "YouTube Ads", "Programmatic", "Retargeting", "Ad Creative Library"],
            "Influencer Marketing": ["Influencer Database", "Outreach Templates", "Campaign Briefs", "Contracts", "Performance Tracking"],
            "Event Marketing": ["Webinars", "Conferences", "Virtual Events", "Sponsorships", "Event Recaps"],
            "Marketing Analytics": ["Campaign Reports", "Attribution Models", "Channel ROI", "Marketing Dashboards", "Budget Allocation"],
            "Go To Market": ["GTM Playbooks", "Launch Plans", "Positioning", "Pricing Strategy", "Sales Enablement"],
            "AI Workflows": ["Campaign Builder", "Copy Generator", "Strategy Analyzer"],
        },
        "Growth Hacking": {
            "Experimentation": ["Experiment Backlog", "Running Experiments", "Completed Experiments", "Experiment Results", "Learning Library"],
            "A-B Testing": ["Landing Page Tests", "Pricing Tests", "Onboarding Tests", "Email Tests", "CTA Tests"],
            "Viral Loops": ["Referral Mechanics", "Share Triggers", "Virality Coefficient", "Invite Flows", "Loop Analysis"],
            "Product Led Growth": ["PLG Strategy", "Freemium Model", "Free Trial Design", "Aha Moment Map", "Activation Funnel", "PQL Framework", "Expansion Triggers"],
            "Conversion Rate Optimization": ["CRO Audits", "Heatmap Analysis", "Session Recordings", "UX Friction Points", "Form Optimization", "Checkout Optimization"],
            "Acquisition Hacks": ["Community Infiltration", "Platform Arbitrage", "SEO Hacks", "PR Stunts", "Partnership Hacks"],
            "Retention Hacks": ["Habit Forming Loops", "Gamification", "Push Notifications", "Re Engagement Flows", "Power User Programs"],
            "Monetization Hacks": ["Pricing Psychology", "Urgency & Scarcity", "Bundle Strategies", "Downsell Flows", "LTV Maximization"],
            "Data Driven Growth": ["Growth Models", "Cohort Analysis", "Funnel Metrics", "Growth Accounting", "Predictive Models"],
            "Tools Stack": ["Analytics Tools", "Testing Tools", "Automation Tools", "Tracking Setup"],
            "AI Workflows": ["Experiment Designer", "Growth Lever Finder", "CRO Advisor"],
        },
        "Business Development": {
            "BD Strategy": ["BD Vision", "Target Markets", "Revenue Targets", "BD Playbook", "Quarterly Plans"],
            "Prospect Research": ["Target Account Lists", "Account Intelligence", "Decision Maker Maps", "Buying Signals", "Intent Data"],
            "Outreach": ["Cold Email Sequences", "LinkedIn Sequences", "Call Scripts", "Video Outreach", "Multi Touch Sequences", "Follow Up Templates"],
            "Pipeline Management": ["Lead Stage", "Discovery Stage", "Proposal Stage", "Negotiation Stage", "Closed Won", "Closed Lost"],
            "Proposals & Pitches": ["Proposal Templates", "Pitch Decks", "Case Studies", "Sent Proposals", "Won Proposals"],
            "Partnerships": ["Strategic Partners", "Channel Partners", "Tech Partners", "Referral Partners", "Partner Agreements", "JV Opportunities"],
            "Alliances": ["Co Marketing", "Co Selling", "White Label", "Reseller Agreements", "OEM Deals"],
            "BD Analytics": ["Pipeline Reports", "Win Loss Analysis", "Activity Metrics", "Revenue Attribution"],
            "AI Workflows": ["Prospect Researcher", "Proposal Builder", "Deal Coach"],
        },
        "Sales Funnel": {
            "Top of Funnel": ["Awareness Campaigns", "Brand Content", "Thought Leadership", "PR & Media", "Paid Awareness"],
            "Middle of Funnel": ["Consideration Content", "Comparison Pages", "Case Studies", "Webinars", "Demo Offers"],
            "Bottom of Funnel": ["Sales Pages", "Pricing Pages", "Trial Offers", "Objection Handling", "Close Scripts"],
            "Funnel Optimization": ["Conversion Rates", "Drop Off Points", "Funnel Tests", "Optimization Roadmap"],
            "Post Purchase": ["Onboarding Flows", "Upsell Sequences", "Loyalty Programs", "Referral Asks", "Advocacy Programs"],
            "AI Workflows": ["Funnel Analyzer", "Drop Off Diagnoser", "Conversion Optimizer"],
        },
        "Customer Acquisition": {
            "Acquisition Channels": ["Organic Search", "Paid Search", "Social Organic", "Paid Social", "Email", "Referral", "Direct", "Partnerships"],
            "CAC Management": ["CAC by Channel", "Blended CAC", "CAC Payback Period", "CAC Benchmarks", "CAC Reduction Plans"],
            "Paid Acquisition": ["Google Ads", "Meta Ads", "LinkedIn Ads", "Native Ads", "Affiliate Programs", "Ad Spend Tracker"],
            "Organic Acquisition": ["SEO", "Content", "Community", "Social Media", "Word of Mouth"],
            "Attribution": ["Attribution Models", "UTM Framework", "Multi Touch Reports", "Channel Mix"],
            "AI Workflows": ["Channel Optimizer", "CAC Calculator", "Attribution Advisor"],
        },
        "Retention & Loyalty": {
            "Onboarding": ["Onboarding Flows", "Welcome Sequences", "Activation Checklist", "Aha Moment Design", "Time to Value"],
            "Customer Success": ["Success Plans", "QBR Templates", "Health Scores", "At Risk Customers", "Expansion Plays"],
            "Loyalty Programs": ["Points Systems", "Tier Programs", "VIP Programs", "Rewards Catalog", "Program Analytics"],
            "Churn Prevention": ["Churn Signals", "Intervention Playbooks", "Save Offers", "Cancellation Flows", "Win Back Campaigns"],
            "Community": ["Community Strategy", "Forum Management", "User Groups", "Ambassador Program", "Community Events"],
            "AI Workflows": ["Churn Predictor", "Loyalty Designer", "CS Playbook Builder"],
        },
        "Content Engine": {
            "Content Strategy": ["Pillar Topics", "Topic Clusters", "Content Pillars", "Audience Journey Map", "Competitive Content"],
            "Content Production": ["Blog Posts", "Case Studies", "Whitepapers", "Infographics", "Video Scripts", "Podcast Scripts"],
            "Content Distribution": ["Publish Calendar", "Repurposing Plan", "Syndication", "Amplification"],
            "Copywriting": ["Sales Copy", "Ad Copy", "Email Copy", "Landing Page Copy", "Social Copy", "Copy Swipe File"],
            "Content Analytics": ["Traffic Reports", "Engagement Metrics", "Lead Attribution", "Top Performers"],
            "Brand Assets": ["Logo Files", "Color Palette", "Typography", "Templates", "Style Guide"],
            "AI Workflows": ["Content Brief Generator", "Content Repurposer", "SEO Content Writer"],
        },
        "Outreach & Campaigns": {
            "Email Campaigns": ["Cold Outreach", "Nurture Campaigns", "Launch Campaigns", "Re Engagement", "Promotional", "Transactional"],
            "LinkedIn Campaigns": ["Connection Sequences", "InMail Templates", "Content Campaigns", "Event Promotion", "Thought Leadership"],
            "Cold Email": ["Prospect Lists", "Email Sequences", "Personalization Snippets", "Subject Line Tests", "Reply Templates", "Campaign Results"],
            "Multi Channel": ["Email + LinkedIn", "Email + Call", "Social + Email", "ABM Plays"],
            "Campaign Analytics": ["Open Rates", "Reply Rates", "Meeting Booked Rates", "Campaign ROI", "A-B Test Results"],
            "AI Workflows": ["Sequence Writer", "Subject Line Tester", "Reply Handler"],
        },
        "Analytics & Reporting": {
            "Growth Metrics": ["MRR ARR", "Revenue Growth Rate", "Customer Count", "NRR GRR", "Growth Accounting"],
            "Acquisition Metrics": ["Traffic Sources", "Lead Volume", "CAC Tracking", "Conversion Rates", "Pipeline Value"],
            "Engagement Metrics": ["DAU WAU MAU", "Session Metrics", "Feature Usage", "NPS CSAT"],
            "Revenue Metrics": ["ARPU ARPA", "LTV Tracking", "Expansion Revenue", "Churn Revenue"],
            "Dashboards": ["Growth Dashboard", "Marketing Dashboard", "Sales Dashboard", "BD Dashboard", "Executive Dashboard"],
            "Reports": ["Weekly Growth Reports", "Monthly Reviews", "Quarterly Business Reviews", "Investor Updates"],
            "AI Workflows": ["Metrics Analyzer", "Report Generator", "Growth Diagnoser"],
        },
        "Archive": {
            "Past Campaigns": [],
            "Old Experiments": [],
            "Closed Deals": [],
            "Old Strategies": [],
            "Deprecated Playbooks": [],
        },
    }
}


def create_structure(base_path, structure):
    for name, contents in structure.items():
        folder_path = os.path.join(base_path, name)
        os.makedirs(folder_path, exist_ok=True)
        print(f"  ✓ {folder_path}")
        if isinstance(contents, dict):
            create_structure(folder_path, contents)
        elif isinstance(contents, list):
            for subfolder in contents:
                sub_path = os.path.join(folder_path, subfolder)
                os.makedirs(sub_path, exist_ok=True)
                print(f"      ✓ {sub_path}")
                with open(os.path.join(sub_path, ".gitkeep"), "w") as f:
                    pass


def count_folders(structure, count=0):
    for name, contents in structure.items():
        count += 1
        if isinstance(contents, dict):
            count = count_folders(contents, count)
        elif isinstance(contents, list):
            count += len(contents)
    return count


if __name__ == "__main__":
    base = os.getcwd()
    total = count_folders(STRUCTURE)

    print("\n🚀 Growth-OS Folder Generator")
    print(f"📍 Location: {base}")
    print(f"📁 Total folders to create: {total}")
    print("-" * 50)

    create_structure(base, STRUCTURE)

    print("-" * 50)
    print(f"\n✅ Done! {total} folders created.")
    print(f"📂 Open: {base}/Growth-OS\n")
