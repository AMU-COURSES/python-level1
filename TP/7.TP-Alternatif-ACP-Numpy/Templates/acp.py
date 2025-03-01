# -*- coding: utf-8 -*-
""" Module de calcul le l'ACP de la base Iris

@author: Arrivault
"""

import numpy as np
import numpy.linalg as linalg
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def acp(X, k=-1):
    """ Calcule l'ACP de X

    Args:
        X - array2d - Matrice des données array(nbelem,nbattr)
        k - int - Nombre de dimensions à garder (0 < k <= nbatrr)
    Retourne:
        array2d - Y la projection de X sur les nouveaux axes de l'ACP
    """
    pass
    
def calc_Xc(X):
    """ Calcule les données centrées
    
    Args:
        X - array2d - Matrice des données array(nbelem,nbattr)
    Retourne:
        array2d - Xc = X - means (moyennes des attributs : array(nbattr))
    """
    pass

def calc_Sigma(Xc):
    """ Calcule la matrice de diffusion

    Args:
        Xc - array2d - Matrice des données centrées array(nbelem,nbattr)
    Retourne:
        array2d - Sigma = Xc.T * Xc
    """
    pass

def calc_eigen(Sigma):
    """ Calcule les valeurs et vecteurs propres de Sigma 
    
    Args:
        Sigma - array2d - Matrice de diffusion
    Retourne:
        (array1d, array2d) - Tuple (ValP, VectP) valeurs propres,
        vecteurs propres.    
    """
    # Sigma est symétrique : on utilse la méthode linalg.eigh()
    pass

def sort_eigen(ValP, VectP):
    """ Trie les vecteurs et valeurs propres par ordre decroissant des
    valeurs absolues

    On utilise ici la fonction np.argsort(A) qui renvoie les tableaux des
    indices de A trié par ordre croissant.
    
    Args:
        array1d - ValP - valeurs propres.
        array2d - VectP - vecteurs propres.
    Retourne:
        (array1d, array2d) - Tuple (ValP, VectP) valeurs propres,
        vecteurs propres triés.    
    """
    pass

def reduction(VectP, k):
    """ Reduit le nombre de dimensions aux k plus informatives

    Args:
        array2d - VectP - vecteurs propres triés.
        int - k - nombre de dimensions à garder (0 < k <= nbatrr)
    Retourne:
        array2d - Matrice de projection W
    """
    pass

def projection(Xc, W):
    """ Projette X sur les nouveaux axes
    
    Args:
        Xc - array2d - Matrice des données centrées array(nbelem,nbattr)
        W - array2d - Matrice de projection W
    Retourne:
        array2d - Y = Xc * W
    """
    pass

def test_polynome_caracteristique(ValP, VectP, Sigma):
    """ Test si Sigma*V - lambda*V = 0
    
    Args:
        Sigma - array2d - Matrice de diffusion
        array1d - ValP - valeurs propres.
        array2d - VectP - vecteurs propres.
   
    Retourne
        boolean - vrai si le test est vérifié, faux sinon    
    """
    pass

def affichage_nuage_couleur_acp(X, C, acp=False):
    """ Affiche les données de la matrice X (3 première colonnes) sous forme d'un nuage de points
        3D en mettant l'information de classe contenue dans le vecteur C en couleur.

    Args:
        X - array2d - Matrice contenant les mesures pour chaque iris
        C - array1d - Vecteur contenant le numéro de la classe pour chaque iris
    """
    fig = plt.figure()

    cl1 = (C == 0)
    cl2 = (C == 1)
    cl3 = (C == 2)

    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X[cl1, 0], X[cl1, 1], X[cl1, 2], c='b')
    ax.scatter(X[cl2, 0], X[cl2, 1], X[cl2, 2], c='r')
    ax.scatter(X[cl3, 0], X[cl3, 1], X[cl3, 2], c='g')
    title = "Nuage des points de X"
    if acp:
        title += " après ACP"
    ax.set_title(title)

    plt.show()
 
if __name__ == '__main__':
    from sklearn import datasets
    iris = datasets.load_iris()
    X = iris.data
    C = iris.target
    # Affichage du nuage de points
    affichage_nuage_couleur_acp(X, C)

    # Décommentez la suite quand l'implémentation est terminée:

    # # Calcule l'ACP
    # k = 4
    # Y = acp(X, k)
    # # Affichage du nuage de points
    # affichage_nuage_couleur_acp(Y, C, True)
    # # comparing result with sklearn.decomposition.PCA
    # from sklearn.decomposition import PCA
    # pca = PCA(n_components=k)
    # pca.fit(X)
    # skY = pca.transform(X)
    # if np.allclose(np.fabs(Y), np.fabs(skY)):
    #     print("ACP identique à celle de scikit-learn!")
    # else:
    #     print("Oups, il semble y avoir un souci...")