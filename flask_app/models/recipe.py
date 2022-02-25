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

    @classmethod
    def get_by_id(cls,data):
        query = 'select * from recipes where id = %(id)s'
        print(query)
        return connectToMySQL("cookbook").query_db(query,data)

    @classmethod
    def delete(cls,data):
        query  = 'DELETE FROM `cookbook`.`recipes` WHERE (`id`=%(id)s);'
        return connectToMySQL("cookbook").query_db(query,data)