from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"hello": "world"}


def run_api():
    import uvicorn
    
    uvicorn.run(app, host="0.0.0.0", port=8000)