from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

# FastAPI 앱 생성
app = FastAPI()

# 대시보드 HTML 제공
@app.get("/")
def read_dashboard():
    current_dir = os.path.dirname(__file__)  # 현재 파일의 경로
    dashboard_path = os.path.join(current_dir, "static", "dashboard.html")  # dashboard.html 경로
    return FileResponse(dashboard_path)  # HTML 파일 반환
