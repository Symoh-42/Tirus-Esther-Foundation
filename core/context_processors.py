from dashboard.models import Settings

def all_settings(request):
    settings = Settings.objects.first()
    context = {
        "settings":settings
    }
    return context

