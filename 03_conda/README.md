# Conda

### Resources
 - [basic tutorials](https://astrobiomike.github.io/unix/conda-intro)
 - [official documents](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html)

### Homework
 1. update your forked repo from my repo([ref](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork))
 1. following [01_git](../01_git/), create a new branch `LAST#_03conda` (ex: pan667_03conda) in your forked repo
 1. install [miniconda](https://docs.conda.io/en/latest/miniconda.html) (This is preferable than Anaconda because it won't install unused packages.)
 1. create a conda virtual enviornment named py3.8 with Python version 3.8
 1. activate the created environment
 1. install pytorch and torchvision ([pytorch](https://pytorch.org))
 1. install [detectron2](https://github.com/facebookresearch/detectron2) with `git clone` and `pip install -e` (please find more information in their instruction and go check what `-e` means)
 1. install opencv
 1. run `python -m detectron2.utils.collect_env.py` and redirect the output to the file named LAST.#.txt under submissions (check [02_bash](../02_bash/) for redirection)
 1. stage changes, commit with the message "learning conda", push and submit a pr