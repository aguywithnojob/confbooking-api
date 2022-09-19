
from db.database import Base
from sqlalchemy import Column, Integer, String, DateTime,Date, Boolean
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship
from time import timezone
from datetime import date
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key =True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    generated  = Column(DateTime)
    booking_slot = relationship('Booking', back_populates='users')


class Room(Base):
    __tablename__ = 'room'
    id = Column(Integer, primary_key =True, index=True)
    name = Column(String)
    capacity = Column(Integer)
    vacant = Column(Boolean)
    remark = Column(String, nullable=True)
    booking_slot = relationship('Booking', back_populates='rooms')

class Booking(Base):
    __tablename__ = 'booking'
    id = Column(Integer, primary_key =True, index=True)
    today_date = Column(Date, default=date.today())
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    room_id = Column(Integer,ForeignKey('room.id'))
    rooms = relationship('Room', back_populates='booking_slot')
    user_id = Column(Integer, ForeignKey('user.id'))
    users = relationship('User', back_populates='booking_slot')
    generated = Column(DateTime)
    updated_timestamp = Column(DateTime)