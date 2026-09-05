from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4


app = FastAPI(
    title="My Task Manager API",
    description="A full-stack learning project",
    version="1.0.0"
)


# -----------------------------
# Data Model
# -----------------------------

class Task(BaseModel):
    id: UUID
    title: str
    description: Optional[str] = None
    completed: bool = False
    created_at: datetime


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    completed: Optional[bool] = None


# -----------------------------
# Temporary Database
# -----------------------------

tasks: dict[UUID, Task] = {}


# -----------------------------
# Routes
# -----------------------------

@app.get("/")
def home():
    return {
        "message": "My Task Manager API",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "timestamp": datetime.now()
    }


# Get all tasks
@app.get("/tasks", response_model=list[Task])
def get_tasks():
    return list(tasks.values())


# Get one task
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: UUID):

    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return tasks[task_id]


# Create a task
@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task_data: TaskCreate):

    task = Task(
        id=uuid4(),
        title=task_data.title,
        description=task_data.description,
        created_at=datetime.now()
    )

    tasks[task.id] = task

    return task


# Update a task
@app.patch("/tasks/{task_id}", response_model=Task)
def update_task(
    task_id: UUID,
    task_data: TaskUpdate
):

    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    existing_task = tasks[task_id]

    updated_task = existing_task.model_copy(
        update=task_data.model_dump(
            exclude_unset=True
        )
    )

    tasks[task_id] = updated_task

    return updated_task


# Delete a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: UUID):

    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    del tasks[task_id]
from datetime import datetime
from uuid import UUID, uuid4

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


# -------------------------
# Application
# -------------------------

app = FastAPI(
    title="My Task Manager API",
    description="Backend for my first full-stack website",
    version="1.0.0"
)


# -------------------------
# CORS
# -------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------------------------
# Models
# -------------------------

class TaskCreate(BaseModel):

    title: str = Field(
        min_length=1,
        max_length=100
    )


class TaskUpdate(BaseModel):

    completed: bool


class Task(BaseModel):

    id: UUID
    title: str
    completed: bool
    created_at: datetime


# -------------------------
# Temporary Database
# -------------------------

tasks: dict[UUID, Task] = {}


# -------------------------
# Home
# -------------------------

@app.get("/")
def home():

    return {
        "message": "Task Manager API",
        "status": "running"
    }


# -------------------------
# Health Check
# -------------------------

@app.get("/health")
def health():

    return {
        "status": "ok"
    }


# -------------------------
# Get All Tasks
# -------------------------

@app.get("/tasks", response_model=list[Task])
def get_tasks():

    return list(tasks.values())


# -------------------------
# Get Single Task
# -------------------------

@app.get(
    "/tasks/{task_id}",
    response_model=Task
)
def get_task(task_id: UUID):

    if task_id not in tasks:

        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return tasks[task_id]


# -------------------------
# Create Task
# -------------------------

@app.post(
    "/tasks",
    response_model=Task,
    status_code=201
)
def create_task(task_data: TaskCreate):

    task = Task(
        id=uuid4(),
        title=task_data.title,
        completed=False,
        created_at=datetime.now()
    )

    tasks[task.id] = task

    return task


# -------------------------
# Update Task
# -------------------------

@app.patch(
    "/tasks/{task_id}",
    response_model=Task
)
def update_task(
    task_id: UUID,
    task_data: TaskUpdate
):

    if task_id not in tasks:

        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    old_task = tasks[task_id]

    updated_task = old_task.model_copy(
        update={
            "completed": task_data.completed
        }
    )

    tasks[task_id] = updated_task

    return updated_task


# -------------------------
# Delete Task
# -------------------------

@app.delete("/tasks/{task_id}")
def delete_task(task_id: UUID):

    if task_id not in tasks:

        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    del tasks[task_id]

    return {
        "message": "Task deleted successfully"
    }
    return {
        "message": "Task deleted successfully"
    }