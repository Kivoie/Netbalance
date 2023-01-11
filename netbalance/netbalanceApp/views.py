from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from netbalanceApp.models import NewApplication

#other modules
from datetime import datetime



def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        username = request.POST['username']
        password = request.POST['password']
        if form.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return redirect('homepage')
                else:
                    return HttpResponse('Invalid login details supplied.')
            return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'register.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('login')


@login_required(login_url='login')
def management(request):

    if request.method == 'POST':
        #node_number = int(request.POST['node_number'])
        
        location = str(request.POST['location'])
    
        ip_address = str(request.POST['ip']).strip()
        
        timestamp = datetime.now()
        timestamp = str(timestamp.strftime("%Y/%m/%d %H:%M:%S")).strip()
        
        description = str(request.POST['description'])
        
        
        
        new_node = NewApplication(location=location, ip=ip_address, date=timestamp, description=description)
        
        new_node.save()
        
        print(new_node.location, new_node.ip, new_node.date, new_node.description)
        
        return redirect('management')
        
    elif request.method == 'GET':
        
        raw_list = NewApplication.objects.all().values()
            
        return render(request, 'management.html', {'sql_table': raw_list})


@login_required(login_url='login')
def homepage(request):
    if request.user.is_authenticated:
        print('user is authenticated')
    return render(request, 'homepage.html')
