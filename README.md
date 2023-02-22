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
    │   │
    │   ├───static
    │   │   ├───assets
    │   │   │   ├───icon
    │   │   │   │
    │   │   │   └───images
    │   │   │
    │   │   ├───css
    │   │   │       bootstrap.min.css
    │   │   │       dashboard.css
    │   │   │       homepage.css
    │   │   │       login.css
    │   │   │       management.css
    │   │   │       management.rtl.css
    │   │   │       mission.css
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
    │   │       mission.html
    │   │       register.html
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
- `netbalance/netbalanceApp/templates/*.html`
- `netbalance/netbalanceApp/urls.py`
- `netbalance/netbalanceApp/views.py`
- `netbalance/netbalanceProject/settings.py`
- `netbalance/netbalanceProject/urls.py`
