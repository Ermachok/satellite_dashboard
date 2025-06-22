from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.v1.endpoints.imagery import router as clouds_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(clouds_router)

templates = Jinja2Templates(directory="app/templates")

LAYER_ID = "MODIS_Terra_Cloud_FR"


@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("map.html", {"request": request})
