import sqlite3

# Função para criar o banco de dados e a tabela
def create_database(db_file):
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Crie uma tabela para armazenar os dados
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS comments_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Rating INTEGER,
                Date TEXT,
                Review TEXT
            )
        ''')

        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print("Erro ao criar o banco de dados:", str(e)

# Função para consultar o banco de dados
def query_database(db_file, query):
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        cursor.execute(query)
        results = cursor.fetchall()

        conn.close()
        return results

    except sqlite3.Error as e:
        print("Erro ao consultar o banco de dados:", str(e)
        return []

# Exemplo de uso:
# db_file = "AppStoreData.db"
# create_database(db_file)
# query = "SELECT * FROM comments_data WHERE Rating > 3"
# results = query_database(db_file, query)
# for row in results:
#     print(row)
