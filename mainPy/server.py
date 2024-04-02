from fastapi import FastAPI
from typing import Dict
from requestHandler import requestDataHandle
from GoogleDataFetch import getLocationRadius
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

class CoordonatesRequest(BaseModel):
    coordonates: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],  
    allow_headers=["*"], 
   
)

@app.get("/")
def read_root():
    return {"Main": "Python Api"}




@app.post("/getPopularTimesData")
def get_popular_times_data(coordonates: CoordonatesRequest):
   print(coordonates)
   try:
    placeData = getLocationRadius(coordonates.coordonates)  
    data = requestDataHandle(placeData)
   except Exception as e:
      return {"error": str(e)}
   return {"data": data}