from fastapi import APIRouter
from admin.models import Event
api = APIRouter()


@api.get('/admin')
async def hello():
    res = await Event.all()
    return {'data': res}
