import tkinter as tk

# Função para criar a interface gráfica
def create_gui(root, start_scraping):
    # Crie um rótulo e uma entrada para inserir a URL base
    url_label = tk.Label(root, text="URL Base:")
    url_label.pack()
    url_entry = tk.Entry(root)
    url_entry.pack()

    # Crie um botão para iniciar o processo de scraping
    scrape_button = tk.Button(root, text="Iniciar Coleta de Dados", command=start_scraping)
    scrape_button.pack()

    # Crie um rótulo para exibir o resultado
    result_label = tk.Label(root, text="")
    result_label.pack()
