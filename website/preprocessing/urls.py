from django.urls import path
from . import views

urlpatterns = [
    path('home-dp/',views.dp_home_view,name='dp_home')

]
