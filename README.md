# fastapi_crud

API sencilla de CRUD de usuarios hecha con **FastAPI**. Usa un archivo `db.json` como "base de datos" falsa (no hay base de datos real todavía).

## Requisitos

- Docker
- Docker Compose

## Cómo correrlo

Desde la carpeta `backend/` (donde está el `docker-compose.yml`):

```bash
docker compose up --build
```

Esto construye la imagen del servicio `api` y levanta el contenedor. La API queda disponible en:

```
http://localhost:8000
```

Para correrlo en segundo plano, agrega `-d`:

```bash
docker compose up --build -d
```

Para detenerlo:

```bash
docker compose down
```

## Endpoints

| Método | Ruta            | Descripción                    |
|--------|-----------------|---------------------------------|
| GET    | `/`              | Lista todos los usuarios        |
| POST   | `/create_user`   | Crea un usuario nuevo           |
| PATCH  | `/update_user`   | Actualiza un usuario existente  |
| DELETE | `/delete_user`   | Elimina un usuario              |

Puedes probar todos los endpoints desde la documentación interactiva de FastAPI:

```
http://localhost:8000/docs
```

### Ejemplos

**Crear usuario**
```
POST /create_user?name=Juan&email=juan@mail.com&password=1234
```

**Actualizar usuario**
```
PATCH /update_user?id_to_update=1
Body (JSON):
{
  "name": "Juan Actualizado",
  "email": "nuevo@mail.com",
  "password": "5678"
}
```

**Eliminar usuario**
```
DELETE /delete_user?id=1
```

## Estructura del proyecto

```
backend/
├── docker-compose.yml
└── api/
    ├── Dockerfile
    ├── main.py
    ├── requirements.txt
    ├── db.json
    ├── database/
    │   └── db.py
    └── routes/
        ├── create_user.py
        ├── update_user.py
        └── delete_user.py
```

## Notas

- Los datos se guardan en `api/db.json`. Al arrancar, la app carga ese archivo en memoria y cada creación/edición/borrado lo vuelve a escribir.
- Este proyecto todavía no usa una base de datos real; eso se puede agregar más adelante.
