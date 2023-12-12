import uvicorn
from fastapi import FastAPI
from router.api_router import api_router


app = FastAPI()

app.include_router(api_router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="debug",
        workers=1000,
        limit_concurrency=1000,
        access_log=True,
    )
