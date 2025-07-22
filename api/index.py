import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "egg_timer_project.settings")

from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()