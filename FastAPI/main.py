from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

# 정적 파일 제공 설정 (docs 디렉토리에서 제공)
app.mount("/static", StaticFiles(directory="docs"), name="static")

# 기본 경로에서 index.html 파일을 제공
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return HTMLResponse(content=open("docs/index.html", encoding="utf-8").read())

# /dashboard 경로에서 dashboard.html 파일을 제공
@app.get("/dashboard", response_class=HTMLResponse)
async def show_dashboard():
    return HTMLResponse(content=open("docs/dashboard.html", encoding="utf-8").read())

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
