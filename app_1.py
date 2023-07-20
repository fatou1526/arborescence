# Dans ce script, nous utilisons, la bibliothèque os pour créer l'arborescence
import os
import shutil
from git import Repo 

def creer_arborescence():
    # Créer les répertoires
    os.makedirs('data/cleaned')
    os.makedirs('data/raw')
    os.makedirs('docs')
    os.makedirs('models')
    os.makedirs('notebooks')
    os.makedirs('reports')
    os.makedirs('src')

    # Créer les files
    with open('LICENSE','w') as f:
        f.write('Votre license')

    with open('Makefile','w') as f:
        f.write('Vos règles Make')    

    with open('notebooks/main_notebook.ipynb','w') as f:
        f.write('Votre notebook principal')

    with open('README.md','w') as f:
        f.write('Votre readme file')

    with open('requirements.txt','w') as f:
        f.write('Vos requirements')

    with open('src/utils.py','w') as f:
        f.write('Vos fonctions utils')

def initialiser_repo():
    repo = Repo.init('.')
    repo.index.add(['data', 'docs', 'LICENSE', 'Makefile', 'models', 'notebooks', 'README.md', 'reports', 'requirements.txt', 'src'])
    repo.index.commit('Initial commit')

if __name__ == '__main__':
    creer_arborescence()
    initialiser_repo()

