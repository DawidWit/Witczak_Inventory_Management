from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_, desc, asc
from typing import List, Optional
from app.database import get_db
from app.schemas.resource import Resource as ResourceSchema, ResourceCreate, ResourceUpdate, ResourceFilter
from app.models.resource import Resource, ResourceStatus
from app.models.user import User
from app.api.deps import get_current_active_user

router = APIRouter()

@router.post("/", response_model=ResourceSchema, status_code=status.HTTP_201_CREATED)
def create_resource(
    resource: ResourceCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    # Automatically set status based on quantity
    if resource.quantity == 0:
        status_value = ResourceStatus.OUT_OF_STOCK
    elif resource.quantity <= 10:  # You can make this configurable
        status_value = ResourceStatus.LOW_STOCK
    else:
        status_value = ResourceStatus.AVAILABLE
    
    db_resource = Resource(
        **resource.dict(),
        owner_id=current_user.id,
        status=status_value
    )
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    
    return db_resource

@router.get("/", response_model=List[ResourceSchema])
def read_resources(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    category: Optional[str] = Query(None),
    status: Optional[ResourceStatus] = Query(None),
    search: Optional[str] = Query(None),
    sort_by: str = Query("date_added"),
    sort_order: str = Query("desc"),
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    query = db.query(Resource).filter(Resource.owner_id == current_user.id)
    
    # Apply filters
    if category:
        query = query.filter(Resource.category == category)
    
    if status:
        query = query.filter(Resource.status == status)
    
    if search:
        query = query.filter(
            or_(
                Resource.name.ilike(f"%{search}%"),
                Resource.description.ilike(f"%{search}%")
            )
        )
    
    # Apply sorting
    if hasattr(Resource, sort_by):
        column = getattr(Resource, sort_by)
        if sort_order.lower() == "desc":
            query = query.order_by(desc(column))
        else:
            query = query.order_by(asc(column))
    
    resources = query.offset(skip).limit(limit).all()
    return resources

@router.get("/{resource_id}", response_model=ResourceSchema)
def read_resource(
    resource_id: int,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    resource = db.query(Resource).filter(
        Resource.id == resource_id,
        Resource.owner_id == current_user.id
    ).first()
    
    if resource is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resource not found"
        )
    
    return resource

@router.put("/{resource_id}", response_model=ResourceSchema)
def update_resource(
    resource_id: int,
    resource_update: ResourceUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    resource = db.query(Resource).filter(
        Resource.id == resource_id,
        Resource.owner_id == current_user.id
    ).first()
    
    if resource is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resource not found"
        )
    
    # Update fields
    update_data = resource_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(resource, field, value)
    
    # Automatically update status based on quantity if quantity was updated
    if "quantity" in update_data:
        if resource.quantity == 0:
            resource.status = ResourceStatus.OUT_OF_STOCK
        elif resource.quantity <= 10:
            resource.status = ResourceStatus.LOW_STOCK
        else:
            resource.status = ResourceStatus.AVAILABLE
    
    db.commit()
    db.refresh(resource)
    
    return resource

@router.delete("/{resource_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_resource(
    resource_id: int,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    resource = db.query(Resource).filter(
        Resource.id == resource_id,
        Resource.owner_id == current_user.id
    ).first()
    
    if resource is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resource not found"
        )
    
    db.delete(resource)
    db.commit()

@router.get("/categories/list", response_model=List[str])
def get_categories(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    categories = db.query(Resource.category).filter(
        Resource.owner_id == current_user.id
    ).distinct().all()
    
    return [category[0] for category in categories if category[0]]