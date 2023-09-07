# API DE CONVERSIÓN A MAYÚSCULAS

Esta API ha sido desarrollada utilizando FastAPI y SQLAlchemy y se conecta a una base de datos PostgreSQL. Te permite realizar conversiones de texto a mayúsculas de manera sencilla.

## Configuración y Uso

Para configurar y utilizar esta API, sigue estos pasos:

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

5. Crea un archivo llamado `.env` en la raíz del proyecto y define la siguiente variable de entorno con tus propios valores:

    ```plaintext
      DATABASE_URL=postgresql://user_db:passwor_db@localhost/nombre_db
    ```

6. Inicia el servidor con el siguiente comando:

   ```bash
   uvicorn main:app --reload
   ```

Una vez que el servidor esté en funcionamiento, puedes utilizar la API a través de la documentación Swagger proporcionada para realizar conversiones de texto a mayúsculas y explorar otras funcionalidades disponibles.

## Acceso a la Documentación

Después de seguir los pasos de configuración mencionados en la sección anterior, puedes acceder a la documentación Swagger de FastAPI para explorar y probar los endpoints de la API. Para hacerlo, abre tu navegador web y ve a la siguiente URL:

[http://localhost:8000/docs](http://localhost:8000/docs)

La dirección puede variar según el puerto en el que se haya levantado el servidor, pero por lo general, el puerto predeterminado es 8000. Asegúrate de que tu servidor esté en ejecución antes de acceder a la documentación Swagger.

## Rutas Disponibles

### GET

- `/data`: Esta ruta te permite acceder a los datos.
- `/data/{id}`: Con esta ruta, puedes obtener un elemento de datos específico por su ID.

### POST

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