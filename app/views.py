from flask import Flask
from flask import render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
from app import app
from app import db 
from app.models import UserProfile 
from models import UserProfile
import datetime
from forms import ProfileForm 

@app.route("/")
def newprofile():
    return render_template('profile.html')
    
@app.route("/profile", methods=['GET', 'POST'])
def addprofile():
    form = ProfileForm()
    filefolder = app.config["UPLOAD_FOLDER"]

    file = request.files['picture']
    filename = secure_filename(file.filename)
    file.save(os.path.join(filefolder, filename))
    flash('File uploaded')
    
    img = "./static/uploads/" + filename
    date = str(datetime.date.today())
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
    
    
    return render_template(url_for('profiles'))
    
@app.route("/profiles")
def profiles():
    users = db.session.query(UserProfile).all()
    return render_template('profiles.html',users=users)
    
@app.route("/profile/<userid>")
def profile(userid):
    users = db.session.query(UserProfile).all()
    for UserProfile in users:
        if userid == UserProfile.getid():
            img = UserProfile.img
            date = UserProfile.date
            username = UserProfile.username
            firstname = UserProfile.firstname
            lastname = UserProfile.lastname
            gender = UserProfile.gender
            age = UserProfile.age
            bio = UserProfile.bio
            password = UserProfile.password
    
    
            return render_template("profileuser.html", firstname=firstname, lastname=lastname, username=username, password=password, age=age, bio=bio, img=img, date=date, gender=gender)
    
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")