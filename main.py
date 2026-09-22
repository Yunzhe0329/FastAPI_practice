import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()
# 建立資料庫連線
con = mysql.connector.connect(
    user= os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host = os.getenv("DB_HOST"),
    database= os.getenv("DB_NAME")
)

print("connection sucessful!")

from fastapi import FastAPI
from typing import Annotated
app = FastAPI()

@app.get("/createMessage")
def createMessage(author: Annotated[str, None], content:Annotated[str,None]):
    cursor = con.cursor() # cursor 是 mysql.connector 操作 DB 的 interface
    # %s 代表我要傳入資料
    cursor.execute("INSERT INTO message(author, content) VALUES(%s,%s)", [author, content])
    con.commit()
    return {"ok":True}

    
    