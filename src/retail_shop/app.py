from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/")
def hello():
    return {"hello": "world"}


def run_api():
   
     uvicorn.run(
        "retail_shop.app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )