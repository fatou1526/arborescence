# Ici, les methodes path, mkdir et write_text de la bibliothèque pathlib pour l'arborescence

from pathlib import Path
from git import Repo 

def creer_arborescence3():
    # Créer les répertoires 
    Path('data/cleaned').write_text('Vos cleaned données')
    #Path('data/raw').write_text("Vos raw data")
    Path('docs').write_text("Vos documents")
    Path('models').write_text("Vos modeles")
    Path('notebooks').write_text("Vos notebooks")
    Path('reports').write_text("Vos rapports")
    Path('src').write_text("Vos fonctions sources")

    # Créer les files

    Path('LICENSE').write_text('Votre license')

    Path('Makefile').write_text('Votre Makefile')

    Path('notebooks/main_notebook.ipynb').write_text('Votre notebook principal')

    Path('README.md').write_text('Votre readme file')

    Path('requirements.txt').write_text('Vos requirements')

    Path('src/utils.py').write_text('Vos fonctions utils')

def initialiser_repo():
    repo = Repo.init('.')
    repo.index.add(['data', 'docs', 'LICENSE', 'Makefile', 'models', 'notebooks', 'README.md', 'reports', 'requirements.txt', 'src'])
    repo.index.commit('Initial commit')


if __name__ == '__main__':
    creer_arborescence3()
    initialiser_repo()