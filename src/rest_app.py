import os
from fastapi.middleware.cors import CORSMiddleware
from src.app.custom_app import CustomApp
from src.routers.menu_router import menu_router


app = CustomApp(
    title="MenuService"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv('FRONTEND_URL')],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    menu_router
)
