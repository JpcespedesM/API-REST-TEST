from fastapi import FastAPI
from routes import items

app = FastAPI()

# Incluir las rutas de items
app.include_router(items.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)