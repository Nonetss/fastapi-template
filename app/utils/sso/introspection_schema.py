from pydantic import BaseModel, Field


class IntrospectionResponse(BaseModel):
    active: bool = Field(..., description="Indica si el token está activo")
    scope: str = Field(..., description="Alcance del token")
    client_id: str = Field(..., description="ID del cliente")
    token_type: str = Field(..., description="Tipo de token")
    exp: int = Field(..., description="Tiempo de expiración")
    iat: int = Field(..., description="Tiempo de emisión")
    auth_time: int = Field(..., description="Tiempo de autenticación")
    nbf: int = Field(..., description="No válido antes de")
    sub: str = Field(..., description="Identificador del sujeto")
    aud: list[str] = Field(..., description="Lista de audiencia")
    amr: list[str] = Field(..., description="Referencias de métodos de autenticación")
    iss: str = Field(..., description="Emisor del token")
    jti: str = Field(..., description="ID del JWT")
    username: str = Field(..., description="Nombre de usuario")
    name: str = Field(..., description="Nombre completo")
    given_name: str = Field(..., description="Nombre")
    family_name: str = Field(..., description="Apellido")
    locale: str = Field(..., description="Configuración regional del usuario")
    updated_at: int = Field(..., description="Marca de tiempo de última actualización")
    preferred_username: str = Field(..., description="Nombre de usuario preferido")
    email: str = Field(..., description="Dirección de correo electrónico")
    email_verified: bool = Field(
        ..., description="Estado de verificación del correo electrónico"
    )
