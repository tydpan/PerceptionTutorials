# Docstring

### Resources
 - [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) section 3.8 Comments and Docstrings
 - [Tutorial for type hints](https://www.pythontutorial.net/python-basics/python-type-hints/)
 - [detectron2](https://github.com/facebookresearch/detectron2/tree/cbbc1ce26473cb2a5cc8f58e8ada9ae14cb41052), see how they did

### Homework
 1. update your forked repo from my repo([ref](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork))
 1. following [01_git](../01_git/), create a new branch `LAST#_05doc` (ex: pan667_05doc) in your forked repo
 1. activate the environment you created in [03_conda](../03_conda/)
 1. copy the file `code.py` to `submissions/` and rename it as `LAST#.py`
 1. read the function in the file `LAST#.py`, add proper doc string with googledoc style, and add proper type hints
 1. run `black` with line length 100, `isort`, and `flake8` on the file
 1. stage changes, commit with the message "learning doc", push and submit a pr