from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.session import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)  
    name = Column(String, index=True, nullable=False)  
    description = Column(String, nullable=True)         
    quantity = Column(Integer, default=0)              
    owner_id = Column(Integer, ForeignKey("users.id")) 

    owner = relationship("User", back_populates="items") 
