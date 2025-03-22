from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas import UserCreate, UserResponse, Token
from app.models.models import User
from app.auth.security import hash_password, verify_password, create_access_token
from app.core.dependencies import get_db_dependency

router = APIRouter()

# ✅ Register a new user
@router.post("/register", response_model=UserResponse)
async def register_user(user_data: UserCreate, db: AsyncSession = Depends(get_db_dependency)):
    # Check if user already exists
    result = await db.execute(select(User).where(User.email == user_data.email))
    existing_user = result.scalars().first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered.")

    # Hash password and create user
    new_user = User(
        email=user_data.email,
        password=hash_password(user_data.password)
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user


# ✅ Log in and receive a token
@router.post("/login", response_model=Token)
async def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db_dependency)):
    result = await db.execute(select(User).where(User.email == form_data.username))
    user = result.scalars().first()

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password.")

    token_data = {"sub": str(user.id)}
    access_token = create_access_token(data=token_data)

    return {"access_token": access_token, "token_type": "bearer"}
