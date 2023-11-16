from fastapi import (
    FastAPI,
    Body,
    Depends,
    Form,
    Header,
    Query,
    Request,
    Response,
    Security,
    status,
)

from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from sqlalchemy.orm import Session
from typing import Annotated, Union

from pydantic import BaseModel, Field


app = FastAPI()

numbers = [1,2,3]

@app.get("/")
async def root():
    return {"message": "Hello World"}

class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: Union[float, None] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results





# @app.post("/add")
# def add(req: Request, title: str = Form(...), db: Session = Depends(get_db)):
#     new_todo = models.Todo(title=title)
#     db.add(new_todo)
#     db.commit()
#     url = app.url_path_for("home")
#     return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)

# @app.get("/update/{todo_id}")
# def add(req: Request, todo_id: int, db: Session = Depends(get_db)):
#     todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
#     todo.complete = not todo.complete
#     db.commit()
#     url = app.url_path_for("home")
#     return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)


# @app.get("/delete/{todo_id}")
# def add(req: Request, todo_id: int, db: Session = Depends(get_db)):
#     todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
#     db.delete(todo)
#     db.commit()
#     url = app.url_path_for("home")
#     return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)
