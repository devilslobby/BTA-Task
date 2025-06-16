from fastapi import FastAPI

app = FastAPI()

@app.get("/api/hello")
def say_hello():
    return {"message": "Hello from FastAPI!"}
