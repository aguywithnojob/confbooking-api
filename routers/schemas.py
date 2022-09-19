from datetime import datetime, date
from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    username : str
    email : str
    password : str

class User(BaseModel):
    id : int
    username : str
    class Config:
        orm_mode = True


class UserDisplay(BaseModel):
    id:int
    username : str
    email : str
    password : str
    generated  : datetime
    class Config:
        orm_mode = True



class RoomBase(BaseModel):
    name : str
    capacity : int 
    vacant : bool
    remark : Optional[str]

class Room(BaseModel):
    id:int
    name:str
    capacity:int
    class Config:
        orm_mode = True




class BookingBase(BaseModel):
    start_time : datetime
    end_time : datetime
    today_date: date
    room_id: int
    user_id :int

class BookingDisplay(BaseModel):
    id:int
    start_time : datetime
    end_time : datetime
    today_date: date
    users: User
    rooms: Room
    generated : datetime
    updated_timestamp: datetime
    class Config:
        orm_mode = True


class Booking(BaseModel):
    id: int
    start_time: datetime
    end_time : datetime
    today_date: date
    users: User
    class Config:
        orm_mode = True


class RoomDisplay(BaseModel):
    id:int
    name : str
    capacity : int 
    vacant : bool
    remark : Optional[str]
    booking_slot : List[Booking]
    class Config:
        orm_mode = True

