class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.middleware_attr = 'Atributo agregado por middleware'
        return self.get_response(request)