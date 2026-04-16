import sqlite3
import feedparser

DB_FILE = "/home/soso/miniprojet/archive/save_alert.db"
MAX_HISTORY = 50
CERT_URL = "https://www.cert.ssi.gouv.fr/alerte/feed/"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            reference TEXT UNIQUE,
            title TEXT,
            date TEXT
        )''')
    conn.commit()
    conn.close()

def insert(ref, title, date):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO alerts (reference, title, date) VALUES (?, ?, ?)", (ref, title, date))
    print("Nouvelle alerte ajoutée")
    conn.commit()
    conn.close()

def save(ref, title, date):
    insert(ref, title, date)
    clean()

def clean():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
    	DELETE FROM alerts 
        WHERE id NOT IN (
            SELECT id FROM alerts ORDER BY id DESC LIMIT ?
        )
    ''', (MAX_HISTORY,))
    conn.commit()
    conn.close()

def get_last_alert():
    flux = feedparser.parse(CERT_URL)
    alerte = flux.entries[-1]
    titre = alerte.title
    lien = alerte.link
    date_publication = alerte.published
    print(f"Alerte trouvée : {titre} (Publiée le {date_publication})")
    return alerte

if __name__ == "__main__":
    init_db()
    alert = get_last_alert()
    if alert:
        save(alert.link, alert.title, alert.published)
