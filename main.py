import tkinter as tk
import os
from scraping import scrape_and_save_data
from updates import check_and_install_updates
from gui import create_gui

def start_scraping():
    url_base = url_entry.get()
    result_label.config(text="Coletando e salvando dados... (isso pode levar algum tempo)")
    scrape_and_save_data(url_base)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("AnansiDB")
    root.geometry("400x200")

    icon_file = os.path.join(os.path.dirname(__file__), 'icone.ico')
    root.iconbitmap(default=icon_file)

    check_and_install_updates()
    create_gui(root, start_scraping)
    root.mainloop()
