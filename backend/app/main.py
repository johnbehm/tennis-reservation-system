from fastapi import FastAPI

app = FastAPI(
    title="Tennis Reservation System API",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to the Tennis Reservation System API!"
    }