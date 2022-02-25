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
    return render_template('recipes.html', the_recipe = x)

@app.route('/delete/<int:num>')
def delete(num):
    data = {'id': num}
    Recipe.delete(data)
    return redirect('/login')
