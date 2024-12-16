from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

# 정적 파일 제공 설정
app.mount("/static", StaticFiles(directory="docs"), name="static")

@app.get("/")
async def read_root():
    return {"message": "대시보드 준비 완료!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
