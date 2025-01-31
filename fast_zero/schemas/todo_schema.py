from datetime import datetime

from pydantic import BaseModel

from fast_zero.models.models import TodoState


class TodoSchema(BaseModel):
    title: str
    description: str
    state: TodoState


class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    state: TodoState | None = None


class TodoPublic(TodoSchema):
    id: int
    created_at: datetime
    updated_at: datetime


class TodoList(BaseModel):
    todos: list[TodoPublic]
