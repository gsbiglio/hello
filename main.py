from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello(greeting):
    return {
        'status' : 200,
        'message' : 'Hi! , How are you?'
    }