import sqlite3
from dataclasses import dataclass


class SQLite:
    """Context manager database."""
    def __init__(self, file='application.db'):
        self.file = file
    def __enter__(self):
        self.conn = sqlite3.connect(self.file)
        return self.conn.cursor()
    def __exit__(self, type, value, traceback):
        self.conn.close()


class NotFoundError(Exception):
    
    def __init__(self, message) -> None:
        self.message = message
        super().__init__()


@dataclass
class DB:
    path: str = 'application.db'

    def start_connection(self):
        """Start the connection with database."""
        self.con = sqlite3.connect(self.path)
        
    def create_cursor(self):
        """Create the cursor for execute operations."""
        self.cur = self.con.cursor()

    def execute(self, command: str, itens: list=None):
        """Execute operations into the database."""
        self.start_connection()
        self.create_cursor()
        self.cur.execute(command, itens)

    def fetchall(self):
        """Retrive all data from a request."""
        data = self.cur.fetchall()
        if data is not None:
            return data
        else:
            raise NotFoundError(message="Unable to find blogs.")

    def fetchone(self):
        """Retrive one data from a request."""
        data = self.cur.fetchone()
        if data is not None:
            return data
        else:
            raise NotFoundError(message="Unable to find blog.")


    def close_connection(self):
        """Close the connection with the database."""
        self.con.close()