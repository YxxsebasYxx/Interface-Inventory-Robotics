# Interfaz de Usuario para Inventario

Este proyecto es una aplicación web que permite visualizar y gestionar un inventario desde un archivo de Excel. El sistema tiene un **frontend en React** y un **backend en FastAPI** que se comunican entre sí. El backend lee los datos desde un archivo Excel y expone rutas para que el frontend los consuma.

---

## 📁 Estructura del Proyecto

```

/Interfaz_Usuario_Inventario
│
├── backend/  ← FastAPI
│   ├── api/
│   ├── config/
│   ├── data/
│   ├── repositories/
│   ├── services/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/  ← React app
│   ├── public/
│   │   ├── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── CategoryTree.jsx
│   │   │   ├── SubCategoryTree.jsx
│   │   │   ├── ItemTable.jsx
│   │   │   └── SubItemTable.jsx
│   │   ├── App.jsx
│   │   └── index.jsx)
│   └── package.json
```

## ⚙️ Requisitos

### ✅ Requisitos Generales
- Python 3.10+
- Node.js 16+ y npm
- Git

### 📦 Backend (FastAPI)
- FastAPI
- Uvicorn
- pandas
- openpyxl

### 🌐 Frontend (React)
- React + Vite o CRA
- Axios o fetch para llamadas HTTP


## 🧪 Instalación y ejecución

### 1. Clonar el repositorio

```bash

git clone https://github.com/tu_usuario/Interfaz_Usuario_Inventario.git
cd Interfaz_Usuario_Inventario
```

## Configurar y ejecutar el Backend

#### Instalar dependencias

```bash
pip install -r requirements.txt

```
#### Verificar archivo Excel

Asegúrate de que existe data/inventory.xlsx. Si no, colócalo ahí o crea un archivo con las columnas necesarias.

#### Ejecutar el servidor FastAPI

```bash

~/Interfaz_Usuario_Inventario$ uvicorn backend.main:app --reload
```
El backend estará disponible en: http://127.0.0.1:8000

#### Configurar y ejecutar el Frontend

```bash
cd ~/Interfaz_Usuario_Inventario/frontend
npm install
npm run dev
```
El frontend estará disponible en: http://localhost:3000 y en http://192.168.1.17:3000/

🤝 ¿Cómo colaborar?

Si querés contribuir al proyecto, seguí estos pasos:

## Crea una rama nueva

```bash

git checkout -b feature/nombre-de-tu-feature
```
Realiza tus cambios y commitealos

```bash

git add .
git commit -m "Descripción clara del cambio"
```
Sube la rama al repositorio

```bash

git push origin feature/nombre-de-tu-feature
```
Abre un Pull Request

Desde GitHub, abrí un PR con tu rama hacia main y describe qué cambios hiciste.

Recomendaciones

    No subas archivos .log, carpetas __pycache__, .env, venv/, node_modules, etc.

    Asegurate de tener el .gitignore configurado correctamente.

    Probá tus cambios antes de subirlos.

    Comenta tu código si es necesario.
