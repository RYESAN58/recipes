from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)



@app.route('/')
def index():
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