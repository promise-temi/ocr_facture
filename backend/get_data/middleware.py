import time
from .models import LogEntry

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        duration = round(time.time() - start, 4)

        method = request.method
        path = request.path
        status = response.status_code
        ip = self.get_client_ip(request)
        view_name = getattr(request.resolver_match, 'view_name', None)

        message = f"{method} {path} - {status} - Vue: {view_name}"

        LogEntry.objects.create(
            level='INFO',
            message=message,
            path=path,
            method=method,
            status_code=status,
            view_name=view_name,
            ip_address=ip,
            duration=duration,
            extra_data={}  # Ajoute ce que tu veux ici
        )

        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')
