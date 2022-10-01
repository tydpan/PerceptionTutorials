# PEP8

### Resources
 - [PEP8](https://peps.python.org/pep-0008/#inline-comments)
 - [flake8](https://flake8.pycqa.org/en/latest/index.html)
 - [black](https://black.readthedocs.io/en/stable/)
 - [isort](https://pycqa.github.io/isort/)


### Homework
 1. update your forked repo from my repo([ref](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork))
 1. following [01_git](../01_git/), create a new branch `LAST#_04pep8` (ex: pan667_04pep8) in your forked repo
 1. activate the environment you created in [03_conda](../03_conda/)
 1. install [flake8](https://flake8.pycqa.org/en/latest/index.html), [black](https://black.readthedocs.io/en/stable/), and [isort](https://pycqa.github.io/isort/)
 1. take a look at file `setup.cfg` and try to understand each setting for `flake8`
 1. copy the file `code.py` to `submissions/` and rename it as `LAST#.py`
 1. run flake8 on `LAST#.py` and you will see some warnings
 1. In the warnings, you should see line 33, 34, and 35 are too long. Open `LAST#.py` and you should see these three lines correspond to three dummy lists (if you use `vim` to open the file, type `:set nu` to show the line numbers).  Now add something on these three lines to make `flake8` ignore them. Save the file and run `flake8` again, you should see the warnings are gone. 
 1. run `black --help` and go through the meaning of each option (flag)
 1. run `black` with `diff` and `color` flag and set the line length to 100. These two flags will show the difference without making modification yet. You should see `black` is trying to fix three dummy lists again. Open `LAST#.py` and add something on these three lines to make `black` ignore them. Save the file and run `black` with same flags again, you should see they are ignored. 
 1. run `black` with line length 100 on the file to make modificatoin in place
 1. run `flake8` again and you should see some warnings were fixed by `black`
 1. take a look at file `setup.cfg` and try to understand each setting for `isort`
 1. run `isort` with flag `diff` to review the modification first and run `isort` again to modify the file in place (similar to `black`)
 1. run `flake8` again and you should still see some warnings. This means `black` and `isort` can't fix everything. 
 1. fix the code yourself unitil flake8 shows no warnings
 1. finally run `black` with line length 100, `isort`, and `flake8` again because you may touch something in the previous step
 1. stage changes, commit with the message "learning pep8", push and submit a pr