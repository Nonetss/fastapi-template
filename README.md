# FastAPI Template (Async + SQLModel + Alembic + PostgreSQL + SSO)

Plantilla base para desarrollar APIs con **FastAPI**, **SQLModel**, **Alembic**, **PostgreSQL** y **autenticación SSO/OAuth2** de forma **asíncrona**.

## 🔐 Características

- **Autenticación SSO/OAuth2**: Sistema de introspección de tokens integrado
- **Base de datos asíncrona**: PostgreSQL con SQLModel y Alembic
- **API moderna**: FastAPI con documentación automática
- **Validación de datos**: Schemas Pydantic para requests/responses
- **CORS configurado**: Listo para aplicaciones web

---

## 🚀 Requisitos

- Python 3.13+ (gestionado con [pyenv](https://github.com/pyenv/pyenv) o similar)
- PostgreSQL en ejecución
- [Poetry](https://python-poetry.org/) o `venv` + `pip` para manejar dependencias
- Alembic (incluido en requirements)

---

## ⚙️ Configuración

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tu-org/fastapi-template.git
   cd fastapi-template
   ```

2. Crea y activa el entorno virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Crea un archivo `.env` en la raíz del proyecto con las variables de configuración:

   ```env
   # Base de datos
   DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/mi_db

   # Configuración SSO/OAuth2
   CLIENT_ID=tu_client_id
   CLIENT_SECRET=tu_client_secret
   SSO_ISSUER=https://tu-sso-provider.com
   SSO_AUDIENCE=tu_audience
   ```

---

## ▶️ Ejecución

Lanza el servidor con **fastapi**:

```bash
fastapi dev app/main.py --host 0.0.0.0 --port 8000
```

Por defecto la API estará en: [http://localhost:8000](http://localhost:8000)

---

## 🗄️ Migraciones de Base de Datos

La gestión del esquema de la base de datos se hace con **Alembic**.

### Generar una nueva migración

Cada vez que cambies tus modelos (`app/database/model/...`):

```bash
alembic revision --autogenerate -m "Mensaje de la migración"
```

Ejemplo:

```bash
alembic revision --autogenerate -m "Init"
```

Esto crea un archivo en `migrations/versions/`.

### Aplicar migraciones

Para aplicar los cambios a la base de datos:

```bash
alembic upgrade head
```

### Revertir migraciones

Para volver atrás una versión:

```bash
alembic downgrade -1
```

---

## 📂 Estructura del Proyecto

```
app/
├── api/                 # Rutas y controladores
│   └── v1/
│       └── user/        # Endpoints de usuario
├── core/                # Configuración (variables de entorno)
├── database/
│   ├── model/           # Modelos SQLModel
│   └── session.py       # Motor y sesión async
├── utils/
│   └── sso/             # Utilidades de autenticación SSO
│       ├── introspection.py        # Lógica de introspección
│       └── introspection_schema.py # Schemas de respuesta
└── main.py              # Punto de entrada FastAPI
migrations/              # Scripts de Alembic
```

---

## 🔐 Autenticación SSO/OAuth2

Este template incluye un sistema completo de autenticación basado en **introspección de tokens OAuth2**.

### Cómo funciona

1. **Introspección de tokens**: Los tokens Bearer se validan contra el servidor SSO configurado
2. **Validación de audiencia**: Se verifica que el token esté dirigido a tu API específica
3. **Schemas tipados**: Las respuestas de introspección se validan con Pydantic
4. **Middleware automático**: Protección de endpoints mediante dependencias de FastAPI

### Uso en endpoints

```python
from app.utils.sso.introspection import introspect_token

@router.get("/protected")
async def protected_endpoint(token_data = Depends(introspect_token)):
    # token_data contiene la información del usuario autenticado
    return {"user_id": token_data.sub, "username": token_data.username}
```

### Configuración del proveedor SSO

El sistema está configurado para trabajar con cualquier proveedor OAuth2 que soporte introspección estándar (RFC 7662). Asegúrate de configurar correctamente:

- `SSO_ISSUER`: URL base de tu proveedor SSO
- `CLIENT_ID` y `CLIENT_SECRET`: Credenciales de tu aplicación
- `SSO_AUDIENCE`: Identificador de tu API en el proveedor SSO

---

## ✅ Notas

- El motor de base de datos es **asíncrono**, usando `create_async_engine`.
- Las sesiones se gestionan con `async_sessionmaker` y se inyectan en los endpoints mediante `Depends`.
- No se crean tablas automáticamente en el arranque: la gestión de esquema se hace **exclusivamente con Alembic**.

---

## 🚀 Endpoints Disponibles

### Documentación

- **GET** `/docs` - Documentación interactiva (Swagger UI)
- **GET** `/redoc` - Documentación alternativa (ReDoc)
- **GET** `/health` - Health check básico

### API v1

- **GET** `/api/v1/user/me` - Información del usuario autenticado (requiere token)
- **POST** `/api/v1/user/` - Crear un usuario

---

## 📦 Dependencias Principales

- **FastAPI**: Framework web moderno y rápido
- **SQLModel**: ORM moderno basado en Pydantic y SQLAlchemy
- **Alembic**: Migraciones de base de datos
- **asyncpg**: Driver PostgreSQL asíncrono
- **uvicorn**: Servidor ASGI de alto rendimiento
- **httpx**: Cliente HTTP asíncrono para introspección SSO
- **pyjwt**: Manejo de tokens JWT
- **passlib**: Utilidades de hashing y criptografía
