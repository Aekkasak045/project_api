from pydantic import BaseModel
from typing import Optional

import uvicorn

from fastapi import FastAPI

from action import Action

app = FastAPI()

class User(BaseModel):
    #ID: Optional[int]
    username: Optional[str]
    password: Optional[str]
    name: Optional[str]
    last_name: Optional[str]
    address: Optional[str]

class chagnePasswordAndName(BaseModel):
    id: Optional[int]
    user_password: Optional[str]
    Name: Optional[str]


class login(BaseModel):
    username: Optional[str]
    user_password: Optional[str]


#--------------rout
@app.get("/")
async def read_root():
    return {"Con":"Start"}

@app.get("/user/get")
async def us_get():
    data = Action.getUS()
    return data

@app.get("/user/get_id")
async def us_get_id(id):
    data = Action.getUSID(id)
    return data

@app.get("/user/add_us")
async def us_add(StudentNumber,Name,LastName):
    data = Action.addUS(StudentNumber,Name,LastName)
    return data

@app.get("/user/updata_role_us")
async def us_updata(user_role_id,id):
    data = Action.updataUS(user_role_id,id)
    return data

@app.get("/hw/delete_US")
async def DeleteUS(id):
    data = Action.DeleteUS(id)
    return data

@app.get("/user/hw_get_id")
async def hw_getID(id):
    data = Action.get_hwID(id)
    return data

@app.get("/hw/updata_hw")
async def updata_hw(status,value,id):
    data = Action.updata_hw(status,value,id)
    return data

@app.post("/login")
async def login(user: login):
    data = Action.login(user)
    return data

@app.post("/changePassword_and_Name")
async def chang_pasword(user: chagnePasswordAndName):
    data = Action.changePasswordAndName(user)
    return data

    

if __name__ == "__main__":
    uvicorn.run(app, host="192.168.0.101", port=8000)