from fastapi import FastAPI

from app.api.endpoints.courts import router as courts_router

app = FastAPI()

app.include_router(courts_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Tennis Reservation API!"}