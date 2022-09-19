from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm.session import Session
from db.database import get_db
from .schemas import BookingBase, BookingDisplay
from db import booking_db
from typing import List

router = APIRouter(
    prefix='/bookslot',
    tags=['Slot Booking']
)

@router.post('/', response_model=BookingDisplay)
def newslot(request:BookingBase, db:Session=Depends(get_db)):
    try:
        return booking_db.create(request,db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Error: {e}')

@router.get('/', response_model=List[BookingDisplay])
def getslot(db:Session=Depends(get_db)):
    return booking_db.get_slot(db)

@router.get('/{id}/',response_model=BookingDisplay)
def getslot(id:int,db:Session=Depends(get_db)):
    return booking_db.get_slot(db,id)

@router.put('/{id}/')
def updateslot(id:int, request:BookingBase, db:Session= Depends(get_db)):
    return booking_db.update(id,request,db)

@router.delete('/{id}/')
def deleteslot(id:int, db:Session=Depends(get_db)):
    return booking_db.delete(id,db)