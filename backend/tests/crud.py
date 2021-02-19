# 增删改查
from app.database import SessionLocal
from admin.models import Room, RoomPlate
from admin.models import Order
from sqlalchemy import and_
from sqlalchemy.orm.query import Query
session = SessionLocal()



def get_all_room():
    query = session.query(Room).all()
    return list(query)

def get_all_room_plate():
    query = session.query(RoomPlate).all()
    return list(query)

def join_order_room_plate(order_id: int):
    """

    :param order_id:
    :return:
    """
    room_ids = session.query(Order.room_ids).filter(Order.id == order_id)
    print(room_ids.first())
    # query:Query = room_ids.one()
    # print(query)
    if room_ids.first():
        query: Query = room_ids
        room_ids = query[0].split(',')
        # print(type(room_ids), room_ids)
        query = session.query(Room, RoomPlate)
        query = query.filter(
            and_(
                Room.id==RoomPlate.room_id,
                Room.id.in_(room_ids)
            )
        )
    else:
        query = []
    return list(query)