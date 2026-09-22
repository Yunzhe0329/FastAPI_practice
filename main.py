from typing import Annotated;
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

# Method 連線方法 GET, POST, PUT, DELETE，以REST API來看
@app.get("/")
def index():
    return FileResponse("home.html")

# 處理 GET Mrthod 的路徑 /test
@app.get("/test")
def testGET():
    return {"data" : 10, "Method":"GET"}

@app.post("/test")
def testPost():
    return {"ok":True, "Method":"POST"}