from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def first_project():
    return 'Hi'
