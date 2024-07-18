from fastapi import FastAPI, status
from typing import Optional



app = FastAPI()


@app.get('/')
def first_project():
    return 'Hi'


@app.get('/first-page')
def page_one():
    return {f'massage': 'ok'}


@app.get('/first-page/{name}')
def id_pv(name: str):
    return {f'massage': '{name}'}


@app.get('/first-name/ number')
def num(number: Optional[int] = None):
    return {'number':f'{number}'}


