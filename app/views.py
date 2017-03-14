from flask import Flask
from flask import render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
from app import app
from app import db 
from app.models import UserProfile 
from models import UserProfile
from datetime import datetime
    

    
@app.route("/profile", methods=['GET', 'POST'])
def addprofile():
    filefolder = app.config["UPLOAD_FOLDER"]

    file = request.files['picture']
    filename = secure_filename(file.filename)
    file.save(os.path.join(filefolder, filename))
    flash('File uploaded')
    
    img = "./static/uploads/" + filename
    date = datetime.date
    username = form.username.data
    firstname = form.firstname.data
    lastname = form.lastname.data
    gender = form.gender.data
    age = form.age.data
    bio = form.bio.data
    password = form.password.data
    
    user = UserProfile(first_name=firstname, last_name=lastname, username=username, password=password, age=age, bio=bio, img=img, date=date, gender=gender)
    db.session.add(user)
    db.session.commit()
    quit()
    return render_template("profiles.html", img=img)
    
@app.route("/profiles")
def profiles():
    return render_template("profile.html")
    
@app.route("/profile/<userid>")
def profile(userid):
    return "User {0}".format(userid)
    
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")