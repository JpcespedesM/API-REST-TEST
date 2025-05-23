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

### Obtener todos los items
- **GET** `/items/`

## Documentación

La documentación automática de la API está disponible en:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`