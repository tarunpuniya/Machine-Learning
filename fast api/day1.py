from fastapi import FastAPI

app = FastAPI()
@app.get('/hello')
def hello():
    return{'message':"Hello world"}

@app.get('/about')
def about():
    return{'message':"I am in 3rd year of my college"}
