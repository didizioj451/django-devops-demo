from django.http import JsonResponse
from django.db import connection
from django.views.decorators.cache import never_cache
import time

@never_cache
def health_check(request):
    """Endpoint de santé pour monitoring"""
    start_time = time.time()
    
    try:
        # Test de la base de données
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            
        # Calcul du temps de réponse
        response_time = (time.time() - start_time) * 1000
        
        return JsonResponse({
            'status': 'healthy',
            'database': 'connected',
            'response_time_ms': round(response_time, 2),
            'timestamp': time.time()
        })
        
    except Exception as e:
        return JsonResponse({
            'status': 'unhealthy',
            'error': str(e),
            'timestamp': time.time()
        }, status=503)
