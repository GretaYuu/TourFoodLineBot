from django.urls import path, include
from django.contrib import admin
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mylinebot.settings')
application = get_wsgi_application()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('foodlinebot/', include('foodlinebot.urls'))
]
