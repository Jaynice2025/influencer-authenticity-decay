from datetime import date, datetime
from lib.db.connection import SessionLocal, engine, Base
from lib.models.influencer import Influencer
from lib.models.partnership import Partnership
from lib.models.authenticity_score import AuthenticityScore
from lib.models.relationship import Relationship

def seed_influencers():
    session = SessionLocal()
    influencers_data = [
        Influencer(name="Jaynice Wathuo", niche="Fashion", follower_count=200000, engagement_rate=0.6, join_date=date(2025, 6, 4)),
        Influencer(name="Jane Doe", niche="Sports", follower_count=90000, engagement_rate=0.07, join_date=date(2025, 6, 4)),
        Influencer(name="Trevor Mint", niche="Skincare", follower_count=8700, engagement_rate=0.2, join_date=date(2025, 6, 4)),
        Influencer(name="Vivian K", niche="Makeup", follower_count=2780, engagement_rate=0.02, join_date=date(2025, 6, 4)),
    ]
    session.add_all(influencers_data)
    session.commit()
    session.close()

def seed_partnerships():
    session = SessionLocal()
    partnerships_data = [
        Partnership(influencer_id=1, brand_name="BrandA", start_date=date(2025, 5, 1), end_date=date(2025, 5, 31), content_details="Sponsored post"),
        Partnership(influencer_id=2, brand_name="BrandB", start_date=date(2025, 4, 15), end_date=date(2025, 5, 15), content_details="Video campaign"),
    ]
    session.add_all(partnerships_data)
    session.commit()
    session.close()

def seed_authenticity_scores():
    session = SessionLocal()
    scores_data = [
        AuthenticityScore(influencer_id=1, score=0.95, recorded_at=datetime(2025, 6, 1)),
        AuthenticityScore(influencer_id=2, score=0.85, recorded_at=datetime(2025, 6, 2)),
    ]
    session.add_all(scores_data)
    session.commit()
    session.close()

def seed_relationships():
    session = SessionLocal()
    relationships_data = [
        Relationship(influencer_id=1, related_influencer_id=2, relation_type="collaboration"),
    ]
    session.add_all(relationships_data)
    session.commit()
    session.close()

def main():
    Base.metadata.create_all(bind=engine)

    seed_influencers()
    seed_partnerships()
    seed_authenticity_scores()
    seed_relationships()

    print("Seeding complete!")

if __name__ == "__main__":
    main()
