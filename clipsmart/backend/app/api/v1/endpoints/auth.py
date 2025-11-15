"""
Authentication endpoints.
"""

from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.database import get_db
from app.core.security import (
    get_password_hash,
    verify_password,
    create_access_token,
    get_current_user,
)
from app.core.exceptions import AuthenticationError, ValidationError
from app.models.user import User, UserTier
from app.schemas.user import UserCreate, UserLogin, UserResponse, Token
from app.core.config import get_settings

settings = get_settings()
router = APIRouter()


@router.post("/register", response_model=Token, status_code=status.HTTP_201_CREATED)
async def register(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    """
    Register a new user.
    """
    # Check if email already exists
    result = await db.execute(
        select(User).where(User.email == user_data.email)
    )
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    # Check if username already exists
    result = await db.execute(
        select(User).where(User.username == user_data.username)
    )
    existing_username = result.scalar_one_or_none()

    if existing_username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already taken"
        )

    # Create new user
    user = User(
        email=user_data.email,
        username=user_data.username,
        full_name=user_data.full_name,
        hashed_password=get_password_hash(user_data.password),
        tier=UserTier.FREE,
        is_active=True,
        is_verified=False,
        quota_reset_date=datetime.utcnow() + timedelta(days=30),
    )

    db.add(user)
    await db.commit()
    await db.refresh(user)

    # Create access token
    access_token = create_access_token(
        data={"sub": user.id}
    )

    # Update last login
    user.last_login = datetime.utcnow()
    await db.commit()

    return Token(
        access_token=access_token,
        token_type="bearer",
        user=UserResponse(
            id=user.id,
            email=user.email,
            username=user.username,
            full_name=user.full_name,
            is_active=user.is_active,
            is_verified=user.is_verified,
            tier=user.tier.value,
            monthly_quota_used=user.monthly_quota_used,
            monthly_quota_limit=user.monthly_quota_limit,
            created_at=user.created_at,
            last_login=user.last_login,
        )
    )


@router.post("/login", response_model=Token)
async def login(
    credentials: UserLogin,
    db: AsyncSession = Depends(get_db)
):
    """
    Login with email and password.
    """
    # Get user by email
    result = await db.execute(
        select(User).where(User.email == credentials.email)
    )
    user = result.scalar_one_or_none()

    if not user or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user account"
        )

    # Create access token
    access_token = create_access_token(
        data={"sub": user.id}
    )

    # Update last login
    user.last_login = datetime.utcnow()
    await db.commit()

    return Token(
        access_token=access_token,
        token_type="bearer",
        user=UserResponse(
            id=user.id,
            email=user.email,
            username=user.username,
            full_name=user.full_name,
            is_active=user.is_active,
            is_verified=user.is_verified,
            tier=user.tier.value,
            monthly_quota_used=user.monthly_quota_used,
            monthly_quota_limit=user.monthly_quota_limit,
            created_at=user.created_at,
            last_login=user.last_login,
        )
    )


@router.get("/me", response_model=UserResponse)
async def get_current_user_info(
    current_user: User = Depends(get_current_user)
):
    """
    Get current user information.
    """
    return UserResponse(
        id=current_user.id,
        email=current_user.email,
        username=current_user.username,
        full_name=current_user.full_name,
        is_active=current_user.is_active,
        is_verified=current_user.is_verified,
        tier=current_user.tier.value,
        monthly_quota_used=current_user.monthly_quota_used,
        monthly_quota_limit=current_user.monthly_quota_limit,
        created_at=current_user.created_at,
        last_login=current_user.last_login,
    )


@router.post("/refresh", response_model=Token)
async def refresh_token(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Refresh access token.
    """
    # Create new access token
    access_token = create_access_token(
        data={"sub": current_user.id}
    )

    # Update last login
    current_user.last_login = datetime.utcnow()
    await db.commit()

    return Token(
        access_token=access_token,
        token_type="bearer",
        user=UserResponse(
            id=current_user.id,
            email=current_user.email,
            username=current_user.username,
            full_name=current_user.full_name,
            is_active=current_user.is_active,
            is_verified=current_user.is_verified,
            tier=current_user.tier.value,
            monthly_quota_used=current_user.monthly_quota_used,
            monthly_quota_limit=current_user.monthly_quota_limit,
            created_at=current_user.created_at,
            last_login=current_user.last_login,
        )
    )
