import uvicorn
from src.rest_app import app


if __name__ == "__main__":
    uvicorn.run(
        app=app,
    )

