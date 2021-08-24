from fastapi import APIRouter, status, Security, Depends

from app.models.schemas_tortoise.user import UserProfile
from app.core.security.deps import jwt_bearer, get_current_user

router = APIRouter()


@router.get("",
            name="get_user_profile",
            status_code=status.HTTP_200_OK,
            response_model=UserProfile,
            dependencies=[Security(jwt_bearer)]
)
async def get_user_profile(
        user: UserProfile = Depends(get_current_user)
) -> UserProfile:
    return user
