from tabulate import tabulate
from lib.models.influencer import Influencer
from lib.models.partnership import Partnership
from lib.models.authenticity_score import AuthenticityScore
from lib.models.relationship import Relationship

def list_influencers(session):
    influencers = session.query(Influencer).all()
    if not influencers:
        print("No influencers found.")
    else:
        table_data = []
        for inf in influencers:
            partnerships = ", ".join([p.brand for p in inf.partnerships])
            scores = ", ".join([f"{s.score:.1f}" for s in inf.authenticity_scores])

            table_data.append([
                inf.id,
                inf.name,
                inf.niche,
                inf.follower_count,
                f"{inf.engagement_rate:.2f}",
                inf.join_date,
                partnerships or "—",
                scores or "—"
            ])

        headers = ["ID", "Name", "Niche", "Followers", "Engagement", "Joined", "Brands", "Scores"]
        print("\n📋 Influencer Overview:\n")
        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

def list_relationships(session):
    relationships = session.query(Relationship).all()
    if not relationships:
        print("No relationships found.")
        return

    table_data = [
        [r.id, r.influencer.name, r.related_entity, r.relationship_type]
        for r in relationships
    ]
    headers = ["ID", "Influencer", "Related Entity", "Type"]
    print("\n🔗 Relationships:\n")
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
