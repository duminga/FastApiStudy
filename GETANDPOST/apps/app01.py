from fastapi import APIRouter

app01 = APIRouter()

@app01.get("/user/1")
def get_user():
    # print("id:",id,type(id))
    return {
        "user_id": "root_user"
    }

@app01.get("/user/{id}")
def get_user(id):
    print("id:",id,type(id))
    return {
        "user_id": id
    }

@app01.get("/articles/{id}")
def get_user(id):
    print("id:",id)
    return {
        "articles_id": id
    }