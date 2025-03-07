from fastapi import APIRouter

user = APIRouter()


@user.get("/login")
async def user_login():
    return {"user":"login"}

@user.get("/reg")
async def user_reg():
    return {"user":"reg"}

