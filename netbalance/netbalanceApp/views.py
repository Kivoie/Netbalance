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
from django.db import connection
import subprocess
import os
from datetime import datetime


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

@login_required(login_url='login') # require the user to be logged in to access this view
def register(request):
    form = UserCreationForm()           #load the user create form
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()                 #save the form data to the database
            return redirect('login')
    return render(request, 'register.html', {'form': form})



@login_required(login_url='login') # require the user to be logged in to access this view
def mission(request):
    return render(request, 'mission.html')


@login_required(login_url='login') 
def dashboardv2(request):

    raw_images = subprocess.Popen('docker images', stdout=subprocess.PIPE, shell=True)
    output, _ = raw_images.communicate()

    # Convert the output to a string and count the lines
    docker_line_count = len(output.decode().splitlines())
    print(docker_line_count)

    if docker_line_count > 1:
        print('at least one image was found')
        docker_image_exists = True
    else:
        print('no images were found')
        docker_image_exists = True
        # subprocess.Popen(['docker', 'pull', 'nginx:latest', ';', 'kubectl', 'create', '-f',  '/root/manifests/deployment.yaml'])
    
    

    if 'image-pull' in request.POST:
        image = str(request.POST.get('docker_file'))
        print(image)
        with open('/root/manifests/deployment.yaml', 'w+') as f:
            f.write(f"""
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deploymentnetbalance
  namespace: default
spec:
  selector:
    matchLabels:
      app: netbalance
  template:
    metadata:
      labels:
        app: netbalance
    spec:
      containers:
      - name: netbalance
        image: {image}
        ports:
        - containerPort: 80
        resources:
          requests:
            cpu: "250m"
          limits:
            cpu: "500m"

---
apiVersion: v1
kind: Service
metadata:
  name: netbalanceservice
  labels:
    app: netbalance
spec:
  selector:
    app: netbalance
  type: NodePort
  ports:
    - protocol: TCP
      port: 80
      nodePort: 31050
      targetPort: 80
    """)
        subprocess.Popen(['ansible-playbook', '/root/Ansible/deploycluster.yml', '--inventory-file=/root/Ansible/hosts'])
        subprocess.Popen(['kubectl', 'create', '-f',  '/root/manifests/deployment.yaml'])

    elif 'reset' in request.POST:
        
        
        
        os.chdir('/home/ubuntu/Netbalance/netbalance/netbalanceApp')
        with open('../deployment/hosts_template', 'r') as f:
            contents = f.read()
        
            with open('../deployment/remove/hosts', 'w') as f:
                f.write(contents)
                f.close()
        f.close()
        
        new_entries = NewApplication.objects.all()
        for i in range(len(new_entries)):
            node_username = request.POST.get(f'node_username_{i+1}')
            node_password = request.POST.get(f'node_password_{i+1}')
            node_root_password = request.POST.get(f'node_root_password_{i+1}')            
            
            if node_username is not None and node_password is not None and node_root_password is not None:
                new_entry = NewApplication.objects.all()[i]
                ip_address = new_entry.ip
                
                with open("../deployment/reset/hosts", "r+") as f:
                    contents = f.read()

                    index = contents.index("[worker]\n") + len("[worker]\n")
                    contents = contents[:index] + f"{ip_address} ansible_connection=ssh ansible_ssh_user={node_username} ansible_ssh_pass={node_password} ansible_sudo_pass={node_root_password}\n" + contents[index:]

                    f.seek(0)
                    f.write(contents)
                    f.truncate()

        subprocess.Popen(['ansible-playbook', '/root/Ansible/resetcluster.yml', '--inventory-file=../deployment/reset/hosts'])
        
        #DELETES DATA ENTRIES
        NewApplication.objects.all().delete()
        
                    

        
    elif 'add' in request.POST:
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
        
    elif 'commit_pass' in request.POST:

        subprocess.Popen(['ansible-playbook', '/root/Ansible/nodejoin.yml', '--inventory-file=../deployment/add/hosts'])
        NewApplication.objects.filter(pending_add=1).update(pending_add=0)
        if NewApplication.objects.filter(pending_delete=1):
            # run the node delete playbook with the remove hosts file
            subprocess.Popen(['ansible-playbook', '/root/Ansible/nodedelete.yml', '--inventory-file=../deployment/del/hosts'])   
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

        os.chdir('/home/ubuntu/Netbalance/netbalance/netbalanceApp')
        with open('../deployment/hosts_template', 'r') as f:
            contents = f.read()
            

            with open('../deployment/add/hosts', 'w') as f:
                f.write(contents)
                f.close()
                
            with open('../deployment/del/hosts', 'w') as f:
                f.write(contents)
                f.close()
        f.close()
        
        new_entries = NewApplication.objects.all()

        for i in range(len(new_entries)):
            node_username = request.POST.get(f'node_username_{i+1}')
            node_password = request.POST.get(f'node_password_{i+1}')
            node_root_password = request.POST.get(f'node_root_password_{i+1}')
            
            # Opening sql database to find del/add node
            cursor = connection.cursor()
            # Check Add
            cursor.execute(f"SELECT pending_add FROM netbalanceApp_newapplication LIMIT 1 OFFSET {i}")
            add_status = cursor.fetchone()
            print(list(add_status))
            
            # Check Remove
            cursor.execute(f"SELECT pending_delete FROM netbalanceApp_newapplication LIMIT 1 OFFSET {i}")
            delete_status = cursor.fetchone()
            cursor.close()
            
            
            print(i, node_username, node_password, node_root_password)
            
            if node_username is not None and node_password is not None and node_root_password is not None:
                
                
                new_entry = NewApplication.objects.all()[i]
                ip_address = new_entry.ip
                
                if list(add_status)[0] is True:
                    with open("../deployment/add/hosts", "r+") as f:
                        contents = f.read()

                        index = contents.index("[worker]\n") + len("[worker]\n")
                        contents = contents[:index] + f"{ip_address} ansible_connection=ssh ansible_ssh_user={node_username} ansible_ssh_pass={node_password} ansible_sudo_pass={node_root_password}\n" + contents[index:]

                        f.seek(0)
                        f.write(contents)
                        f.truncate()
                    
                else:    
                    with open("../deployment/del/hosts", "r+") as f:
                        contents = f.read()

                        index = contents.index("[worker]\n") + len("[worker]\n")
                        contents = contents[:index] + f"{ip_address} ansible_connection=ssh ansible_ssh_user={node_username} ansible_ssh_pass={node_password} ansible_sudo_pass={node_root_password}\n" + contents[index:]

                        f.seek(0)
                        f.write(contents)
                        f.truncate()
         # run the node join playbook with the add hosts file
       
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
                if entry.pending_add == True:
                    entry.delete()
                else:
                    entry.pending_add='False'
                    entry.pending_delete='True'
                    entry.save()
                    del counter     #delete the counter so it cannot be re-used again until re-declared
                break       #we break because we are only modifying a single entry for now
            counter += 1
        
        return redirect('dashboardv2')
    
    elif 'commit' in request.POST:
       
        return redirect('dashboardv2')
        
    elif request.method == 'GET':           
        raw_list = NewApplication.objects.all().values()
        return render(request, 'dashboardv2.html', {'sql_table': raw_list, 'docker_image_exists': docker_image_exists})

    #If the user uploads files to the server through the webpage
    elif request.method == 'POST' and request.FILES['myfile']:
        uploaded_file = request.FILES['myfile']
        fs = FileSystemStorage()
        
        #Deletes all files in media
        dir_path = "netbalance/netbalanceApp/media"
        for filename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filename)
            os.remove(file_path)
            
        fs.save(uploaded_file.name, uploaded_file) 
        return redirect('dashboardv2')
    
    return render(request, 'dashboardv2.html', {'docker_image_exists': docker_image_exists})


def reindex(table_object):
    counter = 1
    for entry in table_object:
        entry.id = counter
        entry.save()
        counter +=1


@login_required(login_url='login') # require the user to be logged in to access this view
def logout(request):
    auth_logout(request)
    return redirect('login')


@login_required(login_url='login')
def homepage(request):
    if request.user.is_authenticated:
        print('user is authenticated')
    return render(request, 'homepage.html')
