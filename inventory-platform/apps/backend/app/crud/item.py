from sqlalchemy.orm import Session
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate

# Create a new item
def create_item(db: Session, item: ItemCreate, owner_id: int) -> Item:
    db_item = Item(**item.dict(), owner_id=owner_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Get item by ID
def get_item(db: Session, item_id: int) -> Item | None:
    return db.query(Item).filter(Item.id == item_id).first()

# Get list of items
def get_items(db: Session, skip: int = 0, limit: int = 100) -> list[Item]:
    return db.query(Item).offset(skip).limit(limit).all()

# Update item
def update_item(db: Session, db_item: Item, updates: ItemUpdate) -> Item:
    update_data = updates.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_item, field, value)
    db.commit()
    db.refresh(db_item)
    return db_item

# Delete item
def delete_item(db: Session, db_item: Item) -> None:
    db.delete(db_item)
    db.commit()
