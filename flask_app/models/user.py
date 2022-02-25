from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.firstname = db_data['firstname']
        self.lastname = db_data['lastname']
        self.password = db_data['password']

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO `cookbook`.`user` (`firstname`, `lastname`, `password`, `email`) VALUES (%(firstname)s, %(lastname)s, %(password)s, %(email)s);"
        return connectToMySQL("cookbook").query_db(query,data)

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['firstname']) < 3:
            flash("Name must be at least 3 characters.", 'register')
            is_valid = False
        if len(user['lastname']) < 3:
            flash("lastname must be at least 3 characters.", 'register')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Please enter a valid Email", 'register')
            is_valid = False
        if len(user['password']) < 8:
            flash("password must be 8 characters", 'register')
            is_valid = False
        return is_valid

    @classmethod
    def verify_email(cls,data):
        is_valid = True
        query = 'SELECT * FROM user WHERE email = %(email)s;'
        result = connectToMySQL("cookbook").query_db(query,data)
        if len(result)  != 0:
            flash('This Email is already Taken', 'register')
            is_valid = False
        return is_valid
    
    
    @classmethod
    def login_email(cls,data):
        query = "SELECT * FROM user WHERE email = %(email)s;"
        result = connectToMySQL("cookbook").query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])