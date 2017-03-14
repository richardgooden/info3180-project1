from flask import Flask
from flask import render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
from app import app
img="./static/uploads/temp.png"



@app.route("/addfile", methods=['POST', 'GET'])
def addfile():
    filefolder = app.config["UPLOAD_FOLDER"]

    file = request.files['picture']
    filename = secure_filename(file.filename)
    file.save(os.path.join(filefolder, filename))
    flash('File uploaded')
    img = "./static/uploads/" + filename
    return render_template("profile.html", img=img)
    
@app.route('/')
def home():
    return render_template("base.html")
    
@app.route("/profile")
def addprofile():
    
    return render_template("profile.html", img=img)
    
@app.route("/profiles")
def profiles():
    return render_template("profile.html")
    
@app.route("/profile/<userid>")
def profile(userid):
    return "User {0}".format(userid)
    
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")