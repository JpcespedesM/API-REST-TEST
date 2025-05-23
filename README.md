# API REST de Items

Esta es una API REST simple que permite crear y obtener items con nombre y precio.

## Estructura del Proyecto
```
.
├── app.py              # Punto de entrada de la aplicación
├── routes/             # Carpeta de rutas
│   └── items.py       # Rutas relacionadas con items
└── requirements.txt    # Dependencias del proyecto
```

## Requisitos

- Python 3.7+
- FastAPI
- Uvicorn

## Instalación

1. Instala las dependencias:
```bash
pip install -r requirements.txt
```

2. Ejecuta el servidor:
```bash
python app.py
```

El servidor se ejecutará en `http://localhost:8000`

## Endpoints

### Crear un nuevo item
- **POST** `/items/`
- Body:
```json
{
    "nombre": "Ejemplo",
    "precio": 99.99
}
```
El sistema generará automáticamente un ID único para el item.

### Obtener todos los items
- **GET** `/items/`
- Respuesta:
```json
[
    {
        "id": "123e4567-e89b-12d3-a456-426614174000",
        "nombre": "Ejemplo",
        "precio": 99.99
    }
]
```

### Obtener un item por ID
- **GET** `/items/{item_id}`
- Ejemplo: `GET /items/123e4567-e89b-12d3-a456-426614174000`
- Respuesta:
```json
{
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "nombre": "Ejemplo",
    "precio": 99.99
}
```
- Si el item no existe, devolverá un error 404 con el mensaje "Item no encontrado"

## Documentación

La documentación automática de la API está disponible en:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`