from fastapi import APIRouter, HTTPException
from ...schemas.auth import LoginRequest, TokenResponse, UserResponse

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login", response_model=TokenResponse)
async def login(body: LoginRequest):
    if body.username == "admin" and body.password == "admin":
        return TokenResponse(
            access_token="simulated-jwt-token",
            refresh_token="simulated-refresh-token",
        )
    raise HTTPException(status_code=401, detail="Invalid credentials")

@router.get("/me", response_model=UserResponse)
async def get_current_user():
    return UserResponse(id=1, username="admin", email="admin@vfb-bildung.de", is_active=True)
