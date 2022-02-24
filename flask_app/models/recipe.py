from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

from flask_app.models.user import EMAIL_REGEX
class Recipe:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.description = db_data['description']
        self.instructions = db_data['instructions']
        self.date = db_data['date']

