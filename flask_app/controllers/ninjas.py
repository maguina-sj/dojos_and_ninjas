from flask import Flask, render_template, redirect, session, request
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def addNinja():

    dojos=Dojo.get_all()
    return render_template('addninja.html', dojos=dojos)


@app.route('/ninjas/process', methods=['POST'])
def processNinja():
    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'age':request.form['age'],
        'dojos_id':request.form['dojos_id']
    }
    Ninja.save(data)
    
    return redirect ('/ninjas')



