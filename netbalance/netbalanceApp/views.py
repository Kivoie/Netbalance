from codecs import register_error
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from netbalanceApp.models import NewApplication
from django.core.files.storage import FileSystemStorage
import subprocess
import json
import requests

#other modules
from datetime import datetime


#view for handling login requests
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        username = request.POST['username']     #this is the user's username
        password = request.POST['password']     #this is the user's password IN PLAINTEXT
        if form.is_valid():                     #perform basic form validation
            #authenticate the user by checking for username and matching hashed password with the one already in the database, if any
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)       #login the user and submit a cookie to the user's web browser
                    return redirect('homepage')     #redirect to the homepage
                else:
                    return HttpResponse('Invalid login details supplied.')      #the user provided invalid login details, redirect back to the same login page with an error message as feedback
            return redirect('homepage')
    else:
        form = AuthenticationForm()     #load the authentication form when the user submits a GET request to the web server
    return render(request, 'login.html', {'form': form})

#view to handle user registrations
def register(request):
    form = UserCreationForm()           #load the user create form
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()                 #save the form data to the database
            return redirect('login')
    return render(request, 'register.html', {'form': form})


#view to handle the mission page
@login_required(login_url='login') # require the user to be logged in to access this view
def mission(request):
    return render(request, 'mission.html')


#dashboard v2 view
@login_required(login_url='login') 
def dashboardv2(request):
    if 'add' in request.POST:
        location = str(request.POST.get('location'))
        ip_address = str(request.POST.get('ip')).strip()
        timestamp = datetime.now()
        timestamp = str(timestamp.strftime("%Y/%m/%d %H:%M:%S")).strip()
        description = str(request.POST.get('description'))
        
        #instantiate an object based on the NewApplication model with the user's given parameters and the computer-generated timestamp.
        new_node = NewApplication(location=location, ip=ip_address, date=timestamp, pending_add='True', pending_delete='False', description=description)
        new_node.save()
        
        print(new_node.location, new_node.ip, new_node.date, new_node.pending_add, new_node.pending_delete, new_node.description)  #debugging
        
        return redirect('dashboardv2')
        
    elif 'remove' in request.POST:
        node_id = int(request.POST.get('node_id'))  #gets user input from the frontend. This can be tricky to form a REGEX pattern from scratch, so it only supports a SINGLE number for now. I will look into this later. hint: use the 're' module in Python. -Danny
        
        '''
        if node_id >= 1:
            #delete the specified entry or entries from the database
            NewApplication.objects.filter(id=node_id).delete()
        '''
        
        table = NewApplication.objects.all()
        
        counter = 1     #this starts at the first value in the database
        for entry in table:
            if node_id == counter:
                entry.pending_add='False'
                entry.pending_delete='True'
                entry.save()
                del counter     #delete the counter so it cannot be re-used again until re-declared
                break       #we break because we are only modifying a single entry for now
            counter += 1
    
        return redirect('dashboardv2')
    
    
    elif 'commit' in request.POST:
        NewApplication.objects.filter(pending_add=1).update(pending_add=0)
        if NewApplication.objects.filter(pending_delete=1):
            NewApplication.objects.filter(pending_delete=1).delete() 
            '''
            table = NewApplication.objects.all()

            counter = 1     #start with the first entry in the database
            for entry in table:
                if entry.pending_delete == 1:
                    entry.delete()
                    del counter
                    break   #this line should be removed if trying to delete multiple entries in a single form submission (plus some other code)
                counter += 1
            '''
        return redirect('dashboardv2')
        
    elif request.method == 'GET':
        raw_list = NewApplication.objects.all().values()
        return render(request, 'dashboardv2.html', {'sql_table': raw_list})

    #If the user uploads files to the server through the webpage
    elif request.method == 'POST' and request.FILES['myfile']:
        uploaded_file = request.FILES['myfile'] #get the file from the request
        fs = FileSystemStorage() #instantiate a file system storage object
        fs.save(uploaded_file.name, uploaded_file) #save the file to the server
        return redirect('dashboardv2')



@login_required(login_url='login') # require the user to be logged in to access this view
def logout(request):
    auth_logout(request)
    return redirect('login')


