from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models.resource import ResourceStatus

class ResourceBase(BaseModel):
    name: str
    description: Optional[str] = None
    category: str
    quantity: int = 0
    status: ResourceStatus = ResourceStatus.AVAILABLE

class ResourceCreate(ResourceBase):
    pass

class ResourceUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    quantity: Optional[int] = None
    status: Optional[ResourceStatus] = None

class Resource(ResourceBase):
    id: int
    date_added: datetime
    last_updated: Optional[datetime] = None
    owner_id: int
    
    class Config:
        from_attributes = True

class ResourceFilter(BaseModel):
    category: Optional[str] = None
    status: Optional[ResourceStatus] = None
    search: Optional[str] = None
    sort_by: Optional[str] = "date_added"
    sort_order: Optional[str] = "desc"  # "asc" or "desc"