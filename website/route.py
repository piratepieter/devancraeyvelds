from website import app
from flask import render_template, request, send_from_directory

@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/')
def hello():

    return render_template("page-petante.html") 

@app.route('/pieter')
def pieter():

    return render_template("page-pieter.html") 
    
@app.route('/julia')
def julia():

    return render_template("page-julia.html") 

@app.route('/saar')
def saar():

    return render_template("page-saar.html") 
    
@app.route('/michiel')
def michiel():

    return render_template("page-michiel.html")  

@app.route('/frank')
def frank():

    return render_template("page-frank.html")     