from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
import enum

class ResourceStatus(str, enum.Enum):
    AVAILABLE = "Available"
    LOW_STOCK = "Low Stock"
    OUT_OF_STOCK = "Out of Stock"

class Resource(Base):
    __tablename__ = "resources"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    description = Column(String)
    category = Column(String, nullable=False, index=True)
    quantity = Column(Integer, nullable=False, default=0)
    status = Column(Enum(ResourceStatus), nullable=False, default=ResourceStatus.AVAILABLE)
    date_added = Column(DateTime(timezone=True), server_default=func.now())
    last_updated = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Foreign key to user
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="resources")
