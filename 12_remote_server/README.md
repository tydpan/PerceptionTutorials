# Remote Server

# Resources
[Ohio Supercomputer Center (OSC)](https://www.osc.edu)

# Homework
1. Register an account on OSC with my invitation to the project
1. connect to the server via ssh by `ssh -X -L 8888:localhost:8888 ACCOUNT@owens.osc.edu`
    - `-X`: X11 forwarding
    - `-L 8888:localhost:8888`: port forwarding
    - For Windows users, you can eitehr use WSL or PuTTY (please check it out yourself)
    - You can also use OSC OnDemand
1. Type `module avail` for available libraries or tools on the server. For ML/DL development, we need cuda for Nvidia GPUs. Find the cuda version you want and load it with `module load XXX`. Here I suggest cuda-10.2 which is a stable version and works well with multiple version of PyTorch. Later you can put this command in `~/.bashrc` to load it automatically when logging on the server. 
1. Conda setup
    - install [miniconda](https://docs.conda.io/en/latest/miniconda.html)
    - create a conda virtual enviornment named py3.8 with Python version 3.8
    - activate the created environment
    - install pytorch and torchvision ([pytorch](https://pytorch.org))
    - install [detectron2](https://github.com/facebookresearch/detectron2) with `git clone` and `pip install -e` (please find more information in their instruction and go check what `-e` means)
    - You can put `conda activate XXX` in `~/.bashrc` to activate specific environment automatically when logging on the server. 
1. Now navigate to `/fs/ess/scratch/PAS2119/OSCCompetition` and create a folder named `LAST.#`
    - Note `/fs/ess/scratch/PAS2119/` is the place you put large files like datasets. OSC will remove and clean the unused files stored here. Later we will just call it `scratch`. 
    - We have project folder at `/fs/ess/PAS2119/`. This is the place you keep important files like codes and models. We have limited space, so do not put large files here unless you get permssion from the team leads. 
1. run `python -m detectron2.utils.collect_env` and redirect the output to the file named `LAST.#.txt` under the foler you created
1. now go back to the local computer and navigate to your forked repo of this repo, update to the latest([ref](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork)), create a new branch `LAST#_12osc`
1. open another window on local computer and use `scp` to download the `LAST.#.txt` to `submissions`
1. open the file locally and append a line "LAST.# says this is on local." at the end of the file
1. stage changes, commit with the message "learning OSC", push and submit a pr

# Supplementary
- Interactive nodes request: type `srun --account=PAS2119 --time=00:30:00 --nodes=1 --ntasks-per-node=1 --gpus-per-node=1 --pty /bin/bash` to request an interactive node. This is usefull when you are debugging your code or doing just inference. type `nvidia-smi` to verify you got GPUs after getting on the requested nodes. 
    - `--time=00:30:00`: request for 30 minutes
    - `--nodes=1`: request for 1 node
    - `--gpus-per-node=1`: request 1 gpu per node
- JupyterLab: type `jupyter lab --no-browser --port=8888` and copy the link to your local browser
    - `port`: it should be aligned with the port you set with `ssh`

 # Suggestions
- For Mac users: iterm2 + tmux + vscode
- For Windoes users: WSL + tmux + vscode
- [Some of my personal setup](https://github.com/tydpan/env_setup)