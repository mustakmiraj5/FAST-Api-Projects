from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm

from app.database import get_db
from app.schemas import UserCreate, UserRead, Token
from app.crud import user_crud
from app.core.security import create_access_token, verify_password, get_password_hash

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def register_user(request: UserCreate, db: AsyncSession = Depends(get_db)):
    existing_user = await user_crud.get_user_by_email(db, request.email)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    hashed_password = get_password_hash(request.password)

    new_user = await user_crud.create_user(
        db,
        email=request.email,
        hashed_password=hashed_password
    )

    return new_user


@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    user = await user_crud.get_user_by_email(db, form_data.username)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    token = create_access_token({"sub": str(user.id)})

    return {"access_token": token, "token_type": "bearer"}
