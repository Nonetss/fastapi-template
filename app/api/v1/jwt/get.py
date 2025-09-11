from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials
from app.utils.auth import security, decode_access_token

router = APIRouter()


@router.get("/user")
async def read_users_me(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    """
    Devuelve la información contenida en el token JWT enviado en la cabecera Authorization.
    Sirve como ejemplo sencillo de autenticación con Bearer token.
    """
    token = credentials.credentials
    payload = decode_access_token(token)
    return payload
