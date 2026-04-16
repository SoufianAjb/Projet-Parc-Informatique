import pygal
import sqlite3
DB_FILE = "/home/soso/miniprojet/archive/save_alert.db"
DESTINATION = "/home/soso/miniprojet/web/graphes/"

def getValues(user):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data_users WHERE user='"+ user + "'")
    tab = cursor.fetchall()
    conn.commit()
    conn.close()
    return tab

def getAllUsers():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
	SELECT DISTINCT user FROM data_users''')
    tab = cursor.fetchall()
    conn.commit()
    conn.close()
    return tab

def generateGraphe():
    userList = getAllUsers()
    for k in range(len(userList)):
        data = []
        heures = []
        cpuTab = []
        usersTab = []
        memoryTab = []
        val = getValues(userList[k][0])
        for i in range(len(val)):
            value = float(val[i][3])
            heures.append(val[i][4])
            if val[i][1]=="memory":
                memoryTab.append(value)
            elif val[i][1]=="cpu":
                cpuTab.append(value)
            elif val[i][1]=="user":
                usersTab.append(value)
        graph = pygal.Line()	
        graph.title = 'Sondes de ' + str(userList[k][0])
        graph.add('% Mémoire', memoryTab)
        graph.add('% CPU', cpuTab)
        graph.add('Nombres utilsateurs', usersTab)
        fileGraph = DESTINATION + "graph-" + str(userList[k][0]) +".svg"
        graph.render_to_file(fileGraph)

if __name__ == "__main__":
    generateGraphe()

