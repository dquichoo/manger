'''
Ici, le problème se situe lignes 94 à 105. Le programme ne détecte pas
l'alignement des pions de même couleur en diagonale décroissante
'''


grille=[7*[0], 7*[0], 7*[0], 7*[0], 7*[0], 7*[0]]

# tab_colonne mémorise le nombre de pions dans chacune des colonnes
tab_colonne=7*[0]
# joueur_courant indique le prochain joueur qui doit jouer : 1 pour ROUGE et 2 pour BLEU
joueur_courant=1

a  = 3
# La fonction afficher_grille() affiche la grille
def afficher_grille():
    for i in range(6):
        print(grille[i])

    # affiche le repère des colonnes sous la grille :
    print('\n 0  1  2  3  4  5  6')


# La fonction grille_pleine() teste si la grille est pleine
def grille_pleine():
    for i in range(6):
        for j in range(7):
            if grille[i][j]==0:
                return False
    return True

# La fonction pions_alignes() teste si 4 pions de même couleur sont alignés dans la grille
def pions_alignes():
    trouve=0
    # teste 4 pions alignés horizontalement en alanysant chacune des 6 lignes :
    for i in range(6):
        rouge=0
        bleu=0
        for j in range(7):
            if grille[i][j]==1:
                rouge+=1
                bleu=0
                if rouge>=4:
                    trouve=1
                    gagnant = 2
                    return trouve
            elif grille[i][j]==2:
                rouge=0
                bleu+=1
                if bleu>=4:
                    trouve=2
                    gagnant = 1
                    return trouve
            else:
                rouge=0
                bleu=0

    # teste 4 pions alignés verticalement en alanysant chacune des 7 colonnes :
    for j in range(7):
        rouge=0
        bleu=0
        for i in range(6):
            if grille[i][j]==1:
                rouge+=1
                bleu=0
                if rouge>=4:
                    trouve=1
                    gagnant = 2
                    return trouve
            elif grille[i][j]==2:
                rouge=0
                bleu+=1
                if bleu>=4:
                    trouve=2
                    gagnant = 1
                    return trouve
            else:
                rouge=0
                bleu=0

    # on teste les diagonales croissantes:

    for i in range(3):
        for j in range(2):
            if grille[i][j] == 1 and grille[i+1][j+1] == 1 and grille[i+2][j+2] == 1 and grille [i+3][j+3] == 1:
                trouve=2
                gagnant=1
                return trouve
            if grille[i][j] == 2 and grille[i+1][j+1] == 2 and grille[i+2][j+2] == 2 and grille [i+3][j+3] == 2:
                trouve=1
                gagnant=2
                return trouve
    #On teste les diagonales décroissantes
    for i in range(6):
        for j in range(6):
            if grille[i][j] == 1 and grille[i-1][j+1] == 1 and grille[i-2][j+2] == 1 and grille [i-3][j+3] == 1:
                print("trouve")
                trouve=2
                gagnant=1
                return trouve
            if grille[i][j] == 2 and grille[i-1][j+1] == 2 and grille[i-2][j+2] == 2 and grille [i-3][j+3] == 2:
                print("trouve")
                trouve=1
                gagnant=2
                return trouve
        

    # si on n'a rien trouvé on retourne 0 :
    return 0

# La fonction tester_saisie demande au joueur de saisir un nombre entre 0 et 6,
# et recommence tant que la valeur saisie n'est pas un entier dans cet intervale

def tester_saisie(joueur_courant):
    """
    teste la saisie
    @joueur_courant: le joueur courant
    """
    if joueur_courant==1:
        joueur='ROUGE'
    else:
        joueur='BLEU'
    saisie_correct=False
    while not saisie_correct:
        s_colonne=input("%s : entrez la colonne où jouer (de 0 à 6) :" % joueur)
        # teste si la chaine saise est un entier :
        if not s_colonne.isdigit():
            print("Erreur de saise : la valeur entrée par le joueur %s n'est pas un nombre entier. Recommencez." % joueur)
        # teste si la valeur numérique est comprise entre 0 et 6 :
        elif int(s_colonne)<0 or int(s_colonne)>6:
            print("Erreur de saise : la valeur numérique entrée par le joueur %s n'est pas comprise entre 0 et 6. Recommencez." % joueur)
        else:
            saisie_correct=True
#convertit en entier et on la renvoie
    return int(s_colonne)


# La fonction jouer() demande au joueur courant dans quelle colonne il veut jouer
def jouer(joueur_courant):
    if joueur_courant==1:
        joueur='ROUGE'
    else:
        joueur='BLEU'
    # La fonction tester_saisie renvoie forcément un chiffre entre 0 et 6 :
    colonne=tester_saisie(joueur_courant)
    while tab_colonne[colonne]==6:
        print('La colonne %d est pleine ! %s jouez dans une colonne non pleine' % (colonne,joueur))
        colonne=tester_saisie(joueur_courant)
    grille[5-tab_colonne[colonne]][colonne]=joueur_courant
    tab_colonne[colonne]+=1
    print('\nLe joueur %s vient de jouer dans la colonne %d :' % (joueur,colonne))

#Programme principal
print('Le nom des joueurs sera ici ROUGE et BLEU. Le joueur ROUGE commence.')
print('Début de la partie (la grille est vide) :')
gagnant=0
while not grille_pleine() and gagnant==0:
    afficher_grille()
    jouer(joueur_courant)
    joueur_courant=3-joueur_courant
    gagnant=pions_alignes()
if pions_alignes()==1:
    print('Bravo ! Le joueur ROUGE a gagné !')
elif pions_alignes()==2:
    print('Bravo ! Le joueur BLEU a gagné !')

afficher_grille()
if gagnant==0:
    print("Fin de la partie : la grille est pleine et il n'y a pas 4 pions alignés")
elif grille_pleine():
    print("Fin de la partie : 4 pions sont alignés et la grille est pleine")
else:
    print("Fin de la partie : 4 pions sont alignés et la grille n'est pas pleine")
