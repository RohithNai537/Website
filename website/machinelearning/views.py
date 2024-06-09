from django.shortcuts import render

# Create your views here.
def ml_home_view(request):
    return render(request,'ml_home.html')
