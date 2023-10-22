import requests
from tkinter import messagebox

# URL da página de atualizações no site oficial
update_url = "https://anansidb.github.io/versions/anansidb_version.txt"
# Versão atual do aplicativo
current_version = "1.2"  # Atualize para a versão atual do seu aplicativo

# Função para verificar e instalar atualizações
def check_and_install_updates():
    try:
        # Envie uma solicitação GET para a URL de atualizações
        response = requests.get(update_url)

        if response.status_code == 200:
            latest_version = response.text.strip()

            # Verifique se há uma versão mais recente disponível
            if latest_version > current_version:
                # Faça o download da atualização
                update_download_url = f"https://anansidb.github.io/versions/anansidb_v{latest_version}.exe"
                update_response = requests.get(update_download_url)
                
                if update_response.status_code == 200:
                    # Aqui você pode adicionar a lógica para instalar a atualização,
                    # como fazer o download do arquivo e executar a instalação.
                    
                    # Exiba uma mensagem de sucesso em uma caixa de diálogo
                    messagebox.showinfo("Sucesso", f"Nova atualização (v{latest_version}) baixada com sucesso e pronta para ser instalada.")
                else:
                    messagebox.showerror("Erro", "Falha ao fazer o download da atualização.")
            else:
                messagebox.showinfo("Atualizado", "Você já possui a versão mais recente do aplicativo.")
        else:
            messagebox.showerror("Erro", "Não foi possível verificar as atualizações.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao verificar/atualizar: {str(e)}")
