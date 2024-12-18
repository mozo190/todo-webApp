import sqlite3


class DatabaseConnection:
    def __init__(self, database_file='database.db'):
        self.database_file = database_file
        
    def connect(self):
        return sqlite3.connect(self.database_file)
