from lib.db.connection import SessionLocal, engine, Base
from lib.models.influencer import Influencer
from lib.models.partnership import Partnership
from lib.models.relationship import Relationship
import datetime

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

def main_menu():
    while True:
        print("\n🎯 Influencer Management System")
        print("1. View All Influencers")
        print("2. View All Partnerships")
        print("3. Create New Influencer")
        print("4. Create New Relationship")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            view_all_influencers()
        elif choice == '2':
            view_all_partnerships()
        elif choice == '3':
            create_influencer()
        elif choice == '4':
            create_relationship()
        elif choice == '5':
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

def view_all_influencers():
    session = SessionLocal()
    influencers = session.query(Influencer).all()
    print("\n📋 Influencers:")
    for i in influencers:
        print(f"- ID: {i.id}, Name: {i.name}, Niche: {i.niche}")
    session.close()

def view_all_partnerships():
    session = SessionLocal()
    partnerships = session.query(Partnership).all()
    print("\n🔗 Partnerships:")
    for p in partnerships:
        print(f"- {p.brand_name} with Influencer ID: {p.influencer_id} (Start: {p.start_date}, End: {p.end_date})")
    session.close()

def create_influencer():
    name = input("Enter influencer name: ")
    niche = input("Enter influencer niche: ")
    try:
        follower_count = int(input("Enter follower count (optional, default 0): ") or 0)
        engagement_rate = float(input("Enter engagement rate (optional, default 0.0): ") or 0.0)
    except ValueError:
        print("Invalid number. Try again.")
        return
    join_date = datetime.date.today()

    new_inf = Influencer.create(name=name, niche=niche, follower_count=follower_count,
                                engagement_rate=engagement_rate, join_date=join_date)
    print(f"✅ Influencer '{name}' created with ID: {new_inf.id}")

def create_relationship():
    session = SessionLocal()
    influencer_id = input("Enter Influencer ID: ")
    related_entity = input("Enter Related Entity Name (e.g., agency): ")
    relation_type = input("Enter Relationship Type (e.g., Manager): ")

    relationship = Relationship(
    influencer_id=influencer_id,
    related_entity=related_entity,
    relationship_type=relationship_type  
)

    session.add(relationship)
    session.commit()
    print("✅ Relationship added successfully!")
    session.close()

if __name__ == "__main__":
    main_menu()
