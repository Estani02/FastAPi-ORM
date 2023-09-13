# API DE CONVERSIÓN A MAYÚSCULAS

Esta API ha sido desarrollada utilizando FastAPI y SQLAlchemy y se conecta a una base de datos PostgreSQL. Te permite realizar conversiones de texto a mayúsculas de manera sencilla.

Puedes acceder a la API de dos maneras: de forma local o a través del siguiente enlace: [FastAPI ORM](https://fastapiorm.onrender.com/).

## Uso Local

### Configuración y Uso

1. Clona el repositorio de FastAPI ORM en tu sistema local:

   ```bash
   git clone https://github.com/Estani02/FastAPi-ORM.git
   ```

2. Navega al directorio del proyecto desde tu terminal.

3. Crea y activa un entorno virtual para aislar las dependencias del proyecto:

   ```bash
   # Crear el entorno virtual
   python -m venv venv

   # Activar el entorno virtual en Windows
   venv\Scripts\activate.bat

   # Activar el entorno virtual en Unix o MacOS
   source venv/bin/activate
   ```

4. Instala las dependencias necesarias desde el archivo `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

5. Crea un archivo llamado `.env` en la raíz del proyecto y define la siguiente variable de entorno con tus valores:

    ```plaintext
    DATABASE_URL=tu_url_de_la_base_de_datos
    ```

6. Inicia el servidor con el siguiente comando:

   ```bash
   uvicorn main:app --reload
   ```

Una vez que el servidor esté en funcionamiento, puedes utilizar la API a través de la documentación Swagger proporcionada para realizar conversiones de texto a mayúsculas y explorar otras funcionalidades disponibles.

## Rutas Disponibles

### Documentación Swagger

- `/docs`

### Rutas GET

- `/get_data`: Esta ruta te permite acceder a los datos.
- `/get_data/{id}`: Con esta ruta, puedes obtener un elemento de datos específico por su ID.

### Ruta POST

- `/input/{my_target_field}`: Utiliza esta ruta para realizar una solicitud POST y proporcionar datos en el cuerpo del mensaje. Debes ingresar la siguiente estructura JSON en el cuerpo de la solicitud:

```json
{
  "field_1": "string",
  "author": "string",
  "description": "string",
  "my_numeric_field": 0
}
```

Asegúrate de seguir el formato JSON proporcionado para realizar con éxito una solicitud POST a esta ruta.

¡Disfruta de tu API de conversión a mayúsculas desarrollada con FastAPI y SQLAlchemy! Si encuentras algún problema, asegúrate de haber seguido los pasos con precisión y de que tu entorno esté correctamente configurado.