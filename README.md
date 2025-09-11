# FastAPI Template (Async + SQLModel + Alembic + PostgreSQL)

Plantilla base para desarrollar APIs con **FastAPI**, **SQLModel**, **Alembic** y **PostgreSQL** de forma **asíncrona**.

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

4. Crea un archivo `.env` en la raíz del proyecto con tu URL de base de datos:

   ```env
   DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/mi_db
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
│       └── user/
├── core/                # Configuración (ej. variables entorno)
├── database/
│   ├── model/           # Modelos SQLModel
│   └── session.py       # Motor y sesión async
└── main.py              # Punto de entrada FastAPI
migrations/              # Scripts de Alembic
```

---

## ✅ Notas

- El motor de base de datos es **asíncrono**, usando `create_async_engine`.
- Las sesiones se gestionan con `async_sessionmaker` y se inyectan en los endpoints mediante `Depends`.
- No se crean tablas automáticamente en el arranque: la gestión de esquema se hace **exclusivamente con Alembic**.

---

## 🔗 Endpoints de ejemplo

- `POST /api/v1/user/` → Crear un usuario
