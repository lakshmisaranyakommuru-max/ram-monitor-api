from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class SystemData(BaseModel):
    ram_usage: float
    cpu_usage: float
    available_ram: float
    process_count: int


latest_data = {}


@app.get("/")
def home():
    return {"message": "RAM Monitoring API is running"}


@app.post("/data")
def receive_data(data: SystemData):
    global latest_data
    latest_data = data.model_dump()

    return {
        "status": "success",
        "message": "System data received"
    }


@app.get("/data")
def get_data():
    return latest_data