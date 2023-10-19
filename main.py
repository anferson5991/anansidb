import tkinter as tk
from tkinter import messagebox
from scraping import scrape_and_save_data
from updates import check_and_install_updates
from gui import create_gui

def start_scraping():
    url_base = url_entry.get()
    result_label.config(text="Coletando e salvando dados...")
    scrape_and_save_data(url_base)

if __name__ == "__main__":
    # Crie a janela principal da aplicação
    root = tk.Tk()
    root.title("Web Scraping App")
    root.geometry("400x200")

    # Verificar atualizações automaticamente no início
    check_and_install_updates()

    # Crie a interface gráfica
    create_gui(root, start_scraping)

    # Inicie o loop principal da aplicação
    root.mainloop()
