from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

from flask_app.models.user import EMAIL_REGEX
class Recipe:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.description = db_data['description']
        self.instructions = db_data['instructions']
        self.date = db_data['date']
        self.name = db_data['name']
        self.bool = db_data['bool']
        self.user_id = db_data['user_id']

    @classmethod
    def get_by_id(cls,data):
        query = 'select * from recipes where id = %(id)s'
        print(query)
        return connectToMySQL("cookbook").query_db(query,data)

    @classmethod
    def delete(cls,data):
        query  = 'DELETE FROM `cookbook`.`recipes` WHERE (`id`=%(id)s);'
        return connectToMySQL("cookbook").query_db(query,data)

    @classmethod
    def add(cls,data):
        query = "INSERT INTO `cookbook`.`recipes` (`description`, `instructions`, `date`, `user_id`, `name`, `bool`) VALUES (%(description)s, %(instructions)s, %(date)s, %(user_id)s, %(name)s, %(bool)s);"
        print(query)
        return connectToMySQL('cookbook').query_db(query, data)

    @staticmethod
    def validate_rec(user):
        is_valid = True
        if len(user['description']) < 3:
            flash("description must be at least 3 characters.")
            is_valid = False
        if len(user['instructions']) < 3:
            flash("instructions must be at least 3 characters.")
            is_valid = False
        if len(user['name']) < 3:
            flash("name must be 3 characters")
            is_valid = False
        if len(user['date']) < 1:
            flash("please enter date")
            is_valid = False
        return is_valid

    @classmethod
    def get_all_from_user(cls, data):
        query = 'SELECT * FROM recipes WHERE user_id = %(id)s'
        return connectToMySQL('cookbook').query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE `cookbook`.`recipes` SET `description` = %(description)s, `instructions` = %(instructionss)s, `date` = %(date)s, `name` = %(name)s, `bool` = %(bool)s WHERE (`id` = %(id)s);"
        return connectToMySQL('cookbook').query_db(query, data)