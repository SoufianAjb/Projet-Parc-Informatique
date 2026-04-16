#/bin/bash

cat > index.html << EOF
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Supervision - Accueil</title>
</head>
<body>

    <h1>BIENVENUE SUR LE SITE DE GESTION</h1>

    <div>
        <h2>Données collectées sur le serveur</h2>

EOF

	for i in `ls graphes/`
	do
		echo `basename $i .svg` >> index.html
        	echo "<object type="image/svg+xml" data="graphes/$i" width="1000" height="600"></object> <br><br>" >> index.html
	done


cat >> index.html << EOF
	</div>
  </body>
</html>

EOF
