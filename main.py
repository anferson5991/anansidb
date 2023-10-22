import tkinter as tk
import os
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
    root.title("AnansiDB")
    root.geometry("400x200")

    # Defina o ícone personalizado (substitua 'icone.ico' pelo caminho real do seu ícone)
    icon_file = os.path.join(os.path.dirname(__file__), 'icone.ico')
    root.iconbitmap(default=icon_file)

    # Verificar atualizações automaticamente no início
    check_and_install_updates()

    # Crie a interface gráfica
    create_gui(root, start_scraping)

    # Inicie o loop principal da aplicação
    root.mainloop()
