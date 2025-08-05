class AuditMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Audit logic can be added here if needed
        response = self.get_response(request)
        return response