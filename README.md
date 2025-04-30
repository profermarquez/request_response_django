# contexto:
Este proyecto es una aplicación educativa de Django que muestra ejemplos prácticos del uso de objetos y funcionalidades de HTTP, como:

HttpRequest y sus atributos.

HttpResponse y sus subclases (JsonResponse, StreamingHttpResponse, FileResponse).

Middleware y atributos personalizados.

Procesamiento de formularios (GET/POST).

Seguridad (is_secure).

Manejo de desconexiones simuladas.

# Accede en tu navegador a:

http://127.0.0.1:8000/ → Página de inicio con links a todos los endpoints.

Ejemplos:

http://127.0.0.1:8000/request/

http://127.0.0.1:8000/request/querydict/?nombre=Juan

http://127.0.0.1:8000/response/json/

Para probar el formulario de home:

Ve a http://127.0.0.1:8000/home/

Ingresa un nombre y envíalo (POST), verás una respuesta JSON con el saludo.

# Cómo probarlo con Postman
Abre Postman y crea nuevas peticiones:

GET:
URL: http://127.0.0.1:8000/request/

Método: GET

POST (formulario):
URL: http://127.0.0.1:8000/home/

Método: POST

Body → x-www-form-urlencoded:

Key: nombre, Value: Carlos

JSON Response:
URL: http://127.0.0.1:8000/response/json/

Método: GET

Verás: {"mensaje": "¡Hola desde JsonResponse!"}