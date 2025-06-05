from tabulate import tabulate
from lib.db.connection import SessionLocal
from lib.models.influencer import Influencer
from lib.models.relationship import Relationship
from lib.controllers.display import list_influencers, list_relationships
from datetime import datetime

def main_menu():
    session = SessionLocal()
    while True:
        print("\n🎯 Influencer Management System")
        print("1. View All Influencers")
        print("2. View All Relationships")
        print("3. Create New Influencer")
        print("4. Create New Relationship")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            list_influencers(session)
        elif choice == "2":
            list_relationships(session)
        elif choice == "3":
            create_influencer(session)
        elif choice == "4":
            create_relationship(session)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

def create_influencer(session):
    name = input("Enter influencer's name: ")
    platform = input("Enter platform (e.g., Instagram, TikTok): ")
    follower_count = int(input("Enter follower count: "))

    new_influencer = Influencer(name=name, platform=platform, follower_count=follower_count)
    session.add(new_influencer)
    session.commit()
    print(f"✅ Influencer '{name}' added successfully.")

def create_relationship(session):
    influencer_id = int(input("Enter Influencer ID: "))
    related_entity = input("Enter Related Entity Name (e.g., agency): ")
    relationship_type = input("Enter Relationship Type (e.g., Manager): ")

    new_relationship = Relationship(
        influencer_id=influencer_id,
        related_entity=related_entity,
        relationship_type=relationship_type
    )
    session.add(new_relationship)
    session.commit()
    print("✅ Relationship added successfully.")
