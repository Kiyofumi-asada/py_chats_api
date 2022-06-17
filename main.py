from fastapi import FastAPI

app = FastAPI()

messageArr = [
    {
        "id": 1,
        "userId": 1,
        "userName": "user1",
        "userIcon": None,
        "message": "message post!!",
        "created_at": "2022-06-03T13:28:45.249Z",
        "updated_at": "2022-06-13T12:42:43.881Z",
        "isDelete": True
    },
    {
        "id": 2,
        "userId": 1,
        "userName": "user1",
        "userIcon": None,
        "message": "message post!!",
        "created_at": "2022-06-03T13:28:45.249Z",
        "updated_at": "2022-06-13T12:42:43.881Z",
        "isDelete":False
    },
    {
        "id": 3,
        "userId": 1,
        "userName": "user1",
        "userIcon": None,
        "message": "message post!!",
        "created_at": "2022-06-03T13:28:45.249Z",
        "updated_at": "2022-06-13T12:42:43.881Z",
        "isDelete":False
    },
    {
        "id": 4,
        "userId": 1,
        "userName": "user1",
        "userIcon": None,
        "message": "message post!! message post!! message post!! message post!! message post!! message post!! message post!! message post!! message post!!",
        "created_at": "2022-06-03T13:28:45.249Z",
        "updated_at": "2022-06-13T12:42:43.881Z",
        "isDelete":False
    },
    {
        "id": 5,
        "userId": 1,
        "userName": "user1",
        "userIcon": None,
        "message": "message post!!",
        "created_at": "2022-06-03T13:28:45.249Z",
        "updated_at": "2022-06-13T12:42:43.881Z",
        "isDelete":False
    },
    {
        "id": 6,
        "userId": 1,
        "userName": "user1",
        "userIcon": None,
        "message": "message post!! message post!! message post!!",
        "created_at": "2022-06-03T13:28:45.249Z",
        "updated_at": "2022-06-13T12:42:43.881Z",
        "isDelete":False
    },
    {
        "id": 7,
        "userId": 1,
        "userName": "user1",
        "userIcon": None,
        "message": "message post!! message post!! message post!!",
        "created_at": "2022-06-03T13:28:45.249Z",
        "updated_at": "2022-06-13T12:42:43.881Z",
        "isDelete":False
    },
    {
        "id": 8,
        "userId": 1,
        "userName": "user1",
        "userIcon": None,
        "message": "message post!! message post!! message post!! message post!! message post!! message post!! message post!! message post!! message post!!",
        "created_at": "2022-06-03T13:28:45.249Z",
        "updated_at": "2022-06-13T12:42:43.881Z",
        "isDelete":False
    },
    {
        "id": 9,
        "userId": 1,
        "userName": "user1",
        "userIcon": None,
        "message": "message post!! message post!! message post!! message post!! message post!! message post!! message post!! message post!! message post!!",
        "created_at": "2022-06-03T13:28:45.249Z",
        "updated_at": "2022-06-13T12:42:43.881Z",
        "isDelete":False
    },
    {
        "id": 10,
        "userId": 1,
        "userName": "user1",
        "userIcon": None,
        "message": "message post!! message post!! message post!! message post!! message post!! message post!! message post!! message post!! message post!!",
        "created_at": "2022-06-03T13:28:45.249Z",
        "updated_at": "2022-06-13T12:42:43.881Z",
        "isDelete":False
    },

]

@app.get("/chat")
async def root():
    return messageArr