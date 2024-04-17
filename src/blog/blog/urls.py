from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',include('main.urls',namespace='main')),
    path('',include('web.urls',namespace='web')),
    path('user/',include('user.urls',namespace='user')),
    path('posts/',include('posts.urls',namespace='posts')),
]
