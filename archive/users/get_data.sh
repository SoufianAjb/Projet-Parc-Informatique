#!/bin/bash
#!/bin/python3

user="koko@10.0.2.4"
# Récupération de la sonde sur le local
cpuUserA=$(python3 /home/soso/miniprojet/sondes/cpu.py | grep -oE '[0-9]+(\.[0-9]+)?')
memoryUserA=$(python3 /home/soso/miniprojet/sondes/memory.py | grep -oE '[0-9]+(\.[0-9]+)?')
usersA=$(sh /home/soso/miniprojet/sondes/user.sh | grep -oE '[0-9]+(\.[0-9]+)?' | tail -n 1)
usernameA=`whoami`
python3 /home/soso/miniprojet/archive/users/user_stockage.py cpu $cpuUserA $usernameA
python3 /home/soso/miniprojet/archive/users/user_stockage.py memory $memoryUserA $usernameA
python3 /home/soso/miniprojet/archive/users/user_stockage.py user $usersA $usernameA

# Récupération de la sonde sur un user
cpuUserB=$(ssh $user "python3 -" < "/home/soso/miniprojet/sondes/cpu.py" | grep -oE '[0-9]+(\.[0-9]+)?')
memoryUserB=$(ssh $user "python3 -" < "/home/soso/miniprojet/sondes/memory.py" | grep -oE '[0-9]+(\.[0-9]+)?')
usersB=$(ssh $user "sh -" < "/home/soso/miniprojet/sondes/user.sh" | grep -oE '[0-9]+(\.[0-9]+)?' | tail -n 1)
usernameB=$(ssh $user "whoami")
python3 /home/soso/miniprojet/archive/users/user_stockage.py cpu $cpuUserB $usernameB
python3 /home/soso/miniprojet/archive/users/user_stockage.py memory $memoryUserB $usernameB
python3 /home/soso/miniprojet/archive/users/user_stockage.py user $usersB $usernameB

