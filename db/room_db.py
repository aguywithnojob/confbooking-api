from sqlalchemy.orm import Session
from routers.schemas import RoomBase
from fastapi import HTTPException, status
from .models import Room

def create(request:RoomBase, db:Session):
    room = db.query(Room).filter(Room.name == request.name).first()
    if room:
        raise Exception(f'Room already exist with name:{room.name}.')
    
    new_room = Room(
        name =request.name,
        capacity = request.capacity,
        vacant = request.vacant,
        remark = request.remark
    )

    db.add(new_room)
    db.commit()
    db.refresh(new_room)
    return new_room


def get_room(db:Session, id:int=None):
    if not id:
        return db.query(Room).all()

    else:
        room = db.query(Room).filter(Room.id == id).first()
        if not room:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'room not found')
        return room

def update(id:int, request:RoomBase, db:Session):
    room = db.query(Room).filter(Room.id == id)
    if not room.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'room not found')
    
    room.update({
        Room.name :request.name,
        Room.capacity : request.capacity,
        Room.vacant : request.vacant,
        Room.remark : request.remark
    })
    db.commit()
    return 'Ok'

def delete(id:int, db:Session):
    room = db.query(Room).filter(Room.id == id).first()
    if not room :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'room not found')
    db.delete(room)
    db.commit()
    return {
        'msg':'Success',
        'id':room.id,
        'name':room.name
    }