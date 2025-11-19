from fastapi.middleware.cors import CORSMiddleware
from src.app.custom_app import CustomApp
from src.routers.menu_router import menu_router
from src.config.config import settings
from src.routers.payment_router import payment_router

app = CustomApp(
    title="MenuService"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL], # TODO: в проде сейчас "*"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    menu_router
)

app.include_router(
    payment_router
)

