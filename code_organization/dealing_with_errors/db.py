import sqlite3
from dataclasses import dataclass


class NotFoundError(Exception):
    pass

class NotAuthorizedError(Exception):
    pass


@dataclass
class DB:
    path: str = 'code_organization/dealing_with_errors/application.db'

    def start_connection(self):
        self.con = sqlite3.connect(self.path)
        
    def create_cursor(self):
        self.cur = self.con.cursor()

    def execute(self, command: str):
        self.start_connection()
        self.create_cursor()
        self.cur.execute(command)
        
        return self.cur


    def close_connection(self):
        self.con.close()