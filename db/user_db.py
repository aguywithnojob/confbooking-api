from sqlalchemy.orm import Session
from routers.schemas import UserBase
from .models import User
from auth.hashing import Hash
from datetime import datetime
from fastapi import HTTPException, status

def create(request:UserBase, db:Session):
    user = db.query(User).filter(User.email == request.email).filter(User.username == request.username).first()
    if user:
        raise Exception(f'User already exist with email:{user.email} and username:{user.username}')
    new_user = User(
        username = request.username,
        email = request.email,
        password  = Hash.bcrypt(request.password),
        generated = datetime.now()
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all(db:Session, id:int=None):
    if not id:
        return db.query(User).all()
    else:
        user =  db.query(User).filter(User.id == id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user not found')
        return user