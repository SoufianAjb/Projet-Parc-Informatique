import psutil as p

print("Pourcentage de la mémoire utilisé : ", p.virtual_memory().percent)
