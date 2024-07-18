from fastapi import FastAPI, status
from typing import Optional



app = FastAPI()


@app.get('/')
def first_project():
    return 'Hi'


@app.get('/first-page')
def page_one():
    return {f'massage': 'ok'}


@app.get('/first-page/{ids}')
def id_pv(ids: str):
    return {'massage': f'{ids}'}


@app.get('/first-page/{name}/{age}')
def info(name: str, age: int, number: Optional[int] = None):
    return {'name': name,
            'age': age,
            'number': number
            }


