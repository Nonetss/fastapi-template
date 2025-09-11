from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Optional
import jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from fastapi.security import HTTPBearer

# Openssl para generar una clave:
#   openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# ---------- Modelos ----------
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ---------- Password hashing ----------
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# ---------- JWT helpers ----------
def create_access_token(
    data: Dict[str, Any], expires_delta: Optional[timedelta] = None
) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})
    encoded_jwt: str = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str) -> Dict[str, Any]:
    # Lanza InvalidTokenError si no es válido; deja que la ruta lo capture y devuelva 401
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    # opcional: validar claims mínimas aquí (sub, iat, etc.)
    return payload


# ---------- Security dependency ----------
# Úsalo en las rutas:
#   credentials: HTTPAuthorizationCredentials = Depends(security)
security = HTTPBearer(auto_error=False)
