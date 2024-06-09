from django.urls import path
from . import views

urlpatterns = [
    path('home-ml/',views.ml_home_view,name='ml_home')

]
