import tkinter as tk
from . import WindowBuilder, MAIN_WINDOW_TITLE
from .second_window import SecondWindow
from database.queries import User, Task


class MainWindow(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        self.title(MAIN_WINDOW_TITLE)
        self.active_user: int = -1
        self.active_index: int = -1
        self.in_second_window: bool = False

        WindowBuilder.create_label(self, 0, 0, "INDEX:")
        WindowBuilder.create_label(self, 1, 0, "NAME:")
        WindowBuilder.create_label(self, 2, 0, "SURNAME:")

        self.index_entry = WindowBuilder.create_entry(self, 0, 1, 25)
        self.name_entry = WindowBuilder.create_entry(self, 1, 1, 25)
        self.surname_entry = WindowBuilder.create_entry(self, 2, 1, 25)
        self.task_menu_button = WindowBuilder.create_button(self, 3, 0, "Task Menu", self.add_task, pady=1)
        self.add_user_button = WindowBuilder.create_button(self, 4, 0, "Add User", self.add_user, pady=1)
        self.edit_user_button = WindowBuilder.create_button(self, 5, 0, "Edit User", self.update_user, pady=1)
        self.remove_user_button = WindowBuilder.create_button(self, 6, 0, "Remove User", self.remove_user, pady=1)
        self.users_listbox = WindowBuilder.create_listbox(self, 7, 0)
        self.users_scrollbar = WindowBuilder.create_scrollbar(self, 7, 1)
        
        self.users_listbox.configure(yscrollcommand=self.users_scrollbar.set)
        self.users_scrollbar.config(command=self.on_scroll)
        self.users_listbox.bind("<<ListboxSelect>>", self.on_select)

        self.update_listbox()

    def add_task(self):
        if self.active_user == -1:
            return

        user_name: str = self.name_entry.get()
        if len(user_name) == 0:
            return
        
        user_surname: str = self.surname_entry.get()
        if len(user_surname) == 0:
            return

        self.in_second_window = True
        self.index_entry.configure(state=tk.DISABLED)
        self.name_entry.configure(state=tk.DISABLED)
        self.surname_entry.configure(state=tk.DISABLED)
        self.task_menu_button.configure(state=tk.DISABLED)
        self.add_user_button.configure(state=tk.DISABLED)
        self.edit_user_button.configure(state=tk.DISABLED)
        self.remove_user_button.configure(state=tk.DISABLED)
        self.users_listbox.configure(state=tk.DISABLED)
        self.second_window = SecondWindow(self.users_listbox.get(self.active_index))
        self.second_window.protocol("WM_DELETE_WINDOW", self.on_second_window_close)
        self.second_window.grab_set()
        self.second_window.focus_set()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def add_user(self):
        user_name: str = self.name_entry.get()
        if len(user_name) == 0:
            return
        
        user_surname: str = self.surname_entry.get()
        if len(user_surname) == 0:
            return

        User().insert_data((user_name, user_surname))
        self.update_listbox()
    

    def update_user(self):
        if self.active_user == -1:
            return

        user_name: str = self.name_entry.get()
        if len(user_name) == 0:
            return
        
        user_surname: str = self.surname_entry.get()
        if len(user_surname) == 0:
            return

        User().update_data((self.active_user, user_name, user_surname))
        self.update_listbox()

    def remove_user(self):
        if self.active_user == -1:
            return

        User().delete_data(self.active_user)
        Task().delete_data_from_user(self.active_user)

        self.active_user = -1
        self.active_index = -1
        self.update_listbox()
        self.index_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.surname_entry.delete(0, tk.END)

    def update_listbox(self):
        self.users_listbox.delete(0, tk.END)
        for user in User().get_data():
            self.users_listbox.insert(tk.END, user)

    def on_select(self, event):
        try:
            self.active_index = self.users_listbox.curselection()[0]
            data = self.users_listbox.get(self.active_index)
            if self.active_user == data[0]:
                return

            self.active_user = data[0]

            self.index_entry.delete(0, tk.END)
            self.name_entry.delete(0, tk.END)
            self.surname_entry.delete(0, tk.END)
            
            self.index_entry.insert(tk.END, data[0])
            self.name_entry.insert(tk.END, data[1])
            self.surname_entry.insert(tk.END, data[2])
        except Exception:
            return

    def on_scroll(self, *args):
        self.users_listbox.yview(*args)

    def on_second_window_close(self):
        self.index_entry.configure(state=tk.NORMAL)
        self.name_entry.configure(state=tk.NORMAL)
        self.surname_entry.configure(state=tk.NORMAL)
        self.task_menu_button.configure(state=tk.NORMAL)
        self.add_user_button.configure(state=tk.NORMAL)
        self.edit_user_button.configure(state=tk.NORMAL)
        self.remove_user_button.configure(state=tk.NORMAL)
        self.users_listbox.configure(state=tk.NORMAL)
        self.second_window.focus_set()
        self.second_window.grab_release()
        self.second_window.update()
        self.second_window.destroy()
        self.in_second_window = False
    
    def on_close(self):
        if self.in_second_window:
            pass
        else:
            self.destroy()