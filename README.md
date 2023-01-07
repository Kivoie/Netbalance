# Netbalance
Capstone 2022: Data Center Network Monitoring and Web App Service Provisioning Automation with Auto Scaling


## File Structure
```
root@odroid:/home/ubuntu# tree
`-- netbalance
    |-- dashboard
    |   |-- __init__.py
    |   |-- admin.py
    |   |-- apps.py
    |   |-- migrations
    |   |-- models.py
    |   |-- templates
    |   |   |-- base.html
    |   |   |-- dashboard.html
    |   |   `-- system_settings.html
    |   |-- tests.py
    |   |-- urls.py
    |   `-- views.py
    |-- db.sqlite3
    |-- manage.py
    `-- netbalance
        |-- __init__.py
        |-- asgi.py
        |-- settings.py
        |-- urls.py
        `-- wsgi.py
```

## Files of Importance
- `netbalance/dashboard/templates/*.html`
- `netbalance/dashboard/urls.py`
- `netbalance/dashboard/views.py`
- `netbalance/netbalance/settings.py`
- `netbalance/netbalance/urls.py`
