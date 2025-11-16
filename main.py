import uvicorn
from src.rest_app import app
from src.config.config import settings

if __name__ == "__main__":
    uvicorn.run(
        "src.rest_app:app",
        host=settings.BACKEND_URL,
        port=settings.BACKEND_PORT,
        reload=settings.reload,
    )

