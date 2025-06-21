from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.v1.endpoints.imagery import router as imagery_router
from app.core.config import settings
from app.api.v1.endpoints import layers

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(layers.router, prefix="/api")
app.include_router(imagery_router, prefix=f"{settings.API_V1_STR}/imagery")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("map.html", {"request": request})





