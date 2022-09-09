import matplotlib.pyplot as plt
from PIL import Image
from pycocotools.coco import COCO

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="check coco")
    parser.add_argument("-f", "--file", type=str, required=True)
    parser.add_argument("-r", "--image-root", type=str, required=True)
    parser.add_argument("-o", "--out-file", type=str, default="demo.jpg")

    args = parser.parse_args()
    print(args)

    coco = COCO(args.file)
    imgids = coco.getImgIds()
    assert len(imgids) == 2

    fig, axs = plt.subplots(1, 2, figsize=(5, 5))
    for imgid, ax in zip(imgids, axs):
        plt.sca(ax)
        img = coco.loadImgs(imgid)[0]
        im = Image.open(args.image_root + img["file_name"])
        ax.imshow(im)
        ax.axis("off")
        annids = coco.getAnnIds(imgIds=[imgid])
        anns = coco.loadAnns(annids)
        coco.showAnns(anns, draw_bbox=True)
    plt.savefig(args.out_file, bbox_inches="tight")
