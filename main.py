from random import *

#Définir le jeu de carte:
jeu = []
num = ["7", "8", "9", "X", "V", "D", "R", "A"]
coul = ["C", "K", "T", "P"]
mains_joueurs = [[], []]
valeurs_cartes = [1, 2, 3, 4, 5, 6, 7, 8]
vainqueur = ""

#Construire le jeu de cartes
for couleur in coul:
    for numero in num:
        jeu.append(numero + couleur)

#Mélanger le jeu
shuffle(jeu)

#Donner un nom aux joueurs
joueur_1 = input("Quel est le nom du joueur 1 ? ")
joueur_2 = input("Quel est le nom du joueur 2 ? ")
joueurs = [joueur_1, joueur_2]

#Distribue une carte sur deux aux joueurs
for i in range(0, len(jeu), 2):
    mains_joueurs[0].append(jeu[i])
    mains_joueurs[1].append(jeu[i + 1])

#Fonction qui renvoie la valeur des cartes (juste pour savoir laquelle est la plus forte)
def valeur_carte (carte):
  """
  Input : str (une carte)
  Output : int (la valeur de la carte)
  Effet : renvoie la valeur des cartes (juste pour savoir laquelle est la plus forte)
  """
  for i in range(len(num)):
    if carte[0] == num[i]:
      return valeurs_cartes[i]

#Fonction qui regarde si un joueur n'a plus de cartes, donc que l'autres à gagné
def check_victoire():
  """
  Input : Aucun
  Output : Aucun (change la 'variable' vainqueur en le nom du vainqueur)
  Effet : regarde si un joueur n'a plus de cartes, donc que l'autres à gagné
  """
  global vainqueur
  if len(mains_joueurs[0]) == 0:
    vainqueur = joueurs[1]
  elif len(mains_joueurs[1]) == 0:
    vainqueur = joueurs[0]

#Fonction qui fait une bataille (quand les deux joueurs ont la même valeur de carte)
def bataille():
  """
  Input : Aucun
  Output : Aucun (change les mains des joueurs comme il faut après le coup)
  Effet : fait une bataille (quand les deux joueurs ont la même valeur de carte)
  """
  global mains_joueurs
  fini = False
  iteration = 0
  #si un joueur n'a plus assez de carte on change la carte de celui qui en a pour que ça ne fasse pas la bataille sinon ça fait un out of range
  while fini == False:
    if len(mains_joueurs[0]) <= 3 + iteration * 2:
      mains_joueurs[1].append(mains_joueurs[1].pop(0))
      return
    if len(mains_joueurs[1]) <= 3 + iteration * 2:
      mains_joueurs[0].append(mains_joueurs[0].pop(0))
      return
    print("Il y a bataille ! ")
    carte_joueur_1 = mains_joueurs[0][iteration * 2 + 2]
    carte_joueur_2 = mains_joueurs[1][iteration * 2 + 2]
    print(joueurs[0] + " pose la carte : " + carte_joueur_1)
    print(joueurs[1] + " pose la carte : " + carte_joueur_2)
    if valeur_carte(carte_joueur_1) > valeur_carte(carte_joueur_2):
      print("C'est " + joueurs[0] + " qui remporte la bataille")
      if iteration == 0:
        for j in range (3):
          mains_joueurs[0].append(mains_joueurs[0].pop(0))
          mains_joueurs[0].append(mains_joueurs[1].pop(0))
      else :
        for i in range(iteration):
          for j in range (3):
            mains_joueurs[0].append(mains_joueurs[0].pop(0))
            mains_joueurs[0].append(mains_joueurs[1].pop(0))
        for i in range (2):
          mains_joueurs[0].append(mains_joueurs[0].pop(0))
          mains_joueurs[0].append(mains_joueurs[1].pop(0))
      fini = True
    elif valeur_carte(carte_joueur_1) < valeur_carte(carte_joueur_2):
      print("C'est " + joueurs[1] + " qui remporte la bataille")
      if iteration == 0:
        for j in range (3):
          mains_joueurs[1].append(mains_joueurs[0].pop(0))
          mains_joueurs[1].append(mains_joueurs[1].pop(0))
      else :
        for i in range(iteration):
          for j in range (3):
            mains_joueurs[1].append(mains_joueurs[0].pop(0))
            mains_joueurs[1].append(mains_joueurs[1].pop(0))
        for i in range (2):
          mains_joueurs[1].append(mains_joueurs[0].pop(0))
          mains_joueurs[1].append(mains_joueurs[1].pop(0))
      fini = True
    else :
      iteration = iteration + 1
  
#Fonction qui joue un coup
def jouer_coup():
  """
  Input : Aucun
  Output : Aucun (change les mains des joueurs comme il le faut après le coup)
  Effet : joue un coup
  """
  global mains_joueurs
  print("\n")
  print("Appuyez sur entrer ou entrez 'scores' pour voir le score ou entrez 'débloquer' suivi du nombre cartes à échanger (sans espaces)(5 si laissé vide)")
  reponse = input("- ")
  if reponse == "scores":
    print(joueurs[0] + " a " + str(len(mains_joueurs[0])) + " cartes et " + joueurs[1] + " a " + str(len(mains_joueurs[1])) + " cartes")
  if reponse[0:9] == "débloquer":
    if len(reponse) == 10:
      cartes_a_echanger = int(reponse[9])
    elif len(reponse) == 11:
      cartes_a_echanger = int(reponse[9] + reponse[10])
    else :
      cartes_a_echanger = 5
    for i in range (cartes_a_echanger):
      index1 = randint(0, len(mains_joueurs[0]) - 1)
      index2 = randint(0, len(mains_joueurs[1]) - 1)
      print("Les cartes " + mains_joueurs[0][index1] + " et " + mains_joueurs[1][index2] + " sont échangés")
      mains_joueurs[0][index1], mains_joueurs[1][index2] = mains_joueurs[1][index2], mains_joueurs[0][index1]
  carte_joueur_1 = mains_joueurs[0][0]
  carte_joueur_2 = mains_joueurs[1][0]
  print(joueurs[0] + " pose la carte : " + carte_joueur_1)
  print(joueurs[1] + " pose la carte : " + carte_joueur_2)
  if valeur_carte(carte_joueur_1) > valeur_carte(carte_joueur_2):
    print("C'est " + joueurs[0] + " qui remporte les cartes")
    mains_joueurs[0].append(mains_joueurs[0].pop(0))
    mains_joueurs[0].append(mains_joueurs[1].pop(0))
  elif valeur_carte(carte_joueur_1) < valeur_carte(carte_joueur_2):
    print("C'est " + joueurs[1] + " qui remporte les cartes")
    mains_joueurs[1].append(mains_joueurs[0].pop(0))
    mains_joueurs[1].append(mains_joueurs[1].pop(0))
  else :
    bataille()

#Joue des coups tant qu'il n'y a pas de vainqueur
while vainqueur == "":
  jouer_coup()
  check_victoire()

print(vainqueur + " a gagné ! Félicitations !")