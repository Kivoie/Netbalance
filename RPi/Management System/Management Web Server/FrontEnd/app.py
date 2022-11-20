"""
Select the environment to run the application in
& '.\RPi\Management System\Management Web Server\env\Scripts\Activate.ps1'

if "File C:\Python\flask\env\Scripts\Activate.ps1 cannot be loaded because running scripts..."
powershell (Admin) - > "Set-ExecutionPolicy RemoteSigned"

Execute the application
py '.\RPi\Management System\Management Web Server\FrontEnd\flaskApp.py'
"""


from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# __name__ is the name of the current python module template folder is the folder where the html files are stored
app = Flask(__name__, template_folder='templates')

# MySQL configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///push_management.db'

# create a database object
db = SQLAlchemy(app)


class dbPOST(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)  # default value is the current time

    def __repr__(self):  # return a string representation of the object
        return '<POST %r> ' % self.id  # return the id of the post


db.create_all()


@app.route('/')  # The default page
def index():       # The function that runs when the default page is called
    return render_template('index.html')


if __name__ == "__main__":  # If the file is run directly and not imported
    app.run(debug=True)
