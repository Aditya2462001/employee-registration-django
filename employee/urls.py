from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="Home"),
    path('register/',views.register,name="register"),
    path('edit/',views.edit,name="edit"),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
]