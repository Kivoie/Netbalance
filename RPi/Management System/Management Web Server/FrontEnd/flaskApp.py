"""
Select the environment to run the application in
& '.\RPi\Management System\Management Web Server\env\Scripts\Activate.ps1'


if "File C:\Python\flask\env\Scripts\Activate.ps1 cannot be loaded because running scripts..."
powershell (Admin) - > "Set-ExecutionPolicy RemoteSigned"

Execute the application
py '.\RPi\Management System\Management Web Server\FrontEnd\flaskApp.py'
"""

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify


# __name__ is the name of the current python module template folder is the folder where the html files are stored
app = Flask(__name__, template_folder='templates')


@app.route('/')  # the route decorator binds the function to a url
def index():        # function is given a unique URL using the route() decorator
    return render_template('index.html')


if __name__ == "__main__":  # if this file is run directly, run the application
    app.run(debug=True)
