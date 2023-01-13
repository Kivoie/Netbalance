# Netbalance
Capstone 2022: Data Center Network Monitoring and Web App Service Provisioning Automation with Auto Scaling


## File Structure
```
root@VanillaPC:/mnt/c/Users/danny/Downloads# tree netbalance
netbalance
├── db.sqlite3
├── manage.py
├── netbalanceApp
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── models.py
│   ├── static
│   │   ├── assets
│   │   │   ├── brand
│   │   │   │   ├── bootstrap-logo-white.png
│   │   │   │   ├── bootstrap-logo.png
│   │   │   │   ├── favicon
│   │   │   │   │   ├── android-chrome-192x192.png
│   │   │   │   │   ├── android-chrome-512x512.png
│   │   │   │   │   ├── apple-touch-icon.png
│   │   │   │   │   ├── favicon-16x16.png
│   │   │   │   │   ├── favicon-32x32.png
│   │   │   │   │   ├── favicon.ico
│   │   │   │   │   └── site.webmanifest
│   │   │   │   ├── favicon_io.zip
│   │   │   │   └── grafana_logo.png
│   │   │   └── dist
│   │   │       ├── css
│   │   │       │   └── bootstrap.min.css
│   │   │       └── js
│   │   │           ├── bootstrap.bundle.min.js
│   │   │           └── bootstrap.bundle.min.js.map
│   │   ├── css
│   │   │   ├── login.css
│   │   │   ├── management.css
│   │   │   ├── management.rtl.css
│   │   │   └── register.css
│   │   └── javascript
│   │       ├── management.js
│   │       └── register.js
│   ├── templates
│   │   ├── homepage.html
│   │   ├── login.html
│   │   ├── management.html
│   │   └── register.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── netbalanceProject
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

16 directories, 53 files
```

## Files of Importance
- `netbalance/netbalanceApp/templates/*.html`
- `netbalance/netbalanceApp/urls.py`
- `netbalance/netbalanceApp/views.py`
- `netbalance/netbalanceProject/settings.py`
- `netbalance/netbalanceProject/urls.py`
