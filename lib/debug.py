from lib.db.connection import Session
from lib.models.influencer import Influencer

session = Session()

influencers = session.query(Influencer).all()
for inf in influencers:
    print(inf)
