import tkinter as tk
from . import *
from translate_integration.translate import Translator


class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title(WINDOW_TITLE)

        self.listbox_input = self.create_listbox(LANGUAGE_LIST, 0)
        self.listbox_output = self.create_listbox(LANGUAGE_LIST[1:], 3)
        self.listbox_input.activate_item = 0
        self.listbox_output.activate_item = 1
        self.listbox_input.bind("<<ListboxSelect>>", self.on_select_input)
        self.listbox_output.bind("<<ListboxSelect>>", self.on_select_output)
        
        self.text_input = self.create_text(1)
        self.text_output = self.create_text(2)
        self.text_output.config(state=tk.DISABLED)

        self.button_translate = self.create_button(TRANSLATE_BUTTON, 1, self.translate_listbox)
        self.button_clear = self.create_button(CLEAR_BUTTON, 2, self.clear_listboxes)

        self.button_source_lang = self.create_button(LANGUAGE_LIST[self.listbox_input.activate_item], 0, state=tk.DISABLED)
        self.button_dest_lang = self.create_button(LANGUAGE_LIST[self.listbox_output.activate_item], 3, state=tk.DISABLED)

    def create_listbox(self, languages: list, place: int):
        listbox = tk.Listbox(self, relief=RELIEF, width=WIDTH, height=HEIGHT)
        for language in languages:
            listbox.insert(tk.END, language)
        listbox.grid(row=0, column=place, sticky="NSWE")
        return listbox

    def create_text(self, place: int):
        text = tk.Text(self, width=WIDTH, height=HEIGHT, relief=RELIEF)
        text.grid(row=0, column=place)
        return text

    def create_button(self, text: str, place: int, func=0, state=tk.ACTIVE):
        if func:
            button = tk.Button(self, text=text, width=WIDTH, height=BUTTON_HEIGHT, relief=RELIEF, command=func, state=state)
        else:
            button = tk.Button(self, text=text, width=WIDTH, height=BUTTON_HEIGHT, relief=RELIEF, state=state)
        
        button.grid(row=1, column=place, sticky="NSWE")
        return button

    def translate_listbox(self): # translate button
        text_to_translate: str = self.text_input.get("1.0", tk.END)
        if len(text_to_translate) <= 1:
            return

        sorce_language: str|None = None
        if self.listbox_input.activate_item == 0:
            sorce_language = Translator.detect_language(text_to_translate)
        else:
            sorce_language = LANGUAGE_LIST[self.listbox_input.activate_item]

        if sorce_language is None:
            return

        self.text_output.config(state=tk.NORMAL)
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, Translator.translate_text(text_to_translate, sorce_language, LANGUAGE_LIST[self.listbox_output.activate_item]))
        self.text_output.config(state=tk.DISABLED)

    def on_select_input(self, event): # on select event for listbox_input
        try:
            self.listbox_input.activate_item = self.listbox_input.curselection()[0]
            self.button_source_lang.configure(text=LANGUAGE_LIST[self.listbox_input.activate_item])
        except Exception:
            return

    def on_select_output(self, event): # on select event for listbox_output
        try:
            self.listbox_output.activate_item = self.listbox_output.curselection()[0] + 1
            self.button_dest_lang.configure(text=LANGUAGE_LIST[self.listbox_output.activate_item])
        except Exception:
            return

    def clear_listboxes(self): # clear text input and output
        self.text_input.delete("1.0", tk.END)
        self.text_output.delete("1.0", tk.END)