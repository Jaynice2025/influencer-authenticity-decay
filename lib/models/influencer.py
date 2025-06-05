from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from lib.db.connection import Base

class Influencer(Base):
    __tablename__ = 'influencers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    niche = Column(String, nullable=False)
    follower_count = Column(Integer, nullable=False)
    engagement_rate = Column(Float, nullable=False)
    join_date = Column(Date, nullable=False)

    partnerships = relationship("Partnership", back_populates="influencer", cascade="all, delete-orphan")
    authenticity_scores = relationship("AuthenticityScore", back_populates="influencer", cascade="all, delete-orphan")
    relationships = relationship("Relationship", back_populates="influencer", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Influencer(name='{self.name}', niche='{self.niche}')>"
