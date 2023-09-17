from fastapi import (
    FastAPI,
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
# from database import SessionLocal, engine
# import models

# models.Base.metadata.create_all(bind=engine)

# templates = Jinja2Templates(directory="templates")

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
