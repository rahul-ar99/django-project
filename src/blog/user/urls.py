from django.urls import path
from user.views import login,logout, signup



app_name = 'user'


urlpatterns = [
    path('login',login, name="login"),
    path('logout',logout, name="logout"),
    path('signup',signup, name="signup"),
]