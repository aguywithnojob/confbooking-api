from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm.session import Session
from db.database import get_db
from .schemas import UserBase, UserDisplay
from db import user_db
from typing import List

router = APIRouter(
    prefix='/user',
    tags=['user']
)

@router.post('/', response_model=UserDisplay)
def newuser(request:UserBase, db:Session = Depends(get_db)):
    try:
        return user_db.create(request, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Error: {e}')


@router.get('/', response_model=List[UserDisplay])
def getuser(db:Session=Depends(get_db)):
    return user_db.get_all(db)

@router.get('/{id}/',response_model=UserDisplay)
def getuser(id:int,db:Session=Depends(get_db)):
    return user_db.get_all(db,id)
        