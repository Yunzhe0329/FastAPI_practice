from typing import Annotated;
from fastapi import FastAPI,Body
from fastapi.responses import FileResponse
import json
app = FastAPI()

# Method 連線方法 GET, POST, PUT, DELETE，以REST API來看
@app.get("/")
def index():
    return FileResponse("home.html")

# 處理 GET Mrthod 的路徑 /test
@app.get("/test")
def testGET():
    return {"data" : 10, "Method":"GET"}

@app.post("/add")
def testPost(body=Body(None)):
    data=json.loads(body)
    print(data)
    result = data["n1"]+data["n2"]
    return {"result":result }