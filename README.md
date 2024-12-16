# geneLIGNEgraduee
geneLIGNEgraduee - Générateur de Lignes Graduées
Qu'est-ce que c'est ?
Cette application Python permet de créer des fichiers PDF personnalisés contenant des lignes graduées avec des cercles rouges placés aléatoirement. Elle est idéale pour générer des schémas ou des aides visuelles nécessitant des lignes numérotées et des repères visuels.

Installation :
Prérequis :

Python 3 installé sur votre système.
Installation des bibliothèques :

Utilisez pip pour installer les bibliothèques nécessaires :

Bash

pip install tkinter reportlab
Utilisation :
Téléchargement : Téléchargez le code source de ce projet.

Exécution : Ouvrez un terminal, naviguez jusqu'au répertoire où vous avez enregistré le code et exécutez la commande suivante :

Bash

python geneLIGNEgraduee.py
Interface graphique : Une fenêtre s'ouvre. Saisissez les valeurs souhaitées pour :

Le nombre de lignes à générer
La longueur de chaque ligne
Le nombre de cercles rouges par ligne
Génération du PDF : Cliquez sur le bouton "Générer PDF". Choisissez l'emplacement où vous souhaitez enregistrer votre fichier PDF.

Fonctionnalités :
Personnalisation : Contrôle total sur le nombre de lignes, leur longueur et la densité des cercles rouges.
PDF : Génération de fichiers PDF de haute qualité.
Graduations : Chaque ligne est graduée pour une référence facile.
Cercles aléatoires : Les cercles rouges sont placés aléatoirement sur les lignes, évitant les multiples de 5 et les doublons.
Licence :
Ce logiciel est distribué sous la licence GNU General Public License v3.0 (GPLv3). Cela signifie qu'il est libre d'utilisation, de modification et de redistribution, sous certaines conditions. Pour plus d'informations, consultez le fichier LICENSE.

Contribution :
N'hésitez pas à contribuer à ce projet ! Vous pouvez :

Corriger des bugs
Ajouter de nouvelles fonctionnalités
Améliorer la documentation
Pour cela, créez une demande de fusion (pull request) sur la plateforme d'hébergement du projet.

A propos des bibliothèques :
tkinter : Crée l'interface graphique de l'application.
random : Génère des nombres aléatoires pour la position des cercles.
reportlab : Permet de créer le fichier PDF avec ses éléments graphiques.
En résumé :
geneLIGNEgraduee est un outil simple et efficace pour générer des lignes graduées personnalisées. Il est idéal pour les étudiants, les enseignants, les chercheurs ou toute personne ayant besoin de schémas clairs et précis.

Note: Pour une meilleure compréhension du code, référez-vous aux commentaires présents dans le fichier Python.

Suggestions d'amélioration :

Interface utilisateur: Une interface graphique plus intuitive pourrait être développée.
Options supplémentaires: Possibilité d'ajouter d'autres formes géométriques, de personnaliser la couleur des éléments, etc.
Formats de sortie: Envisager d'exporter les résultats dans d'autres formats (PNG, SVG).
