# Netbalance
Capstone 2022: Data Center Network Monitoring and Web App Service Provisioning Automation with Auto Scaling


## File Structure
```
PS C:\Users\AlexT\Desktop\Projects\Netbalance> tree /F 


└───netbalance
    │   db.sqlite3
    │   manage.py
    │
    ├───netbalanceApp
    │   │   admin.py
    │   │   apps.py
    │   │   forms.py
    │   │   models.py
    │   │   test.json
    │   │   tests.py
    │   │   urls.py
    │   │   views.py
    │   │   __init__.py
    │   │
    │   ├───migrations
    │   │   │   0001_initial.py
    │   │   │   __init__.py
    │   │   │
    │   │   └───__pycache__
    │   │           0001_initial.cpython-311.pyc
    │   │           __init__.cpython-311.pyc    
    │   │
    │   ├───static
    │   │   ├───assets
    │   │   │   ├───icon
    │   │   │   │       netbalance-48x48(1).ico 
    │   │   │   │       netbalance-48x48.ico
    │   │   │   │
    │   │   │   └───images
    │   │   │           grafana-200x200.png
    │   │   │           netbalance-16x16.png
    │   │   │           netbalance-180x180.png
    │   │   │           netbalance-32x32.png
    │   │   │           netbalance-512x512.png
    │   │   │           netbalance-full1.png
    │   │   │           netbalance-full2.png
    │   │   │           netbalance-full3.png
    │   │   │           netbalance-name.png
    │   │   │           netbalance192x192.png
    │   │   │
    │   │   ├───css
    │   │   │       bootstrap.min.css
    │   │   │       dashboard.css
    │   │   │       homepage.css
    │   │   │       login.css
    │   │   │       management.css
    │   │   │       management.rtl.css
    │   │   │       register.css
    │   │   │
    │   │   └───javascript
    │   │           bootstrap.bundle.min.js
    │   │           bootstrap.bundle.min.js.map
    │   │           homepage.js
    │   │           login.js
    │   │           management.js
    │   │           register.js
    │   │
    │   ├───templates
    │   │       homepage.html
    │   │       login.html
    │   │       management.html
    │   │       register.html
    │   │
    │   └───__pycache__
    │           admin.cpython-311.pyc
    │           apps.cpython-311.pyc
    │           grafana_script.cpython-311.pyc
    │           models.cpython-311.pyc
    │           urls.cpython-311.pyc
    │           views.cpython-311.pyc
    │           __init__.cpython-311.pyc
    │
    └───netbalanceProject
        │   asgi.py
        │   settings.py
        │   urls.py
        │   wsgi.py
        │   __init__.py
        │
        └───__pycache__
                settings.cpython-311.pyc
                urls.cpython-311.pyc
                wsgi.cpython-311.pyc
                __init__.cpython-311.pyc
```

## Files of Importance
- `netbalance/netbalanceApp/templates/*.html`
- `netbalance/netbalanceApp/urls.py`
- `netbalance/netbalanceApp/views.py`
- `netbalance/netbalanceProject/settings.py`
- `netbalance/netbalanceProject/urls.py`
