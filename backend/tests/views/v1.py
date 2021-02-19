from fastapi import APIRouter
from admin.crud import get_all_room, get_all_room_plate, join_order_room_plate

api = APIRouter()


@api.get("/")
async def get_login():
    return "admin app created!"


@api.get('/GetRoom')
async def get_room():
    room = get_all_room()
    return room

@api.get('/GetRoomPlate')
async def get_room_plate():
    room_plate = get_all_room_plate()
    return room_plate

@api.post('/jorp')
async def jorp(order_id: int):
    jo = join_order_room_plate(order_id)
    return jo