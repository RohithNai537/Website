from django.shortcuts import render

# Create your views here.

def dp_home_view(request):
    return render(request,'dp_home.html')