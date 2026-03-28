from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
from datalayer.database import get_db_session
from services.auth_service import AuthService
from typing import List

router = APIRouter(tags=["Authentication"])

@router.post("/register")
async def register(request: Request, db: AsyncSession = Depends(get_db_session)):
    try:
        data = await request.json()
        if not data.get("username") or not data.get("email") or not data.get("password"):
             raise HTTPException(status_code=400, detail="Missing required fields")
        
        service = AuthService(db)
        user = await service.register_user(data)
        return {"message": "Registration successful", "user_id": user.user_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/users")
async def get_users(db: AsyncSession = Depends(get_db_session)):
    try:
        service = AuthService(db)
        users = await service.get_all_users()
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/login")
async def login(request: Request, db: AsyncSession = Depends(get_db_session)):
    # Simple login placeholder logic
    return {"message": "Login successful"}
