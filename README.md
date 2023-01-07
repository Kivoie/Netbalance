# Netbalance
Capstone 2022: Data Center Network Monitoring and Web App Service Provisioning Automation with Auto Scaling


## File Structure
```
PS \netbalance> tree /f               

netbalance
|
│   db.sqlite3                                             
│   manage.py
│
├───netbalanceApp                                            
│   │   admin.py
│   │   apps.py                                                 
│   │   forms.py
│   │   models.py
│   │   tests.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   │                                    
│   ├───media                                                      
│   ├───migrations                                           
│   │
│   ├───static
│   │   ├───assets
│   │   │   ├───brand
│   │   │   │   │   bootstrap-logo-white.png
│   │   │   │   │   bootstrap-logo.png
│   │   │   │   │   favicon_io.zip
│   │   │   │   │   grafana_logo.png
│   │   │   │   │
│   │   │   │   └───favicon
│   │   │   │           android-chrome-192x192.png
│   │   │   │           android-chrome-512x512.png
│   │   │   │           apple-touch-icon.png
│   │   │   │           favicon-16x16.png
│   │   │   │           favicon-32x32.png
│   │   │   │           favicon.ico
│   │   │   │           site.webmanifest
│   │   │   │
│   │   │   └───dist
│   │   │       ├───css
│   │   │       │       bootstrap.min.css
│   │   │       │
│   │   │       └───js
│   │   │               bootstrap.bundle.min.js
│   │   │               bootstrap.bundle.min.js.map
│   │   │
│   │   ├───css
│   │   │       filepond.css
│   │   │       login.css
│   │   │       management.css
│   │   │       management.rtl.css
│   │   │       register.css
│   │   │
│   │   └───javascript
│   │           filepond.js
│   │           management.js
│   │           register.js
│   │
│   ├───templates
│   │       homepage.html
│   │       login.html
│   │       management.html
│   │       management_data.html
│   │       register.html
│   │       upload_file.html
│   │
│   └───__pycache__
│
└───netbalanceProject
    │   asgi.py
    │   settings.py
    │   urls.py
    │   wsgi.py
    │   __init__.py
    │
    └───__pycache__

```

## Files of Importance
- `netbalance/dashboard/templates/*.html`
- `netbalance/dashboard/urls.py`
- `netbalance/dashboard/views.py`
- `netbalance/netbalance/settings.py`
- `netbalance/netbalance/urls.py`
