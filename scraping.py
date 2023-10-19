import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine
from tkinter import messagebox

# Função para coletar dados e salvá-los em um banco de dados SQLite
def scrape_and_save_data(url_base):
    try:
        # Name of the SQLite Database
        db_file = "AppStoreData.db"
        
        # Connect to SQLite using sqlalchemy using UTF-8
        engine = create_engine(f"sqlite:///{db_file}")
        conn = engine.connect()

        # URL da página do aplicativo desejado
        base_url = url_base
        page_num = 1
        reviews_per_page = 10  # Número de avaliações por página

        # Crie listas vazias para armazenar os dados
        rating_values = []
        review_dates = []
        review_contents = []

        while True:
            # Construa a URL da página atual
            url = f"{base_url}&showAllReviews=true&page={page_num}"

            # Envie uma solicitação GET para a URL
            response = requests.get(url)

            # Analise o conteúdo HTML usando BeautifulSoup
            soup = BeautifulSoup(response.content, "html.parser")

            # Extraia as classificações das avaliações
            ratings = soup.find_all("span", class_="F7XJmb")
            rating_values.extend([rating.get("data-number") for rating in ratings])

            # Extraia as datas das avaliações
            dates = soup.find_all("span", class_="bp9Aid")
            review_dates.extend([date.get_text() for date in dates])

            # Extraia o conteúdo das avaliações
            reviews = soup.find_all("div", class_="h3YV2d")  # Nome da classe atualizada
            review_contents.extend([review.get_text() if review else None for review in reviews])

            # Verifique se não há mais avaliações na página
            if len(ratings) < reviews_per_page:
                break

            # Incremente o número da página
            page_num += 1

            # Limite o número de páginas a serem raspadas
            if page_num == 20:
                break

        # Garanta que todas as listas tenham o mesmo comprimento
        min_length = min(len(rating_values), len(review_dates), len(review_contents))
        rating_values = rating_values[:min_length]
        review_dates = review_dates[:min_length]
        review_contents = review_contents[:min_length]

        # Crie um DataFrame para armazenar os dados
        comments_data = {
            "Rating": rating_values,
            "Date": review_dates,
            "Review": review_contents
        }
        comments_df = pd.DataFrame(comments_data)

        # Salve o DataFrame no banco de dados SQLite
        comments_df.to_sql("comments_data", conn, if_exists="replace", index=False)

        # Feche a conexão SQLite
        conn.close()

        # Exiba uma mensagem de sucesso em uma caixa de diálogo
        messagebox.showinfo("Sucesso", "Dados coletados e salvos com sucesso!")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao coletar dados: {str(e)}")
