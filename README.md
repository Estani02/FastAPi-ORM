# API CONVERSOR DE MAYÚSCULAS

Esta API está diseñada para convertir texto a mayúsculas. Sigue estos pasos para configurar y ejecutar la aplicación en tu entorno local.

## Configuración de la Base de Datos

Primero, debes crear una base de datos PostgreSQL llamada "uppercase_converter" antes de continuar.

## Clonar el Repositorio

Clona el repositorio de FastAPI ORM en tu sistema local.

```bash
git clone https://github.com/Estani02/FastAPi-ORM.git
```

Luego, navega al directorio del proyecto desde tu terminal.

## Creación de un Entorno Virtual

Es una práctica recomendada utilizar entornos virtuales para aislar las dependencias del proyecto. Crea y activa un entorno virtual de la siguiente manera:

```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual en Windows
venv\Scripts\activate.bat

# Activar el entorno virtual en Unix o MacOS
source venv/bin/activate
```

## Instalación de Dependencias

Instala las dependencias necesarias para el proyecto desde el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Configuración de Variables de Entorno

Crea un archivo llamado `.env` en la raíz del proyecto y define las siguientes variables de entorno con tus propios valores:

```plaintext
DB_HOST=Nombre_del_Host_de_tu_Base_de_Datos
DB_PORT=Puerto_de_tu_Base_de_Datos
DB_USER=Usuario_de_tu_Base_de_Datos
DB_PASSWORD=Contraseña_de_tu_Base_de_Datos
DB_NAME=Nombre_de_tu_Base_de_Datos
```

## Iniciar el Servidor

Una vez configurado todo, puedes iniciar el servidor con el siguiente comando:

```bash
uvicorn main:app --reload
```

Si has seguido todos estos pasos correctamente, la API estará funcionando y podrás acceder a ella desde tu navegador o realizar solicitudes a través de herramientas como Postman.

¡Disfruta de tu API de conversión a mayúsculas! Si tienes algún problema, asegúrate de haber seguido los pasos con precisión y de que tu entorno esté correctamente configurado.