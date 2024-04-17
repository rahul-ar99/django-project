from django.urls import path 
from posts.views import index



app_name = 'web'


urlpatterns = [
    path('',index),
]