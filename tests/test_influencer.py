from lib.models.influencer import Influencer

def test_create_influencer():
    influencer = Influencer.create("Jane Doe", "lifestyle")
    assert influencer.name == "Jane Doe"
    assert influencer.niche == "lifestyle"
