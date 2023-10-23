import sqlite3

def create_database(db_file):
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

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
        
        messagebox.showinfo("Sucesso", "Banco de dados criado com sucesso.")
    except sqlite3.Error as e:
        messagebox.showerror("Erro", f"Erro ao criar o banco de dados: {str(e)}")
        conn.close()

def query_database(db_file, query):
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        cursor.execute(query)
        results = cursor.fetchall()

        conn.close()
        return results

    except sqlite3.Error as e:
        messagebox.showerror("Erro", f"Erro ao consultar o banco de dados: {str(e)}")
        return []
