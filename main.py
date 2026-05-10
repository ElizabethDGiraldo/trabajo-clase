from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def inicio(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"ano_actual": datetime.now().year}
    )


@app.get("/materiales", response_class=HTMLResponse)
async def materiales(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="materiales.html",
        context={"ano_actual": datetime.now().year}
    )


@app.get("/salubridad", response_class=HTMLResponse)
async def salubridad(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="salubridad.html",
        context={"ano_actual": datetime.now().year}
    )


@app.get("/tecnicas", response_class=HTMLResponse)
async def tecnicas(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="tecnicas.html",
        context={"ano_actual": datetime.now().year}
    )