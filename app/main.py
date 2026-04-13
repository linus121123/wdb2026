from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return { "msg": "Morjens!", "v": "0.2" }


@app.get("/hello")
def hello():
    return { "msg": "Hellooooo!"}
