import requests
from tkinter import messagebox

update_url = "https://anansidb.github.io/versions/anansidb_version.txt"
current_version = "1.2"

def check_and_install_updates():
    try:
        response = requests.get(update_url)

        if response.status_code == 200:
            latest_version = response.text.strip()

            if latest_version > current_version:
                update_download_url = f"https://anansidb.github.io/versions/anansidb_v{latest_version}.exe"
                update_response = requests.get(update_download_url)
                
                if update_response.status_code == 200:
                    # Add logic to install the update (not provided here).
                    messagebox.showinfo("Sucesso", f"Nova atualização (v{latest_version}) baixada com sucesso e pronta para ser instalada.")
                else:
                    messagebox.showerror("Erro", "Falha ao fazer o download da atualização.")
            else:
                messagebox.showinfo("Atualizado", "Você já possui a versão mais recente do aplicativo.")
        else:
            messagebox.showerror("Erro", "Não foi possível verificar as atualizações.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao verificar/atualizar: {str(e)}")
