from django.http import HttpRequest, HttpResponse, JsonResponse, StreamingHttpResponse, HttpResponseNotAllowed, FileResponse, Http404
from django.shortcuts import render
import time


def base_context():
    return {
        'routes': [
            ('/request/', 'HttpRequest objects'),
            ('/request/app-attributes/', 'Attributes set by application code'),
            ('/request/middleware/', 'Attributes set by middleware'),
            ('/request/querydict/', 'QueryDict objects'),
            ('/request/is-secure/', 'HttpRequest.is_secure()'),
            ('/home/', 'Vista GET/POST combinada (formulario demo)'),  # <- nueva ruta
            ('/response/', 'HttpResponse objects'),
            ('/response/subclasses/', 'HttpResponse subclasses'),
            ('/response/json/', 'JsonResponse'),
            ('/response/streaming/', 'StreamingHttpResponse'),
            ('/response/disconnects/', 'Handling disconnects'),
            ('/response/file/', 'FileResponse'),
            ('/response/base/', 'HttpResponseBase'),
        ]
    }


def home_view(request):
    if request.method == 'GET':
        # Mostrar un formulario o una página informativa
        return render(request, 'edu_http/home.html')

    elif request.method == 'POST':
        # Procesar datos del formulario
        nombre = request.POST.get('nombre', 'Invitado')
        return JsonResponse({'mensaje': f'Hola {nombre}, recibimos tu POST con éxito.'})

    else:
        # Método no permitido (ej: PUT, DELETE, etc.)
        return HttpResponseNotAllowed(['GET', 'POST'], 'Método no permitido')

def request_example(request: HttpRequest):
    context = base_context()
    context.update({
        'method': request.method,
        'headers': dict(request.headers),
        'path': request.path,
        'GET': dict(request.GET),
        'user': str(request.user),
    })
    return render(request, 'edu_http/request.html', context)


def app_attributes_example(request):
    request.custom_attr = "Este atributo fue seteado en la vista."
    return HttpResponse(f"request.custom_attr: {request.custom_attr}")


def middleware_example(request):
    return HttpResponse(f"request.middleware_attr: {getattr(request, 'middleware_attr', 'No seteado')}")


def querydict_example(request):
    context = base_context()
    context.update({
        'get_data': dict(request.GET),
        'post_data': dict(request.POST),
    })
    return render(request, 'edu_http/querydict.html', context)


def response_example(request):
    return HttpResponse("Esto es un HttpResponse básico.")


def response_subclasses_example(request):
    response = HttpResponse("Este es un HttpResponse con encabezados.")
    response['X-Ejemplo'] = 'ValorHeader'
    return response


def json_response_example(request):
    return JsonResponse({'mensaje': '¡Hola desde JsonResponse!'})


def stream_response_example(request):
    def generador():
        yield 'Inicio del stream...\n'
        time.sleep(1)
        yield 'Mitad del stream...\n'
        time.sleep(1)
        yield 'Fin del stream.\n'
    return StreamingHttpResponse(generador(), content_type='text/plain')


def disconnect_example(request):
    return HttpResponse("Simulación de desconexión no implementada (requiere test desde cliente).")

import os
from django.conf import settings
BASE_DIR = settings.BASE_DIR

def file_response_example(request):
    file_path = os.path.join(BASE_DIR, 'files', 'example.txt')
    if not os.path.exists(file_path):
        raise Http404("Archivo no encontrado.")
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='example.txt')


def response_base_example(request):
    resp = HttpResponse("Esto extiende de HttpResponseBase")
    return resp

def index(request):
    context = base_context()
    return render(request, 'edu_http/index.html', context)

def is_secure_example(request):
    context = {
        'secure': request.is_secure()
    }
    context.update(base_context())
    return render(request, 'edu_http/is_secure.html', context)
