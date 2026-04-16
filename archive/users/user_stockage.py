import sqlite3
import feedparser
import datetime
import sys
import send_mail

DB_FILE = "/home/soso/miniprojet/archive/save_alert.db"
HISTORY_FILE = "/home/soso/miniprojet/archive/max_history.txt"
with open(HISTORY_FILE,"r",encoding="utf-8") as file:
    res = file.readlines()
MAX_HISTORY = int(res[0])
sondesMax = {"cpu":0.0,"memory":30.0,"users":20.0}

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS data_users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT,
            user TEXT,
            valeur TEXT,
            date TEXT
        )''')
    conn.commit()
    conn.close()

def insert(title,value,user):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''INSERT INTO data_users (titre,user,valeur,date) VALUES (?, ?, ?, ?)''', (title,user,value,date))
    conn.commit()
    conn.close()

def saveSondes(title, value, user):
    insert(title, value, user)
    if(title in sondesMax.keys()):
        if(float(value) > sondesMax[title]):
            send_mail.sendMail(title,value)
    clean()

def clean():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
    	DELETE FROM data_users
        WHERE id NOT IN (
            SELECT id FROM data_users ORDER BY id DESC LIMIT ?
        )
    ''', (MAX_HISTORY,))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    if len(sys.argv) > 1:
        typeVal = sys.argv[1]
        val = sys.argv[2]
        user = sys.argv[3]
        saveSondes(typeVal,val,user)
