import psutil as p

def get_cpu():
    return p.cpu_percent(interval=1)

print("Pourcentage du CPU : ", get_cpu())
