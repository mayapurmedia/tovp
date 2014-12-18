from django.conf import settings


def variables(request):
    return {
        'current_url': request.path,
        'settings': settings,
    }
