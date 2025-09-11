from fastapi import APIRouter, Depends
from app.database.session import get_session
from app.database.model.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router = APIRouter()


@router.post("/")
async def create_user(user: User, session: AsyncSession = Depends(get_session)):
    user = User(username=user.username, password=user.password)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return JSONResponse(content=jsonable_encoder(user))
