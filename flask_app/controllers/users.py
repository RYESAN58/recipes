from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.recipe import Recipe
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    session['logged in'] = False
    session['user_id'] = ''
    return render_template('index.html')


@app.route('/create_user', methods=['POST'])
def creator():
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    if request.form['password'] != request.form['password2']:
        flash('Both Passwords must match!', 'register')
        return redirect('/')

    data={
        'firstname' : request.form['firstname'],
        'lastname' : request.form['lastname'],
        'email': request.form['email'],
        'password': pw_hash
    }
    if not User.validate_user(request.form):
        return redirect('/')
        #CHECKING TO SEE IF EMAIL IS TAKEN
    x = {'email': request.form['email']}
    valid = User.verify_email(x)
    if  not valid:
        return redirect('/')

    User.create_user(data)
    flash('Added in database', 'success')
    return redirect('/')

@app.route('/dashboard/<int:num1>')
def home(num1):
    id = {
        'id': num1
    }
    user_recipe =  Recipe.get_by_id(id)
    if session['logged_in'] == True:
        return render_template('dashboard.html', name = session['user_name'],  x= session['user_id'], array = user_recipe)
    else:
        flash
        return redirect('/')


@app.route('/login', methods=['POST'])
def login():
    #EMAIL TO BE CHECkED IN DATA BASE
    
    data = { "email" : request.form["email"] }
    user_in_db = User.login_email(data)
    if not user_in_db:
        flash("Invalid Email/Password", 'login')
        return redirect("/")
    
    #CHECKING TO SEE IF PASSWORD MATCHES THE ONE IN THE DATABASE
    
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password", 'login')
        return redirect('/')
    
    #CREATING SESSION INFO FOR USER'S LOGIN
    xray = user_in_db.id
    print(xray)
    session['user_id'] = user_in_db.id
    session['logged_in'] = True
    session['user_name'] = user_in_db.firstname
    if session['logged_in'] == True:
        return redirect(f"/dashboard/{xray}")