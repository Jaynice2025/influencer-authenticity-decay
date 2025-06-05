from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from lib.db.connection import Base

class Relationship(Base):
    __tablename__ = 'relationships'

    id = Column(Integer, primary_key=True)
    influencer_id = Column(Integer, ForeignKey('influencers.id'), nullable=False)
    related_entity = Column(String, nullable=False)  # e.g., Manager, Agency, Friend
    relationship_type = Column(String, nullable=False)  # e.g., "Manager", "Agency"

    influencer = relationship("Influencer", back_populates="relationships")

    def __repr__(self):
        return f"<Relationship(type='{self.relationship_type}', entity='{self.related_entity}')>"
