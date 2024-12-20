
# Extraer Información de Emails

Este proyecto permite extraer información de correos electrónicos específicos utilizando la API de Gmail. Filtra los correos electrónicos que contienen información de seguimiento de pedidos y guarda los datos en archivos JSON.

## Requisitos

Asegúrate de tener Python instalado y las siguientes bibliotecas:

- google-auth
- google-auth-oauthlib
- google-auth-httplib2
- google-api-python-client
- tkinter

Puedes instalar las dependencias utilizando el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Configuración

1. **Credenciales de Google**: 
   - Crea un proyecto en [Google Cloud Console](https://console.cloud.google.com/).
   - Habilita la API de Gmail.
   - Configura la pantalla de consentimiento OAuth 2.0.
   - Crea credenciales OAuth 2.0 y descarga el archivo `credentials.json`.
   - Guarda el archivo `credentials.json` en el directorio del proyecto.



## Uso

1. **Ejecutar el Script Principal**:
   - Ejecuta el script main.py para iniciar el proceso de autenticación y extracción de correos electrónicos.

```bash
python main.py
```

2. **Interfaz Gráfica (Opcional)**:
   - Ejecuta el script app.py para utilizar la interfaz gráfica basada en Tkinter.

```bash
python app.py
```

## Estructura del Proyecto

- main.py : Script principal que maneja la autenticación y extracción de correos electrónicos.
- app.py : Interfaz gráfica para interactuar con el script principal.
- requirements.txt : Archivo con las dependencias necesarias.
- `credentials.json`: Archivo de credenciales de Google (no incluido en el repositorio).
- `token.pickle`: Archivo que almacena los tokens de acceso y actualización (generado automáticamente, tampoco incluida en el repo).

## Seguridad

- **Protege los Archivos de Credenciales**: Asegúrate de que los archivos `token.pickle` y `credentials.json` estén en ubicaciones seguras y con permisos adecuados, revoca tokens de ser necesario. 

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que desees realizar.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
