from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from lib.db.connection import Base

class Partnership(Base):
    __tablename__ = 'partnerships'

    id = Column(Integer, primary_key=True)
    brand_name = Column(String, nullable=False)
    influencer_id = Column(Integer, ForeignKey('influencers.id'), nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
    content_details = Column(String)

    influencer = relationship("Influencer", back_populates="partnerships")

    def __repr__(self):
        return f"<Partnership {self.brand_name} with Influencer ID {self.influencer_id}>"