@login_required(login_url='login')
def management(request):
    
    #API call to get the dashboard of the grafana server, using api key "yJrIjoiZmdsNEQ3SnozaHcxNXFIM1RzRDRCUWVuMGtLNGtrRXkiLCJuIjoiYXBpX2tleSIsImlkIjoxfQ=="
    if 'grafana-post' in request.POST:
        subprocess.call(['curl', '-X', 'POST', '-H', 'Content-Type: application/json', '-d', '{"name":"api_key","role":"Viewer","secondsToLive":3600}', 'http://localhost:3000/api/auth/keys'])

    if 'add' in request.POST:
        #location = str(request.POST['location'])            #old method
        location = str(request.POST.get('location'))    #new method
    
        #get the user's input (IP address)
        ip_address = str(request.POST.get('ip')).strip()
        
        #determine the current time stamp (current time zone)
        timestamp = datetime.now()
        timestamp = str(timestamp.strftime("%Y/%m/%d %H:%M:%S")).strip()
        
        #get the user's input (description)
        description = str(request.POST.get('description'))
        
        #instantiate an object based on the NewApplication model with the user's given parameters and the computer-generated timestamp.
        new_node = NewApplication(location=location, ip=ip_address, date=timestamp, pending_add='True', pending_delete='False', description=description)
        
        #INSERT a new entry into the database
        new_node.save()
        
        print(new_node.location, new_node.ip, new_node.date, new_node.pending_add, new_node.pending_delete, new_node.description)  #debugging
        
        # GRAFANA DASHBOARD CODE
            # Insert grafana dashboard here
            
            # url = 'http://10.43.3.50:8000/api/dashboards/db'
            # headers = {"Accept": "application/json", 'Content-Type': 'application/json', 'Authorization': 'Bearer <api_key>'}


            # open test.json file
            # with open('netbalanceApp/test.json') as f:    
            #    dashboard = json.load(f)

            # Send the request
            # response = requests.post(url, headers=headers, data=json.dumps(dashboard))

            # Check the response
            # if response.status_code == 200:
            #    print('Dashboard created successfully!')
            # else:
            #    print(f'Error creating dashboard: {response.text}')
        

        return redirect('management')
        
    #POST request to remove an entry
    elif 'remove' in request.POST:
    
        #server-side form validation to ensure that the values are within range
        node_id = int(request.POST.get('node_id'))  #gets user input from the frontend. This can be tricky to form a REGEX pattern from scratch, so it only supports a SINGLE number for now. I will look into this later. hint: use the 're' module in Python. -Danny
        
        #"If the user input is >=1 AND <= to the total number of nodes then mark the node for deletion"
        
        '''
        if node_id >= 1:
            #delete the specified entry or entries from the database
            NewApplication.objects.filter(id=node_id).delete()
        '''
        
        table = NewApplication.objects.all()
        
        counter = 1     #this starts at the first value in the database
        for entry in table:
            if node_id == counter:
                entry.pending_add='False'
                entry.pending_delete='True'
                entry.save()
                del counter     #delete the counter so it cannot be re-used again until re-declared
                break       #we break because we are only modifying a single entry for now
            counter += 1
    
        return redirect('management')
    
    #POST request to commit all changes (add or remove)
    elif 'commit' in request.POST:
        
        ### HAND OVER THE PARAMETERS TO ANSIBLE BELOW THIS LINE
        
        #There are two methods I think we can achieve this:
        #  1) Run Ansible sequentially: Ansible will start running here and the web server will not handle any requests until the Ansible script is fully complete and exited, then the management page will load. This would be a great place to implement a loading circle or icon to indicate that the web server is buffering.
        #  2) Run Ansible in parallel with this: The benefit of this is that the web page will load immediately after clicking 'commit' but the page will need to be manually refreshed periodically for the user to verify the nodes have been installed correctly. Personally I'm a fan of this method. Open to any suggestions. 
        # -Danny
        
        ### ANSIBLE ABOVE THIS LINE
        
        #updates all entries with the 'pending_add' field set to 1 with a 0
        NewApplication.objects.filter(pending_add=1).update(pending_add=0)
        
        if NewApplication.objects.filter(pending_delete=1):
            #NewApplication.objects.filter(requires_provision=1).update(requires_provision=0)
            
            NewApplication.objects.filter(pending_delete=1).delete() 


            '''
            table = NewApplication.objects.all()

            counter = 1     #start with the first entry in the database
            for entry in table:
                if entry.pending_delete == 1:
                    entry.delete()
                    del counter
                    break   #this line should be removed if trying to delete multiple entries in a single form submission (plus some other code)
                counter += 1
            '''
        return redirect('management')
        
    #GET request when the user is redirected here or refreshes the page
    elif request.method == 'GET':
        
        raw_list = NewApplication.objects.all().values()
            
        return render(request, 'management.html', {'sql_table': raw_list})

    #If the user uploads files to the server through the webpage
    elif request.method == 'POST' and request.FILES['myfile']:
        uploaded_file = request.FILES['myfile'] #get the file from the request
        fs = FileSystemStorage() #instantiate a file system storage object
        fs.save(uploaded_file.name, uploaded_file) #save the file to the server
        return render(request, 'management.html')

def reindex(table_object):
    counter = 1
    for entry in table_object:
        entry.id = counter
        entry.save()
        counter +=1


@login_required(login_url='login')
def homepage(request):
    if request.user.is_authenticated:
        print('user is authenticated')
    return render(request, 'homepage.html')
