# imports
import pygame
import settings

def loopCheck(enter = 0):                           # verifie si un evenement de sortie a ete effectue
    # return void
    # parametre : aucun, ou 1 pour gerer la touche entrer comme touche de sortie
    for event in pygame.event.get():                # parcourt des evenements recus
        if event.type == pygame.QUIT:               # verification des evenement de sortie (alt + F4, fermeture, etc...)
            print "quit"
            exit()                                  # quitte le programme
        if event.type == pygame.KEYDOWN:            # si une touche est pressee
            if event.key == pygame.K_ESCAPE:        # si cette touche est la touche 'echap'
                print "quit"
                exit()                              # quitte le programme
            if enter:
                if event.key == pygame.K_RETURN:    # si cette touche est la touche 'entrer'
                    print "quit"
                    exit()                          # quitte le programme
