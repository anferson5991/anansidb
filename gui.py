import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def create_gui(root, start_scraping):
    def select_output_folder():
        output_folder = filedialog.askdirectory()
        return output_folder

    def save_format_selection():
        selected_format = format_var.get()
        if selected_format == "SQLite":
            output_folder = select_output_folder()
            result_label.config(text="Coletando e salvando dados em formato SQLite. Aguarde!")
            scrape_and_save_data(url_entry.get(), output_folder, selected_format)
        elif selected_format == "XLSX":
            output_file = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("XLSX Files", "*.xlsx")])
            if output_file:
                result_label.config(text="Coletando e salvando dados em formato XLSX. Aguarde!")
                scrape_and_save_data(url_entry.get(), output_file, selected_format)
        else:
            messagebox.showwarning("Aviso", "Selecione um formato de saída válido.")

    url_label = tk.Label(root, text="URL Base do APP na PlayStore:")
    url_label.pack()
    url_entry = tk.Entry(root)
    url_entry.pack()

    format_var = tk.StringVar()
    format_var.set("SQLite")
    sqlite_radio = tk.Radiobutton(root, text="SQLite", variable=format_var, value="SQLite")
    xlsx_radio = tk.Radiobutton(root, text="XLSX", variable=format_var, value="XLSX")
    sqlite_radio.pack()
    xlsx_radio.pack()

    scrape_button = tk.Button(root, text="Coletar dados!", command=save_format_selection)
    scrape_button.pack()

    result_label = tk.Label(root, text="")
    result_label.pack()
