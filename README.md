# Python_API_Challenge

API REST desarrollada con **FastAPI**, siguiendo los principios de **Clean Architecture**, con persistencia en **SQLite** y pruebas unitarias e integradas. Esta API permite la gestión de personajes mediante endpoints RESTful.

---

## ✅ Requisitos

- Python 3.10 o superior
- `uv` (recomendado) o `venv`
- Docker (opcional para contenedor)

> Si no tenés instalado `uv`, podés hacerlo así:
>
```bash
pip install uv
```

---

## 📥 Clonar el repositorio

Antes de comenzar con la instalación, cloná este repositorio en tu máquina local:
```bash
git clone https://github.com/ezequielsirne/Python_API_Challenge.git
cd Python_API_Challenge
```

---

## ⚙️ Instalación local (Windows)

### Crear entorno virtual

```bash
pip install uv
uv venv .venv
.venv\Scripts\activate
uv pip install -r requirements.txt
```

> ### Alternativa: usando venv estándar
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

> ### Alternativa para Linux/Mac

```bash
# Recomendado: usando uv
uv venv .venv
source .venv/bin/activate
uv pip install -r requirements.txt

# Alternativa: usando venv estándar
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

```

---

## 🚀 Ejecución local (Windows)

```bash
uvicorn app.main:app --reload
```

La API estará disponible en:

- Documentación Swagger: http://localhost:8000/docs
- Documentación Redoc: http://localhost:8000/redoc

---

## 🐳 Ejecución con Docker

```bash
docker compose build

docker compose up
```

---

## 🧪 Tests automatizados

> Ejecutar todos los tests con uv (recomendado)
```bash
pytest
```

> Ejecutar un archivo específico
```bash
pytest app/tests/test_character_service.py
pytest app/tests/test_character_endpoints.py
```

Se ejecutan:
- Tests unitarios (servicios con repositorio falso)
- Tests de integración con TestClient (endpoints reales)

---

## 🧱 Endpoints disponibles

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

## 📁 Estructura del proyecto

```text
app/
├── api/
│   └── character_router.py
├── application/
│   ├── repositories/
│   └── services/
├── domain/
│   ├── dtos/
│   ├── entities/
│   └── services/
├── infrastructure/
│   ├── repositories/
│   └── database.py
├── tests/
│   └── __init__.py
├── main.py
postman/
├── character_api_collection.json
characters.sqlite3
Dockerfile
docker-compose.yml
requirements.txt
README.md
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

## 🗒️ Comentarios

Este proyecto aplica **Clean Architecture**, dividiendo la lógica de negocio, la infraestructura y los controladores en capas independientes.

Se implementó el patrón **Repository** mediante una interfaz abstracta que define las operaciones básicas de acceso a datos (`get_all`, `get_by_id`, `add`, `delete`). Esta interfaz permite desacoplar la lógica de negocio de la tecnología usada para persistencia, y su implementación concreta en infrastructure puede ser reemplazada sin afectar las capas superiores. Esto mantiene la lógica limpia y centrada en el dominio.

La **inyección de dependencias** con `Depends()` desacopla servicios y controladores, y facilita los tests con objetos simulados.

Las **interfaces en domain** muestran claramente qué operaciones forman parte del negocio sin exponer detalles técnicos.

Además, se usó un **DTO** para limitar los campos devueltos por `/character/getAll`, cumpliendo con el requisito de mostrar datos parciales.


