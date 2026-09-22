## 專案啟動
 - 先建立虛擬環境 python -m venv .venv, .\.venv\Scripts\activate
 - pip install -r requirements.txt，裡面有定義專案會需要用到的 package
 - cmd -> net start MySQL80
 - uvicorn <python檔案>:<app name> --reload (會自動重新編譯)
 - 設定好.env要帶入的參數

## 字串與參數處理
- from typing import Annotated : 這個lib可以幫你的前端帶入的參數做型別標註，確保 input 是 back-end 預期的格式
- Path() : 用來處理路徑參數 (必須包含在路徑當中的參數); Query() : 用來處理URL?後面帶上的參數(選擇性帶上)

---
