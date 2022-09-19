from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm.session import Session
from db.database import get_db
from .schemas import RoomBase, RoomDisplay
from db import room_db
from typing import List


router = APIRouter(
    prefix='/room',
    tags=['Conference Room']
)

@router.post('/', response_model=RoomDisplay)
def newroom(request:RoomBase, db:Session = Depends(get_db)):
    try:
        return room_db.create(request, db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Error: {e}')


@router.get('/', response_model=List[RoomDisplay])
def getroom(db:Session=Depends(get_db)):
    return room_db.get_room(db)

@router.get('/{id}/',response_model=RoomDisplay)
def getroom(id:int,db:Session=Depends(get_db)):
    return room_db.get_room(db,id)

@router.put('/{id}/')
def updateroom(id:int, request:RoomBase, db:Session= Depends(get_db)):
    return room_db.update(id,request,db)

@router.delete('/{id}/')
def deleteroom(id:int, db:Session=Depends(get_db)):
    return room_db.delete(id,db)