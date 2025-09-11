from fastapi import APIRouter
from app.database.model.user import User
from app.utils.auth import create_access_token, Token
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router = APIRouter()


@router.post("/token", response_model=Token)
async def login_for_access_token(user: User):
    """
    Genera y devuelve un token JWT a partir de las credenciales del usuario.
    El token incluye la información básica del usuario (sin contraseña) y se usa
    para autenticar futuras peticiones a la API.
    """
    user = user.model_dump(exclude="password")
    user["id"] = str(user["id"])
    access_token = create_access_token(data=user)
    return JSONResponse(jsonable_encoder(access_token))
