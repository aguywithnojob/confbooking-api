from fastapi import FastAPI
from db.database import engine
from db import models
from routers import user, room, booking, authentication

app = FastAPI()
# app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(room.router)
app.include_router(booking.router)

models.Base.metadata.create_all(engine)