import sqlite3
from abc import ABC, abstractmethod
from . import DB_FILE


class DatabaseConnect:

    def __init__(self):
        self.connection = sqlite3.connect(DB_FILE)
        self.cursor = self.connection.cursor()

    def close_connection(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()

    def __del__(self):
        self.close_connection()


class Query(ABC):

    def __init__(self):
        try:
            self.db = DatabaseConnect()
        except sqlite3.Error as e:
            print(f"[TASK:MANAGER] '{e}'")

    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def update_data(self):
        pass

    @abstractmethod
    def insert_data(self):
        pass

    @abstractmethod
    def delete_data(self):
        pass