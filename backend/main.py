import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from backend.api.routes import router



app = FastAPI()

# 1. CORS para desarrollo React en localhost:3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Solo dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Montar las rutas de tu API bajo /api (opcional pero recomendado)
app.include_router(router)

# 3. Servir el build de React en producción
#    Asume que en la raíz de tu proyecto hay la carpeta `frontend/build`
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
react_build_dir = os.path.join(BASE_DIR, os.pardir, "frontend", "build")

