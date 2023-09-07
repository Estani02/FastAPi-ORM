# API CONVERSOR DE MAYÚSCULAS

Esta API ofrece acceso a las siguientes rutas:

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

## Cómo Utilizar la API

Para empezar a usar la API, sigue estos pasos:

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

5. Crea un archivo llamado `.env` en la raíz del proyecto y define las siguientes variables de entorno con tus propios valores:

   ```plaintext
   DB_HOST=Nombre_del_Host_de_tu_Base_de_Datos
   DB_PORT=Puerto_de_tu_Base_de_Datos
   DB_USER=Usuario_de_tu_Base_de_Datos
   DB_PASSWORD=Contraseña_de_tu_Base_de_Datos
   DB_NAME=Nombre_de_tu_Base_de_Datos
   ```

6. Inicia el servidor con el siguiente comando:

   ```bash
   uvicorn main:app --reload
   ```

Ahora puedes utilizar la API para acceder a las rutas mencionadas anteriormente y realizar solicitudes POST con la estructura JSON proporcionada.

¡Disfruta de tu API de conversión a mayúsculas! Si tienes algún problema, asegúrate de haber seguido los pasos con precisión y de que tu entorno esté correctamente configurado.