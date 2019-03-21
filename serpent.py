# -*- coding : UTF-8 -*-
###############################
# PROGRAMME PRINCIPAL
###############################

#SDL Settings
# la fenetre apparaitra aux coordonnees(x,y) sur l'ecran
x = 100
y = 50
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

#imports
import settings as s            # (perso) contient les variables blobales
from pygame import *            # (system) pour la fenetre et ses interactions (evenements, etc...)
import loop                     # (perso) verification pour la boucle principale
import time                     # (system) permet de faire des pauses dans le code (lors de l'execution notament)
from function import *          # (perso) pour toutes les fonctions lourdes
try:                            # on test si il y a quelque chose dans le main() de code.py
    import code                 # (perso) le code de l'utilisateur
except IndentationError as ex:  # gestion de l'erreur du main() vide
    print "nothing to do"

s.init()                # initialisation de toutes les variables globales

print "looping..."
print "ratio : ", sizes()[2], "px"      # le ratio est la taille des sprites utilises (ici 30x30 px)
loop.loopCheck()                        # verifie si des conditions de sortie sont reunies
dispMaze()                              # affiche le labyrinthe
try:                                    # si code est vide il y aura une erreur de nom
    code.main()                         # execute le contenu de la fonction 'main' dans le fichier 'code.py'
except NameError:                       # gestion de l'erreur du non import de code.py
    pass                                # on continue comme si de rien n'etait
print "execution over"                  # quand tout est termine
print "end\npress enter key to quit"    # on demande a l'utilisateur d'appuyer sur entrer
while 1:                                # tant qu'il ne l'a pas fait
    loop.loopCheck(1)                   # verifie si il a appuyer sur une touche de sortie
