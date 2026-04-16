#!/bin/bash
#!/bin/python3

dir="/home/soso/miniprojet/sondes/"
addFile="/home/soso/miniprojet/archive/stockage.py"

# Si on ne veut séparer les bases de données on a juste à remplacer:
# addFile=/home/soso/miniprojet/archive/user_stockage.py
# et ajouter à la fin des commandes le nom serv


###### Note pour les sondes 
# Les fichiers doivent être dans le répertoire $dir
# Les sondes doivent renvoyer une valeur numérique (qui doit etre le dernier nombre que renvoie la sonde)

for file in `ls $dir`
do
  if [ `echo $file | egrep ".py"` ]
  then
  	nom=`basename $file ".py"`
 	python3 $addFile $nom $(python3 /home/soso/miniprojet/sondes/$file | grep -oE '[0-9]+(\.[0-9]+)?' | tail -n 1)
  elif [ `echo $file | egrep ".sh"` ]
  then
	nom=`basename $file ".sh"`
        python3 $addFile $nom $(sh /home/soso/miniprojet/sondes/$file | grep -oE '[0-9]+(\.[0-9]+)?' | tail -n 1)
  fi
done
