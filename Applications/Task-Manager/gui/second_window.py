import tkinter as tk
from . import WindowBuilder
from database.queries import Task


class SecondWindow(tk.Tk):

    def __init__(self, data: tuple):
        super().__init__()
    
        self.title(f"{data[2]} {data[1]}")
        self.active_index: int = -1
        self.active_task: int = -1
        self.active_user: int = data[0]
        
        WindowBuilder.create_label(self, 0, 0, "USER INDEX:")
        WindowBuilder.create_label(self, 1, 0, "USER NAME:")
        WindowBuilder.create_label(self, 2, 0, "USER SURNAME:")
        WindowBuilder.create_label(self, 3, 0, "TASK INDEX:")
        WindowBuilder.create_label(self, 4, 0, "TASK NAME:")
        WindowBuilder.create_label(self, 5, 0, "TASK DSC:")
        WindowBuilder.create_label(self, 6, 0, "TASK STATUS:")

        self.index_entry = WindowBuilder.create_entry(self, 0, 1, 25, text=data[0], state=tk.DISABLED)
        self.name_entry = WindowBuilder.create_entry(self, 1, 1, 25, text=data[1], state=tk.DISABLED)
        self.surname_entry = WindowBuilder.create_entry(self, 2, 1, 25, text=data[2], state=tk.DISABLED)
        
        self.index_text = WindowBuilder.create_entry(self, 3, 1, 25)
        self.name_text = WindowBuilder.create_entry(self, 4, 1, 25)
        self.dsc_text = WindowBuilder.create_entry(self, 5, 1, 25)

        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.grid(row=6, column=1)
        self.task_status = tk.IntVar(value=0)
        
        options: tuple = ("IN PROGRESS", "DONE") 
        for index, option in enumerate(options):
            button = tk.Radiobutton(self.buttons_frame, text=option, variable=self.task_status, value=index)
            button.grid(row=7, column=index)

        self.add_task_button = WindowBuilder.create_button(self, 8, 0, "Add Task", self.add_task, pady=1)
        self.update_task_button = WindowBuilder.create_button(self, 9, 0, "Update Task", self.update_task, pady=1)
        self.remove_task_button = WindowBuilder.create_button(self, 10, 0, "Remove Task", self.remove_task, pady=1)
        self.tasks_listbox = WindowBuilder.create_listbox(self, 11, 0)
        self.tasks_scrollbar = WindowBuilder.create_scrollbar(self, 11, 1)

        self.tasks_listbox.configure(yscrollcommand=self.tasks_scrollbar.set)
        self.tasks_scrollbar.config(command=self.on_scroll)
        self.tasks_listbox.bind("<<ListboxSelect>>", self.on_select)

        self.update_listbox()

    def add_task(self):
        task_name: str = self.name_text.get()
        if len(task_name) == 0:
            return
        
        task_dsc: str = self.dsc_text.get()
        if len(task_dsc) == 0:
            return

        Task().insert_data((task_name, task_dsc, self.task_status.get(), self.active_user))
        self.update_listbox()

    def update_task(self):
        if self.active_task == -1:
            return

        task_name: str = self.name_text.get()
        if len(task_name) == 0:
            return
        
        task_dsc: str = self.dsc_text.get()
        if len(task_dsc) == 0:
            return

        Task().update_data((self.active_task, task_name, task_dsc, self.task_status.get(), self.active_user))
        self.update_listbox()

    def remove_task(self):
        if self.active_task == -1:
            return

        Task().delete_data(self.active_task)
        self.update_listbox()
        self.index_text.delete(0, tk.END)
        self.name_text.delete(0, tk.END)
        self.dsc_text.delete(0, tk.END)

    def update_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in Task().get_data(self.active_user):
            self.tasks_listbox.insert(tk.END, task[:4])

    def on_select(self, event):
        try:
            self.active_index = self.tasks_listbox.curselection()[0]
            data = self.tasks_listbox.get(self.active_index)
            if self.active_task == data[0]:
                return

            self.active_task = data[0]

            self.index_text.delete(0, tk.END)
            self.name_text.delete(0, tk.END)
            self.dsc_text.delete(0, tk.END)
            
            self.index_text.insert(tk.END, data[0])
            self.name_text.insert(tk.END, data[1])
            self.dsc_text.insert(tk.END, data[2])
            self.task_status.set(data[3])
        except Exception:
            return

    def on_scroll(self, *args):
        self.tasks_listbox.yview(*args)

"""
- problem with changing task_status
"""