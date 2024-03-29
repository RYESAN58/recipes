from turtle import update
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.recipe import Recipe
from flask_app.models.user import User
from flask_bcrypt import Bcrypt



@app.route('/recipe/<int:num>')
def description(num):
    data = {
        'id': num
    }
    x = Recipe.get_by_id(data)
    return render_template('recipes.html', the_recipe = x, x= session['user_id'])

@app.route('/delete/<int:num>')
def delete(num):
    data = {'id': num}
    Recipe.delete(data)
    return redirect(f"/dashboard/{session['user_id']}")

@app.route('/creator/<int:num>')
def create_rec(num):
    return render_template('create.html', user = num, x= session['user_id'])

@app.route('/create' , methods =['POST'])
def add_rec():
    data= {
        'name': request.form['name'],

        'description': request.form['description'],

        'instructions': request.form['instructions'],

        'date': request.form['date'],
        
        'bool': request.form['bool'],
        
        'user_id': request.form['user_id']
    }
    if not Recipe.validate_rec(request.form):
        return redirect(f"/creator/{request.form['user_id']}")
    num1 = request.form['user_id']
    Recipe.add(data)
    return redirect(f'/creator/{num1}', x = session['user_id'])

@app.route('/update/<int:num>')
def update(num):
    data = {'id': num}
    edit = Recipe.get_by_id(data)
    return render_template('update.html', update = edit, x= session['user_id'])


@app.route('/update_rec', methods=['post'])
def new_rec():
    data = {
        'name': request.form['name'],

        'description': request.form['description'],

        'instructions': request.form['instructions'],

        'date': request.form['date'],
        
        'bool': request.form['bool'],

        'id': request.form['id']
    }
    if not Recipe.validate_rec(request.form):
        return redirect(f"/update/{request.form['id']}")
    user = request.form['id']
    Recipe.update(data)
    return redirect(f'/recipe/{user}', x= session['user_id'])
    