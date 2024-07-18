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


@app.get('/first-name/ {name} / {age}')
def info(name:str, age: int, number: Optional[int] = None):
    return {'name': f'{name}', 'age': f'{age}', 'number': f'{number}'}


