from typing import List
from uuid import UUID, uuid4

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title='ToDo')


class Task(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    description: str = Field(
        max_length=300,
        default='',
    )
    is_completed: bool = False
    is_hot: bool = False
    is_public: bool = True


tasks: List[Task] = []


@app.get("/")
async def root():
    return 'root'


@app.get("/todo")
async def get_todo_list(id: int):
    return 'todo'


@app.get('/list')
async def get_list():
    return 'list'


@app.get('/task/{task_id}')
async def get_task(task_id: UUID):
    return [el for el in tasks if el.id == task_id]


@app.post('/task')
async def create_task(task: Task):
    tasks.append(task)
    return f'{task.id}'