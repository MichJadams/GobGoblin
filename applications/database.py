
import sqlite3

class Database:
    def __init__(self):
        self.database_name = "gob_goblin.db"

    def add_application(self, company, title, requirements, url):
        print(company)
        print(title)
        print(requirements)
        print(url)
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS jobs (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             company TEXT,
             position TEXT,
             requirements TEXT,
             url TEXT,
             status TEXT
         )''')
        c.execute('INSERT INTO jobs (company, position, requirements, url, status) VALUES (?, ?, ?, ?, ?)',
                  (company, title, requirements, url, "unapplied"))
        conn.commit()
        job_id = c.lastrowid
        conn.close()

    def get_applications(self):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS jobs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    company TEXT,
                    position TEXT,
                    requirements TEXT,
                    url TEXT,
                    status TEXT
                )''')
        c.execute('SELECT id, company, position, requirements, url, status FROM jobs')
        rows = c.fetchall()
        return  [list(row) for row in rows]
