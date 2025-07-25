from fastapi import APIRouter, Depends
from app.schemas.user import User as UserSchema
from app.models.user import User
from app.api.deps import get_current_active_user

router = APIRouter()

@router.get("/me", response_model=UserSchema)
def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user