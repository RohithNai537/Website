from django.shortcuts import render,redirect
from datascience.models import UploadedFile

def home_view(request):
    return render(request,'index.html',{'user':request.user})

def create_dataset(request):
    UploadedFile.objects.create(user=request.user,file=request.FILES['dataset'])
    return redirect('/')