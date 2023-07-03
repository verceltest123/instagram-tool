# myapp/middleware.py

class CORPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Add the Cross-Origin Resource Policy headers
        response["Cross-Origin-Resource-Policy"] = "none"

        return response
    

class CustomSecurityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Add the 'Cross-Origin-Embedder-Policy' header to the response
        response['Cross-Origin-Embedder-Policy'] = 'unsafe-none'
        
        return response

