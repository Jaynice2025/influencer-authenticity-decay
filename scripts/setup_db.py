from lib.db.connection import Base, engine
from lib.models.influencer import Influencer
from lib.models.partnership import Partnership
from lib.models.authenticity_score import AuthenticityScore
from lib.models.relationship import Relationship  # Add this line

if __name__ == "__main__":
    print("Creating database...")
    Base.metadata.create_all(engine)
    print("Done.")
