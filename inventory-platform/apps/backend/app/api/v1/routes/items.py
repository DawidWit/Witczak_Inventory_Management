from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=list[schemas.item.ItemOut])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    return crud.item.get_items(db=db, skip=skip, limit=limit)

@router.post("/", response_model=schemas.item.ItemOut)
def create_item(item: schemas.item.ItemCreate, db: Session = Depends(deps.get_db)):
    return crud.item.create_item(db=db, item=item, owner_id=1)

@router.get("/{item_id}", response_model=schemas.item.ItemOut)
def read_item(item_id: int, db: Session = Depends(deps.get_db)):
    db_item = crud.item.get_item(db=db, item_id=item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.put("/{item_id}", response_model=schemas.item.ItemOut)
def update_item(item_id: int, updates: schemas.item.ItemUpdate, db: Session = Depends(deps.get_db)):
    db_item = crud.item.get_item(db, item_id=item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return crud.item.update_item(db, db_item=db_item, updates=updates)

@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int, db: Session = Depends(deps.get_db)):
    db_item = crud.item.get_item(db, item_id=item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    crud.item.delete_item(db, db_item=db_item)
