from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')
    

def register_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            # Create the user
            user = User.objects.create_user(username=name, email=email, password=password, first_name=name)
            # You may want to do additional processing here, such as sending a confirmation email
            # After registration, you can optionally log the user in
            login(request, user)
            # Redirect to a success page.
            return redirect('/')
        else:
            # Return an error message if passwords do not match
            return render(request, 'register.html', {'error_message': 'Passwords do not match.'})
    else:
        return render(request, 'register.html')
    
def logout_view(request):
    logout(request)
    return redirect('/')