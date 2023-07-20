# Ici, nous utilisons la methode path de la bibliothèque pathlib pour l'arborescence

from pathlib import Path
from git import Repo 

def creer_arborescence2():
    # Créer les répertoires 
    Path('data/cleaned').mkdir(parents=True, exist_ok=True)
    Path('data/raw').mkdir(parents=True, exist_ok=True)
    Path('docs').mkdir(parents=True, exist_ok=True)
    Path('models').mkdir(parents=True, exist_ok=True)
    Path('notebooks').mkdir(parents=True, exist_ok=True)
    Path('reports').mkdir(parents=True, exist_ok=True)
    Path('src').mkdir(parents=True, exist_ok=True)

    # Créer les files
    with open('LICENSE', 'w') as f:
        f.write('Votre license')

    with open('Makefile', 'w') as f:
        f.write('Votre Makefile')

    with open('notebooks/main_notebook.ipynb', 'w') as f:
        f.write('Votre notebook principal')

    with open('README.md', 'w') as f:
        f.write('Votre readme file')

    with open('requirements.txt', 'w') as f:
        f.write('Vos requirements')

    with open('src/utils.py', 'w') as f:
        f.write('Vos fonctions utils')

def initialiser_repo():
    repo = Repo.init('.')
    repo.index.add(['data', 'docs', 'LICENSE', 'Makefile', 'models', 'notebooks', 'README.md', 'reports', 'requirements.txt', 'src'])
    repo.index.commit('Initial commit')


if __name__ == '__main__':
    creer_arborescence2()
    initialiser_repo()


