# imports
import time
import pygame
import loop
import settings as s

########################
#global variables
coordinates = 0     # coordonnees de la fleche et de l'arrivee
delay = 0.2         # laps de temps entre chaque actions en secondes (avancer, tourner) (par defaut : 0.05)

########################
# user functions

def avance(iteration = 1):          # permet de repeter plusieurs fois l'action d'avancer
    # return void
    # parametre : aucun ou nombre de fois que l'on veut avancer
    for i in range(0, iteration):
        avance_simple()

def tourne_droite():            # fait tourner la fleche vers la droite
    # return void
    loop.loopCheck()
    s.arrowOri = s.arrowOri - 1 # soustrait 1 a la valeur de la rotation (voir dispElements() pour plus d'explications)
    refresh()

def tourne_gauche():             # fait tourner la fleche vers la gauche
    # return void
    loop.loopCheck()
    s.arrowOri = s.arrowOri + 1
    refresh()

# [obsolete]
def niy():                      # permet d'afficher un message si une fonction n'est pas encore implementee
    print "Not implemented yet"
    time.sleep(0.5)


def refresh():              # rafraichit l'ecran
    # return void
    global delay            # declare la variable locale 'delay' comme etant la variable globale 'delay'
    pygame.display.update() # ligne de rafraichit l'ecran
    dispMaze()              # reaffichage du Labyrinthe
    time.sleep(delay)       # pause du temps renseigne

####################################
# step forward functions

def avance_simple():    # fait avancer la fleche si possible
    # return void
    loop.loopCheck()    # permet des interaction dans l'execution des fonction utilisateur
    goNext()            # va sur la case en face de la fleche si possible
    refresh()           # rafraichit la fenetre
    if checkWin():      # verifie si la case sur laquelle avac l'utilisateur est la case de fin
        printWin()      # permet d'afficher l'interface finale

def goNext():                                                       # fait avancer la fleche
    # return void
    global coordinates                                              # rappatriement de la variable globale 'coordinates'
    if s.arrowOri%2 == 1: #right / left                             # detecte si la fleche est en position verticale ou horizontale
        if s.arrowOri%4 == 1: # right                               # detecte si la fleche fait face a la droite ou la gauche
            if checkNext(coordinates[1], coordinates[0] - 1) == 1:  # verifie si il y a possibilite d'avancer (si il y a un mur ou pas)
                coordinates[0] = int(coordinates[0]) - 1            # si c'est possible, l'abscisse diminue de 1
        else: # left                                                # sinon, si la fleche fait face a la gauche
            if checkNext(coordinates[1], coordinates[0] + 1) == 1:  # verifie si il y a possibilite d'avancer
                coordinates[0] = int(coordinates[0]) + 1            # si c'est possible, l'abscisse augmente de 1
    else :# up /down                                                # sinon, si la fleche est a la verticale
        if s.arrowOri%4 == 0: # up                                  # detecte si la fleche fait face au haut"
            if checkNext(coordinates[1] - 1, coordinates[0]) == 1:  # verifie si il y a possibilite d'avancer
                coordinates[1] = int(coordinates[1]) - 1            # si c'est possible, l'ordonnee diminue de 1
        else: # down                                                # sinon, si elle fait face au bas
            if checkNext(coordinates[1] + 1, coordinates[0]) == 1:  # verifie si il y a possibilite d'avancer
                coordinates[1] = int(coordinates[1]) + 1            # si c'est possible, l'ordonnee augmente de 1


def checkNext(x, y):                                                                            # verifie la case prochaine
    # return 0 ou 1
    # parametres : le x et le y de la destination voulue
    if (str(s.mazeMap[x][y]) == str('1') or (x == coordinates[3] and y == coordinates[2] )):    # si la valeur est de 1 dans la matrice du Labyrinthe (si c'est un chemin)
        return 1                                                                                # renvoie 1
    else:                                                                                       # sinon, si la valeur n'est pas de 1
        return 0                                                                                # renvoie 0

def checkWin():                                                                 # verifie si l'utilisateur a gagner
    # return 0 ou 1
    global coordinates
    if coordinates[0] == coordinates[2] and coordinates[1] == coordinates[3]:   # si les coordonnees de la fleche sont les memes que celles de l'arrivee
        return 1                                                                # renvoie 1
    else:
        return 0                                                                # renvoie 0

def printWin():                                                                                         # fonction qui affiche l'ecran final si l'utilisateur a gagner
    # return void
    dezoomPic = 5                                                                                       # ratio de dezoom sur le logo du departement (trop grosse resolution)
    sizeWin = s.pictures['4'].get_rect().size                                                           # recuperation des tailles des deux images de fin
    sizeDpt = s.pictures['5'].get_rect().size
    s.window.blit(s.pictures['4'], (int(sizes()[0]*sizes()[2]/4),int(sizes()[0]*sizes()[2]/4)))
    s.window.blit(pygame.transform.scale(s.pictures['5'], (int(sizeDpt[0] / dezoomPic),                 # affichage du logo du departement avec remise a la bonne taille
    int(sizeDpt[1] / dezoomPic))), (int(sizes()[0]*sizes()[2] - (dezoomPic+1)*(sizeDpt[0]/sizes()[2])),
    int(sizes()[1]*sizes()[2] - (dezoomPic+1)*(sizeDpt[1]/sizes()[2]))))
    pygame.display.update()                                                                            # rafraichissement de la fenetre


