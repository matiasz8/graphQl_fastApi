from fastapi import APIRouter

from app.controllers import status_controller as router_status
from app.controllers import hello_controller as router_hello
from app.controllers import user_controller as router_user
from app.core.config import API_PREFIX


api_router = APIRouter(prefix=API_PREFIX)
api_router.include_router(router_status.router, tags=["health"], prefix="/health")
api_router.include_router(router_hello.router, tags=["hello"], prefix="/hello")
api_router.include_router(router_user.router, tags=["users"], prefix="/users")
