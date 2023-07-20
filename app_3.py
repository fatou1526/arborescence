# Ici, les methods mkdir et write_text de la bibliothèque pathlib sont utilisés
from pathlib import Path
from git import Repo 

def creer_arborescence3():
    # Créer les répertoires 
    Path('data/cleaned').mkdir(parents=True, exist_ok=True)
    Path('data/raw').mkdir(parents=True, exist_ok=True)
    Path('docs').mkdir(parents=True, exist_ok=True)
    Path('models').mkdir(parents=True, exist_ok=True)
    Path('notebooks').mkdir(parents=True, exist_ok=True)
    Path('reports').mkdir(parents=True, exist_ok=True)
    Path('src').mkdir(parents=True, exist_ok=True)

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