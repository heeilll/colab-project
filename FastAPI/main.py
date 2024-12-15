from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

# 정적 파일 제공 설정 (dashboard.html 위치)
app.mount("/static", StaticFiles(directory="docs"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    # index.html을 기본 페이지로 보여줍니다.
    return HTMLResponse(content=open("docs/index.html", encoding="utf-8").read())

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
