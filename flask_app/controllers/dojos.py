from flask import Flask, render_template, redirect, session, request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def addDojos():
    dojos=Dojo.get_all()
    return render_template('index.html', dojos=dojos)

@app.route('/dojos/process', methods=['POST'])
def processDojo():
    data = {
        'name' : request.form['name']
    }
    Dojo.save(data)
    print('process done:', data)
    return redirect ('/')


@app.route('/dojos/<int:id>')
def getOneDojo(id):
    data = {
        'id' : id
    }
    dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template ('viewdojo.html', dojo=dojo)


