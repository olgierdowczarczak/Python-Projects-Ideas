from sqlite3 import Error as sqlite3_error
from . import T_USERS, T_TASKS
from .models import Query


class User(Query):

    def create_table(self):
        try:
            self.db.cursor.execute(f"CREATE TABLE IF NOT EXISTS {T_USERS} (id INTEGER PRIMARY KEY AUTOINCREMENT, user_name VARCHAR(50) NOT NULL, user_surname VARCHAR(50) NOT NULL);")
            self.db.connection.commit()
        except sqlite3_error as e:
            print(f"[TASK:MANAGER] '{e}'")

    def get_data(self):
        try:
            self.db.cursor.execute(f"SELECT * FROM {T_USERS};")
            self.db.connection.commit()
            return self.db.cursor.fetchall()
        except sqlite3_error as e:
            print(f"[TASK:MANAGER] '{e}'")
            return None

    def get_user(self, index: int):
        try:
            self.db.cursor.execute(f"SELECT * FROM {T_USERS} WHERE id=?;", (index,))
            self.db.connection.commit()
            return self.db.cursor.fetchall()
        except sqlite3_error as e:
            print(f"[TASK:MANAGER] '{e}'")
            return None
        
    def update_data(self, data: tuple):
        try:
            data = data[1:] + (data[0],)
            self.db.cursor.execute(f"UPDATE {T_USERS} SET user_name=?, user_surname=? WHERE id=?;", (data))
            self.db.connection.commit()
        except sqlite3_error as e:
            print(f"[TASK:MANAGER] '{e}'")
        
    def insert_data(self, data: tuple):
        try:
            self.db.cursor.execute(f"INSERT INTO {T_USERS} VALUES (NULL, ?, ?);", (data))
            self.db.connection.commit()
        except sqlite3_error as e:
            print(f"[TASK:MANAGER] '{e}'")

    def delete_data(self, index: int):
        try:
            self.db.cursor.execute(f"DELETE FROM {T_USERS} WHERE id=?;", (index,))
            self.db.connection.commit()
        except sqlite3_error as e:
            print(f"[TASK:MANAGER] '{e}'")


class Task(Query):

    def create_table(self):
        try:
            self.db.cursor.execute(f"CREATE TABLE IF NOT EXISTS {T_TASKS} (id INTEGER PRIMARY KEY AUTOINCREMENT, task_name VARCHAR(50) NOT NULL, task_dsc VARCHAR(200), task_status INTEGER DEFAULT 0, id_user INTEGER, FOREIGN KEY (id_user) REFERENCES {T_USERS}(id));")
            self.db.connection.commit()
        except sqlite3_error as e:
            print(f"[TASK:MANAGER] '{e}'")
        
    def get_data(self, index: int):
        try:
            self.db.cursor.execute(f"SELECT * FROM {T_TASKS} INNER JOIN {T_USERS} ON {T_TASKS}.id_user = {T_USERS}.id WHERE {T_USERS}.id=?;", (index,))
            self.db.connection.commit()
            return self.db.cursor.fetchall()
        except sqlite3_error as e:
            print(f"[TASK:MANAGER] '{e}'")
            return None

    def update_data(self, data: tuple):
        try:
            data = data[1:] + (data[0],)
            self.db.cursor.execute(f"UPDATE {T_TASKS} SET task_name=?, task_dsc=?, task_status=?, id_user=? WHERE id=?;", (data))
            self.db.connection.commit()
        except sqlite3_error as e:
            print(f"[TASK:MANAGER] '{e}'")

    def insert_data(self, data: tuple):
        try:
            self.db.cursor.execute(f"INSERT INTO {T_TASKS} VALUES (NULL, ?, ?, ?, ?);", (data))
            self.db.connection.commit()
        except sqlite3_error as e:
            print(f"[TASK:MANAGER] '{e}'")

    def delete_data(self, index: int):
        try:
            self.db.cursor.execute(f"DELETE FROM {T_TASKS} WHERE id=?;", (index,))
            self.db.connection.commit()
        except sqlite3_error as e:
            print(f"[TASK:MANAGER] '{e}'")

    def delete_data_from_user(self, index: int):
        try:
            self.db.cursor.execute(f"DELETE FROM {T_TASKS} WHERE id_user=?;", (index,))
            self.db.connection.commit()
        except sqlite3_error as e:
            print(f"[TASK:MANAGER] '{e}'")