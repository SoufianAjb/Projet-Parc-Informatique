import pygal
import sqlite3
DB_FILE = "/home/soso/miniprojet/archive/save_alert.db"
DESTINATION = "/home/soso/miniprojet/web/"

def getValues():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM data''')
    tab = cursor.fetchall()
    conn.commit()
    conn.close()
    return tab

def generateGraphe():
    val = getValues()
    data = []
    heures = []
    cpuTab = []
    usersTab = []
    memoryTab = []
    for i in range(len(val)):
        value = float(val[i][3])
        heures.append(val[i][1])
        if val[i][2]=="memory":
            memoryTab.append(value)
        elif val[i][2]=="cpu":
            cpuTab.append(value)
        elif val[i][2]=="user":
            usersTab.append(value)

    graph = pygal.Line()
    #graph.x_labels = map(str,
    graph.title = 'Évolution des sondes'
    graph.add('% Mémoire', memoryTab)
    graph.add('% CPU', cpuTab)
    graph.add('Nombres utilsateurs', usersTab)
    fileGraph = DESTINATION + "test.svg"
    graph.render_to_file(fileGraph)

if __name__ == "__main__":
    generateGraphe()

