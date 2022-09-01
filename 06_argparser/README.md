# Argparser

### Resources
 - [argparser](https://docs.python.org/3/library/argparse.html)
 - [detectron2](https://github.com/facebookresearch/detectron2/blob/cbbc1ce26473cb2a5cc8f58e8ada9ae14cb41052/detectron2/engine/defaults.py#L82), see how they did
 
### Homework 
 1. update your forked repo from my repo([ref](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork))
 1. following [01_git](../01_git/), create a new branch `LAST#_06arg` (ex: pan667_06arg) in your forked repo
 1. activate the environment you created in [03_conda](../03_conda/)
 1. copy the file `code.py` to `submissions/` and rename it as `LAST#.py`
 1. open the file, add arguments for `mode` and `pow`, set proper values for `type`, `default`, `help`, and `metavar`
 1. add an argument named `print_hello` which `action` is `store_true`
 1. run `python LAST#.py -h` to see the arguments you created
 1. run `python LAST#.py` and test with different argument values to see if it works properly
 1. run `black` with line length 100, `isort`, and `flake8` on the file
 1. stage changes, commit with the message "learning arg", push and submit a pr

