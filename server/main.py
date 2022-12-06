from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
import pickledb


## Database
class Database:
    def __init__(self):
        self.db = pickledb.load("Atlas.db", False)

    def get(self, key):
        return self.db.get(key)


    def put(self, key, value):
        self.db.set(key, value)
        self.db.dump()
       
    def delete(self, key):
        self.db.rem(key)
        self.db.dump()

    def getall(self):
        rtn = []
        for key in list(self.db.getall()):
            rtn.append(self.db.get(key))

        return rtn
 
db = Database()

## Models
class Itenerary(BaseModel):
    UID : str
    src: str
    dest: str
    price: float

    def to_json(self):
        return {
            "uid": self.UID,
            "src": self.src,
            "dest": self.dest,
            "price": self.price
        }


## Resources Endpoints
app = FastAPI()
@app.get('/')
async def welcome():
    return {"message": "Welcome to Atlas's API!"}

@app.get('/trips')
async def get_all_trips():
    return db.getall()    

@app.post("/trips")
async def post_trip(trip: Itenerary ):
    return db.put(trip.UID , trip.to_json())


@app.get("/trip/{trip_id}")
async def get_trip(trip_id: str):
    return db.get(trip_id)

@app.delete("/trips/{trip_id}")
async def delete_trip(trip_id : str):
    return db.delete(trip_id)
