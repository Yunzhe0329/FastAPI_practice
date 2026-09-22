# 幫 input 做資料格式的標註
from typing import Annotated
from fastapi import FastAPI, Path, Query
from fastapi.responses import JSONResponse 
app = FastAPI()

@app.get("/")
def index():
    return {"Hello FastAPI"}

# Query() — 參數是網址問號後面的查詢字串, "GET /hello?name=Tom"
@app.get("/hello")
def hello(name:Annotated[str, Query(min_length=2, max_length=30)]):
    message = f"Hello {name}"
    return {"message": message}

# Path() — 參數是網址路徑的一部分"/square/{number}"
@app.get("/square/{number}")
def square(number: Annotated[int, Path(ge=1)]):
    result = number * number
    return {"result" : result}

@app.get("/multiply")
def multiply(
    n1: Annotated[int, Query(ge=0, le=10)],
    n2: Annotated[int, Query(ge=0, le=10)]
):
    n1 = int(n1)
    n2 = int(n2)
    result = n1 * n2
    return {"result": result}

@app.get("/echo/{name}")
def echo(name: Annotated[str, Path(min_length=2, max_length=30, description="")]):
    return {"message": "Hello" + name}
