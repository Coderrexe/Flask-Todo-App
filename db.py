import sqlite3

class Database:
    def __init__(self, url):
        self.conn = sqlite3.connect(url, check_same_thread=False)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS ew (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            subject TEXT NOT NULL,
            beak TEXT NOT NULL,
            due_date TEXT NOT NULL
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def get_ews(self):
        cursor = self.conn.execute("SELECT * FROM ew")
        return cursor.fetchall()

    def create_ew(self, task, subject, beak, due_date):
        query = "INSERT INTO ew (task, subject, beak, due_date) VALUES (?, ?, ?, ?)"
        self.conn.execute(query, (task, subject, beak, due_date))
        self.conn.commit()
