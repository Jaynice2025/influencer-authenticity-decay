from tabulate import tabulate
from lib.db.connection import SessionLocal
from lib.models.influencer import Influencer
from lib.models.partnership import Partnership
from lib.models.authenticity_score import AuthenticityScore
from lib.models.relationship import Relationship
from lib.controllers.display import list_influencers, list_relationships
from datetime import datetime

def list_menu():
    print("\nMain Menu:")
    print("1. View Influencers")
    print("2. View Relationships")
    print("3. Exit")

def main():
    session = SessionLocal()
    while True:
        list_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            list_influencers(session)
        elif choice == "2":
            list_relationships(session)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
