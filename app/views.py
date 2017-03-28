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
from flask import jsonify

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
    
@app.route("/profiles", methods=['GET', 'POST'])
def profiles():
    
    if request.headers.get('Content-Type') == "application/json" or request.method == 'POST':
        users1 = db.session.query(UserProfile)
        users = []
        l =[]
        for user in users1:
            id = user.id
            username = user.username
            l = (username, id)
            users.append(l)
        return jsonify(users)
    else:
        users = db.session.query(UserProfile).all()
        return render_template('profiles.html',users=users)
    
@app.route("/profile/<userid>", methods=['GET', 'POST'])
def profile(userid):
    if request.headers.get('Content-Type') == "application/json" or request.method == 'POST':
        user = db.session.query(UserProfile).filter_by(id=userid).one()
        id = user.id
        img = user.img
        img = str(img)
        l = list(img)
        del(l[0])
        img = "".join(l)
        
        date = user.date
        username = user.username
        gender = user.gender
        age = user.age
        user1 = [id,username,img,gender,age,date]
        
        return jsonify(user1)
    else:
        user = db.session.query(UserProfile).filter_by(id=userid).one()
        id = user.id
        img = user.img
        img = str(img)
        l = list(img)
        del(l[0])
        img = "".join(l)
        date = user.date
        username = user.username
        firstname = user.first_name
        lastname = user.last_name
        gender = user.gender
        age = user.age
        bio = user.bio
        password = user.password
        return render_template("profileuser.html",id=id, firstname=firstname, lastname=lastname, username=username, password=password, age=age, bio=bio, img=img, date=date, gender=gender)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")