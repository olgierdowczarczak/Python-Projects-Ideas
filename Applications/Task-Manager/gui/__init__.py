import tkinter as tk

MAIN_WINDOW_TITLE = "Task Manager"


class WindowBuilder:

    @classmethod
    def create_label(cls, master, pos_x: int, pos_y: int, text: str, padx=10, pady=0):
        label = tk.Label(master, text=text)
        label.grid(row=pos_x, column=pos_y, padx=padx, pady=pady)
        return label

    @classmethod
    def create_entry(cls, master, pos_x: int, pos_y: int, width: int, text:str = "", padx=10, pady=0, state=tk.NORMAL):
        entry = tk.Entry(master, width=width)
        
        if text:
            entry.insert(tk.END, text)
        
        if state != tk.NORMAL:
            entry.configure(state=state)
        
        entry.grid(row=pos_x, column=pos_y, padx=padx, pady=pady)
        return entry

    @classmethod
    def create_listbox(cls, master, pos_x: int, pos_y: int, sticky="NSWE", padx=10, pady=0):
        listbox = tk.Listbox(master)
        listbox.grid(row=pos_x, column=pos_y, columnspan=2, sticky=sticky, padx=padx, pady=pady)
        return listbox

    @classmethod
    def create_button(cls, master, pos_x: int, pos_y: int, text: str, func, sticky="NSWE", padx=10, pady=0):
        button = tk.Button(master, text=text, command=func)
        button.grid(row=pos_x, column=pos_y, columnspan=2, sticky=sticky, padx=padx, pady=pady)
        return button

    @classmethod
    def create_scrollbar(cls, master, pos_x: int, pos_y: int):
        scrollbar = tk.Scrollbar(master, orient="vertical")
        scrollbar.grid(row=pos_x, column=pos_y, sticky="NSE")
        return scrollbar