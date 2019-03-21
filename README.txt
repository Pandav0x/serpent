***************
 INTRODUCTION
***************

Ce programme se veut pédagogique : il à été créer dans le but de faire découvrir
la programmation impérative par le biais d'appel de fonctions dans un ordre précis.

***************
   PRINCIPE
***************

Le but est de faire atteindre la sortie du labyrinthe a la fleche qui est controlée par
l'utilisateur.
Le controle se fait par l'appel des fonctions suivantes :

	avance() => fait avancer la fleche vers la case ou elle pointe si cela est possible
	tourne_gauche() => fait tourner la fleche vers la gauche
	tourne_droite() => fait tourner la fleche vers la droite

L'arrivee est symbolisée par un carré vert, les chemins par des carrés crèmes et les murs
par des carrés noirs.

	***************
   	   EDITION
	***************

L'édition est la partie principale de ce programme, c'est elle qui détermine le comportement
du programme.
Afin d'éditer ce comportement, ouvrez le fichier 'code.py' avec n'importe quel éditeur de texte brut.
J'enttend par la le bloc-note de windows, notepad++ ou n'importe quel éditeur de texte 'basique'.
(si vous n'en avez pas, vous pouvez en télécharger un ici : https://atom.io/download/windows)


***************
 CONFIGURATION 
***************


	***************	
 	 MODULES REQUIS
	***************
	
Ce programme est développé avec python 2.7, il nécéssite donc les outils suivants pour
son fonctionnement :

	- Python 2.7 (disponible ici : https://www.python.org/ftp/python/2.7.11/python-2.7.11.msi)
	
	- Pygame 1.9.1 (disponible ici : pygame.org/ftp/pygame-1.9.1.win32-py2.7.msi)

	
	***************
	 INSTALLATION
	***************

Une fois ces deux éléments téléchargés, vous n'avez plus qu'à installer python 2.7 en premier
lieu, puis pygame une fois la précédente installation terminée.
Ces deux installations ne sont que des installations 'Next next finish', vous n'avez
théoriquement rien d'autre à faire que de cliquer sur 'suivant' quelques fois puis sur
'terminer'.


	***************
	 VERIFICATION
	***************

Afin de vérifier que tout à correctement été installer, ouvrez la console windows
soit par le menu démarrer > Tous les programmes > Accessoires > invite de commande
Soit par le racourcis [windows]+[r], entrez 'cmd' puis appuyez sur entrer.
Entrez ensuite la commande suivante :
	
	start python.exe

Si une nouvelle console s'ouvre, python à bien été installé. Sinon, réinstallez-le.
Une fois cette nouvelle fenêtre ouverte, patientez jusqu'à ce que la dernière ligne
affichée soit '>>>' puis tapez les commandes suivantes :
	
	import pygame

	pygame.ver

Si le programme vous répond '1.9.1release', tout à correctement été installé. Sinon, si une erreur
survient lors de la réalisation d'une de ces étapes, recommencez l'installation.

***************
   EXECUTION
***************

Pour lancer le programe, vous n'aurez qu'à double-cliquer sur 'maze.py'.
Si cela de fonctionne pas, faite [shift]+[clique droit] dans le dossier où se trouve maze.py et cliquer
sur 'ouvrir une fenetre de commande ici'.
Vous devrez alors taper le chemin absolu de votre executable python (par defaut C:\python27\python.exe)
un espace puis maze.py 
Votre console devrait ressemblée à ceci 

C:\Users\Admin\Desktop\python>C:\python27\python.exe maze.py

appuyez sur entrer, vous n'aurez alors plus qu'à appuyer sur la flèche du haut pour remettre cette ligne
et réappuyer sur entrer

