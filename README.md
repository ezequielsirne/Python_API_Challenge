# Python_API_Challenge

API REST desarrollada con **FastAPI**, siguiendo los principios de **Clean Architecture**, con persistencia en **SQLite** y pruebas unitarias e integradas. Esta API permite la gestión de personajes mediante endpoints RESTful.

---

## ✅ Requisitos

- Python 3.10 o superior
- `uv` (recomendado) o `venv`
- Docker (opcional para contenedor)

---

## ⚙️ Instalación local

### 1. Crear entorno virtual

```bash
# Recomendado: usando uv
uv venv .venv
source .venv/bin/activate
uv pip install -r requirements.txt

# Alternativa: usando venv estándar
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🚀 Ejecución local

```bash
uvicorn app.main:app --reload
```

La API estará disponible en:

- Documentación Swagger: http://localhost:8000/docs
- Documentación Redoc: http://localhost:8000/redoc

---

## 🐳 Ejecución con Docker

```bash
# Build
docker compose build

# Run
docker compose up
```

---

## 🧪 Tests automatizados

```bash
# Ejecutar todos los tests
pytest
```

Se ejecutan:
- Tests unitarios (servicios con repositorio falso)
- Tests de integración con TestClient (endpoints reales)

---

## 🧭 Endpoints disponibles

| Método | Ruta                         | Descripción                          |
|--------|------------------------------|--------------------------------------|
| GET    | `/character/getAll`         | Lista todos los characters (DTO)     |
| GET    | `/character/get/{id}`       | Devuelve un character por ID         |
| POST   | `/character/add`            | Inserta un nuevo character           |
| DELETE | `/character/delete/{id}`    | Elimina un character por ID          |

> ⚠️ Todos los campos deben ser válidos, no nulos y únicos por ID.

---

## 📨 Colección Postman

En la carpeta `postman/` se incluye una colección para probar la API:

```bash
postman/character_api_collection.json
```

Importala en Postman para probar fácilmente los endpoints.

---

## 🧱 Estructura del proyecto

```text
app/
├── api/                   # Routers FastAPI
├── application/           # Servicios (casos de uso)
├── domain/                # Entidades y contratos
│   ├── dto/               # DTOs de entrada/salida
│   └── services/          # Interfaces de servicio
├── infrastructure/        # Base de datos, repositorios
└── main.py                # Punto de entrada
tests/                     # Tests unitarios e integrados
postman/                   # Colección Postman
Dockerfile
docker-compose.yml
requirements.txt
```

---

## 📌 Principales características

- ✅ FastAPI + Pydantic v2
- ✅ Arquitectura limpia (Clean Architecture)
- ✅ Repository Pattern
- ✅ Inyección de dependencias
- ✅ Validaciones estrictas (`strict=True`)
- ✅ Colección Postman
- ✅ Contenerización con Docker

---

## 🧠 Autor

Desarrollado por Ezequiel Sirne para challenge técnico.
