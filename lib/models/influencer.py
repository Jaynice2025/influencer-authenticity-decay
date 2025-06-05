from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from lib.db.connection import Base
from datetime import date

class Influencer(Base):
    __tablename__ = 'influencers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    niche = Column(String, nullable=False)
    follower_count = Column(Integer, nullable=False)
    engagement_rate = Column(Float, nullable=False)
    join_date = Column(Date, nullable=False, default=date.today)  

    partnerships = relationship("Partnership", back_populates="influencer", cascade="all, delete-orphan")
    authenticity_scores = relationship("AuthenticityScore", back_populates="influencer", cascade="all, delete-orphan")
    relationships = relationship("Relationship", back_populates="influencer", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Influencer(name='{self.name}', niche='{self.niche}')>"

    
    @classmethod
    def create(cls, db_session, name, niche, follower_count, engagement_rate, join_date=None):
        if join_date is None:
            join_date = date.today()  

        
        new_influencer = cls(
            name=name,
            niche=niche,
            follower_count=follower_count,
            engagement_rate=engagement_rate,
            join_date=join_date
        )

        try:
            
            db_session.add(new_influencer)
            db_session.commit()

            
            db_session.refresh(new_influencer)
            
            return new_influencer
        except Exception as e:
            db_session.rollback()  
            print(f"Error creating influencer: {e}")
            return None
