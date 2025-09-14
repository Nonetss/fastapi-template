from pydantic import BaseModel, Field


class IntrospectionResponse(BaseModel):
    active: bool | None = Field(
        None, description="Indica si el token está activo", nullable=True
    )
    scope: str | None = Field(None, description="Alcance del token", nullable=True)
    client_id: str | None = Field(None, description="ID del cliente", nullable=True)
    token_type: str | None = Field(None, description="Tipo de token", nullable=True)
    exp: int | None = Field(None, description="Tiempo de expiración", nullable=True)
    iat: int | None = Field(None, description="Tiempo de emisión", nullable=True)
    auth_time: int | None = Field(
        None, description="Tiempo de autenticación", nullable=True
    )
    nbf: int | None = Field(None, description="No válido antes de", nullable=True)
    sub: str | None = Field(None, description="Identificador del sujeto", nullable=True)
    aud: list[str] | None = Field(None, description="Lista de audiencia", nullable=True)
    amr: list[str] | None = Field(
        None, description="Referencias de métodos de autenticación", nullable=True
    )
    iss: str | None = Field(None, description="Emisor del token", nullable=True)
    jti: str | None = Field(None, description="ID del JWT", nullable=True)
    username: str | None = Field(None, description="Nombre de usuario", nullable=True)
    name: str | None = Field(None, description="Nombre completo", nullable=True)
    given_name: str | None = Field(None, description="Nombre", nullable=True)
    family_name: str | None = Field(None, description="Apellido", nullable=True)
    locale: str | None = Field(
        None, description="Configuración regional del usuario", nullable=True
    )
    updated_at: int | None = Field(
        None, description="Marca de tiempo de última actualización", nullable=True
    )
    preferred_username: str | None = Field(
        None, description="Nombre de usuario preferido", nullable=True
    )
    email: str | None = Field(
        None, description="Dirección de correo electrónico", nullable=True
    )
    email_verified: bool | None = Field(
        None, description="Estado de verificación del correo electrónico", nullable=True
    )
