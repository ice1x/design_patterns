from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Base
from db import engine, get_db
from repositories.user_repository import UserRepository
from services.user_service import UserService

app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)


@app.post("/users/")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)

    existing_user = user_service.get_user_by_email(email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = user_service.create_user(name=name, email=email)
    return user


@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)

    user = user_service.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@app.get("/users/")
def list_users(db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)

    return user_service.list_users()
