# Django modules
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django import forms

# Other modules
import subprocess
from time import sleep

# Custom classes
class settings_forms(forms.Form):
    button = forms.CharField()



########### Defined views
# View to display main dashboard web page
def template_dashboard(request):
    if request.method == 'GET':
        return render(request, 'dashboard.html', {'server_time': get_time(), 'health_1': get_health_icmp('10.43.3.10')})

# View to display system settings web page
@csrf_exempt
def template_settings(request):
    if request.method == 'GET':
        return render(request, 'system_settings.html', {'server_time': get_time(), 'server_disk': get_disk(), 'uptime': get_uptime()})

    elif request.method == 'POST':

        form = settings_forms(request.POST)
        if form.is_valid():
            if form.cleaned_data.get("button") == '1':
                subprocess.Popen('sleep 5 && sudo reboot', stdout=None, shell=True, close_fds=True)
                return render(request, 'system_settings.html', {'server_time': get_time(), 'server_disk': get_disk(), 'RST_FLAG': '1'})
        

########### Other functions (non-Views)
#custom function to generate timestamp whenever called (this is the server time, not the user's time)
def get_time():
    timestamp = subprocess.Popen('date "+%Y-%m-%d %H:%M:%S %Z"', stdout=subprocess.PIPE, shell=True, universal_newlines=True)
    return str(timestamp.communicate()[0])

#custom function to determine uptime of the device
def get_uptime():
    uptime = subprocess.Popen('uptime -p', stdout=subprocess.PIPE, shell=True, universal_newlines=True)  #shows the total uptime in a pretty format (-p)
    since = subprocess.Popen('uptime -s', stdout=subprocess.PIPE, shell=True, universal_newlines=True)   #shows the time since last reboot (-s)

    #a dict to store the values so that Django can pass the two strings as a single object rather than returning two separate objects
    statistics = {
            'uptime': str(uptime.communicate()[0]),
            'since': str(since.communicate()[0])
        }

    return statistics

#determine the Pi's total disk space and current usage
def get_disk():
    disk_free = subprocess.Popen('df -h | head -1 && df -h | grep "mmc" | grep -v "tmp"', stdout=subprocess.PIPE, shell=True, universal_newlines=True)
    return str(disk_free.communicate()[0])

#ping an IPv4 address only once with a timeout of 200ms
def get_health_icmp(address):
    bash_ping = subprocess.Popen('ping -c 1 -W 0.2 ' + str(address), stdout=subprocess.PIPE, shell=True, universal_newlines=True)
    return str(bash_ping.communicate()[0])
