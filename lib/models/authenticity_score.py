from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from lib.db.connection import Base

class AuthenticityScore(Base):
    __tablename__ = 'authenticity_scores'

    id = Column(Integer, primary_key=True)
    influencer_id = Column(Integer, ForeignKey('influencers.id'), nullable=False)
    score = Column(Float, nullable=False)
    recorded_at = Column(DateTime, nullable=False)

    # Matches the Influencer model's "authenticity_scores" relationship
    influencer = relationship("Influencer", back_populates="authenticity_scores")

    def __repr__(self):
        return f"<AuthenticityScore(score={self.score}, recorded_at={self.recorded_at})>"
