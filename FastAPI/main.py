from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

# 정적 파일 제공 설정 (docs/images 폴더 내 이미지 제공)
app.mount("/static", StaticFiles(directory="docs"), name="static")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the dashboard!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