####################################################
#initialization and display functions

def getFileContent(filename):                           # recupere le contenu d'un fichier texte et le renvoie
    # return tableau
    # parametre : nom du fichier texte a charger (sans extention)
    with open('map/' + filename + '.txt', 'r') as tmp:  # definition d'une variable temporaire pour stocker les lignes du fichier
        array = []                                      # declaration du tableau qui sera renvoyer par la fonction
        for line in tmp:                                # boucle du parcourt de toutes les lignes
            array.append(line)                          # ajoute la ligne actuelle a la fin du tableau
    return array                                        # retourne un tableau avec toutes les lignes

def sizes():                # retourne un tableau avec toutes les tailles
    # retrun tableau
    ratio = 30              # taille des images (peut etre different, mais au dessus de 30 la fenetre est trop grande)
    return [14, 21, ratio]  # retourne un tableau avec les valeurs [largeur du Labyrinthe, hauteur du Labyrinthe, ratio]

def beginLocation(filename):                                # recupere les coordonnees initiales de la fleche et celles de l'arrivee depuis un fichier texte
    # return void
    global coordinates
    with open('map/' + filename + 'begin.txt', 'r') as tmp:
        array = []
        for line in tmp:
            array.append(int(line))
    coordinates = array

def initPictures():                                                                     # charge en memoire les images qui vont etre utilisees par le programme
    # return void
    folder = "pic\\"                                                                    # defini le repertoire des images
    ext = ".jpg"                                                                        # defini l'extention des images
    wall = pygame.image.load(folder + "wall" + ext).convert()                           # image des murs
    path = pygame.image.load(folder + "path" + ext).convert()                           # image des chemins
    arrow = pygame.image.load(folder + "arrow" + ext).convert()                         # image de la fleche
    goal = pygame.image.load(folder + "goal" + ext).convert()                           # image de l'arrivee
    win = pygame.image.load(folder + "win.png").convert_alpha()                         # logo de victoire (convert_alpha() sert a garder la transparence)
    s.pictures = {'0': wall, '1':path, '2':arrow, '3':goal, '4':win, '5':dpt, '6':icon} # stock les images dans la variable globale pictures

def pygameInit():                                                                       # initialise tout ce qui doit l'etre
    # return le contexte de la fenetre creee
    pygame.init()                                                                       # initialisation de pygame
    window = pygame.display.set_mode((sizes()[0]*sizes()[2], sizes()[1]*sizes()[2]))    # affiche la fenetre a la taille specifiee (nombre d'elements en x * ratio, nombre d'elements en y * ratio)
    pygame.display.set_caption("Serpent")                                               # change le titre de la fenetre
    initPictures()                                                                      # initialise les images
    pygame.display.set_icon(s.pictures['6'])                                            # change l'icone de la fenetre
    coordinates =  beginLocation('maze')                                                # recupere les coordonnees initiales de la fleche et celles de l'arrivee
    s.arrowOri = 0 # 0 => up / 1 => right / 2 => down / 3 => left                       # defini l'orientation de la fleche comme pointant vers le haut
    return window                                                                       # retourne le contexte

def dispMaze():                                                                                             # affiche le Labyrinthe
    # return void
    global coordinates
    for i in range(0, sizes()[1]):                                                                          # parcours de la matrice
        for j in range(0, sizes()[0]):
            s.window.blit(pygame.transform.scale(
            s.pictures[str(s.mazeMap[i][j])], (sizes()[2], sizes()[2])), (j * sizes()[2], i * sizes()[2]))  # affichage des elements et mise a l'echelle
    dispElements()                                                                                          # affiche les elements en surcouche (fleche et arrivee)
    pygame.display.update()

def dispElements():                                                     # affiche les elements en surcouche
    # retrun void
    global coordinates
    s.window.blit(pygame.transform.scale(pygame.transform.rotate(       # affiche la fleche en la mettant a l'echelle et en la faisant tourner en fonction du
    s.pictures['2'], (s.arrowOri%4) * 90), (sizes()[2], sizes()[2])),   #  modulo de la valeur de la rotation par 4. Si le reste de la division par 4 est egal a 0, elle pointe vers le haut
    (coordinates[0] * sizes()[2], coordinates[1]  * sizes()[2]))        #  1 : vers la droite, 2 : vers le bas et 3 vers la gauche

    s.window.blit(pygame.transform.scale(s.pictures['3'],               # affiche l'arrivee en la mettant a l'echelle
    (sizes()[2], sizes()[2])),(coordinates[2] * sizes()[2],
    coordinates[3] * sizes()[2]))
