# 設定這個LINE Bot應用程式(APP)的連結網址
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('callback', views.callback)
]

# 將這個Django應用程式(APP)的網址也加入到專案主程式中

urlpatterns = [
    path('admin/', admin.site.urls),
    path('foodlinebot/', include('foodlinebot.urls'))  # 包含應用程式的網址
]
