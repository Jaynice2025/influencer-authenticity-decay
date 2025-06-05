from tabulate import tabulate
from lib.db.connection import SessionLocal
from lib.models.influencer import Influencer
from lib.models.relationship import Relationship
from lib.controllers.display import list_influencers, list_relationships
from datetime import datetime

def main_menu(db):
    while True:
        print("\n🎯 Influencer Management System")
        print("1. View All Influencers")
        print("2. View All Relationships")
        print("3. Create New Influencer")
        print("4. Create New Relationship")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            list_influencers(db)
        elif choice == "2":
            list_relationships(db)
        elif choice == "3":
            create_influencer(db)  
        elif choice == "4":
            create_relationship(db)  
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

def create_influencer(db):
    
    name = input("Enter influencer's name: ")
    niche = input("Enter influencer's niche: ")
    follower_count = int(input("Enter follower count: "))
    engagement_rate = float(input("Enter engagement rate: "))

    
    new_influencer = Influencer.create(
        db,  
        name=name,
        niche=niche,
        follower_count=follower_count,
        engagement_rate=engagement_rate
    )

    if new_influencer:
        print(f"✅ Influencer '{new_influencer.name}' added successfully.")
    else:
        print("❌ Failed to create influencer.")
