# app/routers/user.py
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db
from app.services.security import verify_password, create_access_token

router = APIRouter()

@router.post("/register/", response_model=schemas.User)
async def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user_in_db = crud.get_user_by_username(db, username=user.username)
    if user_in_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)

@router.post("/login/")
async def login_user(form_data: schemas.Login, db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, username=form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}




@router.get("/profile/", response_model=schemas.User)
async def get_profile(request: Request):
    user = request.state.user  # Retrieve user info from the request
    if user:
        return {"username": user["sub"]}
    raise HTTPException(status_code=401, detail="Not authenticated")