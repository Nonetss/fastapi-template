from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.utils.sso.introspection import introspect_token

router = APIRouter()


@router.get("/me")
async def get_user(
    token: HTTPBearer = Depends(introspect_token),
):
    return JSONResponse(jsonable_encoder(token))
