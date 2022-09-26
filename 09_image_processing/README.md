# Image Processing

### Resources
 - [basics](./image_basics.ipynb) (credits: Divyanshu Tak)
 - [scikit-image](https://scikit-image.org)
 - [open-cv](https://docs.opencv.org/4.x/d9/df8/tutorial_root.html)
 - [JupyterLab](../08_2d_visulization/)
 - [Official Python tools](https://github.com/cocodataset/cocoapi/tree/master/PythonAPI/pycocotools)

### Homework
 1. update your forked repo from my repo([ref](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork))
 1. following [01_git](../01_git/), create a new branch `LAST#_09imgproc` (ex: pan667_09imgproc) in your forked repo
 1. activate the environment you created in [03_conda](../03_conda/)
 1. create a notebook under `submissions` and name as `LAST#.ipynb`
 1. write your code to copy object 1 and 2 in img1 and paste to object 3 and 4 in img2
    - get the bounding boxes of the objects from the masks
    - crop the objects from img1 by bounding boxes
    - resize the cropped objects to target size (i.e. size of bounding boxes in img2)
    - paste the resized objects on img2
    - show the result image
 1. explore 5 different image processing teniques (for example, applying filters, segmentation, or edge detection) and show the results
    - use either opencv or scikit-image. Recently I love scikit-image because I think it's more pythonic. If you want to use scikit-image, follow their instruction to install. 
 1. stage changes, commit with the message "learning imgproc", push and submit a pr