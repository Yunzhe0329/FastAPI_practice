from typing import Annotated
from fastapi import FastAPI, Path, Query
from fastapi.responses import JSONResponse, FileResponse, RedirectResponse, PlainTextResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
app = FastAPI()

# non-static file 
@app.get("/member")
def member():
    return RedirectResponse("/login")
@app.get("/square")
def square(num: Annotated[int, None]):
    result = num*num
    return {"計算結果" : result}
@app.get("/multiply")
def multiply(n1: Annotated[int, None], n2: Annotated[int, None]):
    result = n1*n2
    return {"運算結果" : result}

# static file
@app.get("/")
def index():
    return FileResponse("index.html")
app.mount("/static", StaticFiles(directory="static"))

@app.get("/form")
def form():
    return FileResponse("form.html")