from fastapi import APIRouter

api = APIRouter()


@api.get("/")
def get_login():
    return "admin app created!"
