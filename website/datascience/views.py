from django.shortcuts import render, redirect
from django.http import HttpResponse
import matplotlib.pyplot as plt
import seaborn as sns
from .models import UploadedFile
from .seaborn import plot_dataset, determine_variable_type
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
# Create your views here.
def ds_home_view(request):
    return render(request,'ds_home.html')

def ds_seaborn_view(request):
    
    return render(request,'seaborn.html')

def ds_stats_view(request):
    return render(request,'stats.html')

def ds_numpy_view(request):
    return render(request,'numpy1.html')


def barplot_view(request):
    # Retrieve the latest uploaded file for the user
    try:
        latest_file = UploadedFile.objects.filter(user=request.user).latest('uploaded_at')
    except UploadedFile.DoesNotExist:
        return HttpResponse("No files uploaded by the user.", content_type="text/plain")

    # Get the file path
    file_path = latest_file.file.path
    
    # Read the CSV into a pandas DataFrame
    try:
        df = pd.read_csv(file_path, index_col=False, na_values=['?', 'missing', '', 'NULL', 'N/A'])
    except Exception as e:
        return HttpResponse(f"Error reading CSV file: {e}", content_type="text/plain")
    plot_type = 'barplot'
    plot_dataset(df, plot_type=plot_type)
    return render(request,'seaborn.html')
   


def histplot_view(request):
    try:
        latest_file = UploadedFile.objects.filter(user=request.user).latest('uploaded_at')
    except UploadedFile.DoesNotExist:
        return HttpResponse("No files uploaded by the user.", content_type="text/plain")

    # Get the file path
    file_path = latest_file.file.path
    
    # Read the CSV into a pandas DataFrame
    try:
        df = pd.read_csv(file_path, index_col=False, na_values=['?', 'missing', '', 'NULL', 'N/A'])
    except Exception as e:
        return HttpResponse(f"Error reading CSV file: {e}", content_type="text/plain")
    plot_type = 'histplot'
    plot_dataset(df, plot_type=plot_type)
    return render(request,'seaborn.html')


def catplot_view(request):
    try:
        latest_file = UploadedFile.objects.filter(user=request.user).latest('uploaded_at')
    except UploadedFile.DoesNotExist:
        return HttpResponse("No files uploaded by the user.", content_type="text/plain")

    # Get the file path
    file_path = latest_file.file.path
    
    # Read the CSV into a pandas DataFrame
    try:
        df = pd.read_csv(file_path, index_col=False, na_values=['?', 'missing', '', 'NULL', 'N/A'])
    except Exception as e:
        return HttpResponse(f"Error reading CSV file: {e}", content_type="text/plain")
    plot_type = 'catplot'
    plot_dataset(df, plot_type=plot_type)
    return render(request,'seaborn.html')

def pairplot_view(request):
    try:
        latest_file = UploadedFile.objects.filter(user=request.user).latest('uploaded_at')
    except UploadedFile.DoesNotExist:
        return HttpResponse("No files uploaded by the user.", content_type="text/plain")

    # Get the file path
    file_path = latest_file.file.path
    
    # Read the CSV into a pandas DataFrame
    try:
        df = pd.read_csv(file_path, index_col=False, na_values=['?', 'missing', '', 'NULL', 'N/A'])
    except Exception as e:
        return HttpResponse(f"Error reading CSV file: {e}", content_type="text/plain")
    plot_type = 'pairplot'
    plot_dataset(df, plot_type=plot_type)
    return render(request,'seaborn.html')

def boxplot_view(request):
    try:
        latest_file = UploadedFile.objects.filter(user=request.user).latest('uploaded_at')
    except UploadedFile.DoesNotExist:
        return HttpResponse("No files uploaded by the user.", content_type="text/plain")

    # Get the file path
    file_path = latest_file.file.path
    
    # Read the CSV into a pandas DataFrame
    try:
        df = pd.read_csv(file_path, index_col=False, na_values=['?', 'missing', '', 'NULL', 'N/A'])
    except Exception as e:
        return HttpResponse(f"Error reading CSV file: {e}", content_type="text/plain")
    plot_type = 'boxplot'
    plot_dataset(df, plot_type=plot_type)
    return render(request,'seaborn.html')

def lineplot_view(request):
    try:
        latest_file = UploadedFile.objects.filter(user=request.user).latest('uploaded_at')
    except UploadedFile.DoesNotExist:
        return HttpResponse("No files uploaded by the user.", content_type="text/plain")

    # Get the file path
    file_path = latest_file.file.path
    
    # Read the CSV into a pandas DataFrame
    try:
        df = pd.read_csv(file_path, index_col=False, na_values=['?', 'missing', '', 'NULL', 'N/A'])
    except Exception as e:
        return HttpResponse(f"Error reading CSV file: {e}", content_type="text/plain")
    plot_type = 'lineplot'
    plot_dataset(df, plot_type=plot_type)
    return render(request,'seaborn.html')

def scatterplot_view(request):
    try:
        latest_file = UploadedFile.objects.filter(user=request.user).latest('uploaded_at')
    except UploadedFile.DoesNotExist:
        return HttpResponse("No files uploaded by the user.", content_type="text/plain")

    # Get the file path
    file_path = latest_file.file.path
    
    # Read the CSV into a pandas DataFrame
    try:
        df = pd.read_csv(file_path, index_col=False, na_values=['?', 'missing', '', 'NULL', 'N/A'])
    except Exception as e:
        return HttpResponse(f"Error reading CSV file: {e}", content_type="text/plain")
    plot_type = 'scatterplot'
    plot_dataset(df, plot_type=plot_type)
    return render(request,'seaborn.html')

