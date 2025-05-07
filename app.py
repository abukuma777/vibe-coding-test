from fastapi import FastAPI

app = FastAPI()

<<<<<<< HEAD
@app.get("/")
def root():
    return {"message": "Vibe Coding Test API"}

=======
>>>>>>> 71d6162cc6dd729ffe2e29683176600597ce7151
@app.get("/hello")
def hello():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
<<<<<<< HEAD
    uvicorn.run(app, host="0.0.0.0", port=8000)
=======
    uvicorn.run(app, host="0.0.0.0", port=8000)
>>>>>>> 71d6162cc6dd729ffe2e29683176600597ce7151
