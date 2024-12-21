import logging

import mysql.connector


class DatabaseConnection:
    def __init__(self, host="localhost", user="root", password="3Randi722///", database="school"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print('Connected to database here')
            logging.info('Connected to database')
            return connection
        except mysql.connector.Error as e:
            logging.error(f'Error: {e}')
            raise
