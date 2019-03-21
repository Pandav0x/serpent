# imports
from function import *


def init():                             # initialise les variables globales
    # return void
    global pictures
    pictures = None                     # toutes les images du programme
    global mazeMap
    mazeMap = getFileContent('maze')    # matrice de la carte du labyrynthe
    global window
    window = pygameInit()               # contexte de la fenetre du programme
    global arrowOri
    arrowOri = 0                        # orientation de la fleche
