# Proyecto SENA - Viacol (Movilidad)

Repositorio oficial para el trabajo colaborativo del equipo en la API de optimización de transporte intermunicipal.

## 👥 Integrantes:
- David Rodríguez (Líder Técnico)
- Jhonny Esteban Mosuca Gomez
- Anngi Lorena Leandro Abril
- Santiago Alexander Chaves Rodriguez

---

## 🚀 Instrucciones de Despliegue Local

Sigue estos 7 pasos exactos para ejecutar el proyecto en tu máquina local:

### 1. Clonar el repositorio
```bash
git clone [https://github.com/wilchesdavid611-tech/Proyecto-Sena.git](https://github.com/wilchesdavid611-tech/Proyecto-Sena.git)
cd Proyecto-Sena
```

### 2. Configuración del Entorno Virtual
Es obligatorio crear un entorno virtual para aislar las dependencias del proyecto.
- **Crear el entorno virtual:**
  ```bash
  python -m venv venv
  ```
- **Activar el entorno virtual (Windows):**
  ```bash
  .\venv\Scripts\activate
  ```

### 3. Instalar Dependencias
Con el entorno virtual activado, instala todas las librerías necesarias ejecutando:
```bash
pip install -r requirements.txt
```

### 4. Variables de Entorno (.env)
Por seguridad, las credenciales reales de la base de datos y las llaves JWT no se suben a GitHub. 
1. Busca el archivo llamado `.env.example` en la raíz del proyecto.
2. Crea una copia de ese archivo y renómbrala como `.env`.
3. Llena el archivo `.env` con tus credenciales locales y tu llave secreta.

### 5. Ejecutar Migraciones de Base de Datos
Antes de arrancar la aplicación, debes generar las tablas de seguridad (Usuarios y Roles) en tu base de datos ejecutando las migraciones de Alembic:
```bash
alembic upgrade head
```

### 6. Ejecutar el Servidor
Para levantar la API localmente con recarga automática, ejecuta:
```bash
uvicorn app.main:app --reload
```

### 7. Documentación Activa (Swagger UI)
Una vez que el servidor esté corriendo, puedes ver y probar todos los endpoints documentados ingresando en tu navegador a:
- **Swagger UI:** http://127.0.0.1:8000/docs