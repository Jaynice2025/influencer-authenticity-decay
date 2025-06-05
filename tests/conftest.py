import pytest
from lib.db.connection import SessionLocal, Base, engine
from lib.models import influencer, partnership, authenticity_score

@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown_db():
    # Drop and recreate tables before each test
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    # Optionally clear data or rollback
