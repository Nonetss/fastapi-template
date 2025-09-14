import base64
import httpx
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.config import CLIENT_ID, CLIENT_SECRET, SSO_INTROSPECT, SSO_AUDIENCE
from app.utils.sso.introspection_schema import IntrospectionResponse


bearer = HTTPBearer(auto_error=True)


async def introspect_token(
    creds: HTTPAuthorizationCredentials = Depends(bearer),
) -> IntrospectionResponse:
    token = creds.credentials

    basic = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
    headers = {
        "Authorization": f"Basic {basic}",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    data = {"token": token}
    # Recomendado: httpx.AsyncClient y timeout bajo + reintento si quieres
    async with httpx.AsyncClient(timeout=3.0) as client:
        r = await client.post(SSO_INTROSPECT, data=data, headers=headers)
    if r.status_code != 200:
        raise HTTPException(status_code=401, detail="Introspection failed")

    info = r.json()
    # Respuesta estándar: {"active": true/false, "sub": "...", "aud": "...", "scope": "...", ...}
    if not info.get("active"):
        raise HTTPException(status_code=401, detail="Invalid or revoked token")

    # Valida audiencia (muy importante): el token debe ir dirigido a tu API
    # Añade aquí la(s) aud permitida(s)
    allowed_aud = {SSO_AUDIENCE}
    token_aud = info.get("aud")
    if isinstance(token_aud, str):
        token_aud = {token_aud}
    if not (set(token_aud or []) & allowed_aud):
        raise HTTPException(status_code=403, detail="Invalid audience")

    return IntrospectionResponse(**info)
