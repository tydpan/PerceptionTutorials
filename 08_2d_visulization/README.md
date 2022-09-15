# 2D Visualization
*Note: images and annotations in this tutorial are modified from COCO dataset.*

### Resources
 - [JupyterLab](https://jupyter.org/try)
 - [Official Python tools](https://github.com/cocodataset/cocoapi/tree/master/PythonAPI/pycocotools)

### Homework
 1. update your forked repo from my repo([ref](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork))
 1. following [01_git](../01_git/), create a new branch `LAST#_08vis2d` (ex: pan667_08vis2d) in your forked repo
 1. activate the environment you created in [03_conda](../03_conda/)
 1. install jupyterlab
 1. copy `sample.ipynb` to `submissions` and rename it as `LAST#.ipynb`
 1. start jupyterlab, it should open a window in your browser. open your `LAST#.ipynb`
 1. write your code to plot bounding boxes, masks, and texts, as shown in the sample, using the `annotatoins.txt` (similar to [07_COCO](../07_COCO/))
    - do not use showanns in pycocotools; plot it yourself with matplotlib
    - for boxes, you can use matplotlib.patches.Rectangle
    - for masks, you can create mask images with transparency and overlay with the original image
    - for texts, you can use ax.text. align text and box at the center
 1. stage changes, commit with the message "learning vis2d", push and submit a pr
