from database.queries import User, Task
from gui.main_window import MainWindow


def main():
    User().create_table()
    Task().create_table()
    window = MainWindow()
    window.mainloop()

if __name__ == "__main__":
    main()