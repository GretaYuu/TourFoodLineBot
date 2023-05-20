"""
URL configuration for mylinebot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#而為了要將這個Django應用程式(APP)的網址也加入到專案主程式中，所以，在Django專案主程式下的urls.py檔案中，加入以下的網址設定
from django.contrib import admin
from django.urls import path
'''
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mylinebot.settings')
application = get_wsgi_application()
'''
urlpatterns = [
    path('admin/', admin.site.urls),
]