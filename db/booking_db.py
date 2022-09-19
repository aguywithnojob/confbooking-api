from sqlalchemy.orm import Session
from routers.schemas import BookingBase, RoomBase
from fastapi import HTTPException, status
from .models import Booking, User, Room
from routers.schemas import BookingDisplay
from datetime import datetime
from sqlalchemy import or_


def create(request:BookingBase, db:Session):
    user = db.query(User).filter(User.id  == request.user_id).first()
    if not user:
        raise Exception(f'User not found.')

    room = db.query(Room).filter(Room.id == request.room_id).first()

    if not room:
        raise Exception(f'Room does not exists.')

    if request.start_time > request.end_time :
        raise Exception(f'Please check booking time again.')

    slot = db.query(Booking).filter(
                                Booking.today_date == request.today_date
                            ).filter(
                                or_(
                                        Booking.start_time.between(request.start_time,request.end_time),
                                        Booking.end_time.between(request.start_time,request.end_time)
                                    )
                            ).filter(
                                Booking.room_id == request.room_id
                            )
    if slot.first():
        raise Exception(f'Room already booked from {slot.first().start_time} to {slot.first().end_time}.')
    # raise Exception('Under dev')
    new_slot = Booking(
        start_time =request.start_time,
        end_time = request.end_time,
        today_date = request.today_date,
        room_id = request.room_id,
        user_id = request.user_id,
        generated = datetime.now(),
        updated_timestamp = datetime.now()
    )

    db.add(new_slot)
    db.commit()
    db.refresh(new_slot)
    return new_slot


def get_slot(db:Session, id:int=None):
    if not id:
        return db.query(Booking).order_by(Booking.start_time).all()

    else:
        slot = db.query(Booking).filter(Booking.id == id).first()
        if not slot:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'slot not found')
        return slot

def update(id:int, request:RoomBase, db:Session):
   
    if request.start_time >= request.end_time:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Please check booking slot again.')

    slot = db.query(Booking).filter(Booking.id == id)
    if not slot.first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Slot not found')

    old_slot = db.query(Booking).filter(
                                Booking.today_date == request.today_date
                            ).filter(
                                or_(
                                        Booking.start_time.between(request.start_time,request.end_time),
                                        Booking.end_time.between(request.start_time,request.end_time)
                                    )
                            ).filter(
                                Booking.room_id == request.room_id
                            )
    
    if old_slot.first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Room already booked from {old_slot.first().start_time} to {old_slot.first().end_time}.')

    slot.update({
        Booking.start_time :request.start_time,
        Booking.end_time : request.end_time,
        Booking.today_date : request.today_date,
        Booking.room_id : request.room_id,
        Booking.user_id : request.user_id,
        Booking.updated_timestamp : datetime.now()
    }, synchronize_session=False)
    db.commit()
    return "Ok"

def delete(id:int, db:Session):
    slot = db.query(Booking).filter(Booking.id == id).first()
    if not slot :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'slot not found')
    db.delete(slot)
    db.commit()
    return {
        'msg':'Success',
        'id':slot.id
    }