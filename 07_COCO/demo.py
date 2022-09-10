import os

import matplotlib.pyplot as plt
from PIL import Image
from pycocotools.coco import COCO


def check_image(image):
    keys = list(image.keys())
    assert "id" in keys and isinstance(image["id"], int)
    assert "height" in keys and isinstance(image["height"], int)
    assert "width" in keys and isinstance(image["width"], int)
    assert "file_name" in keys and isinstance(image["file_name"], str)


def check_anns(anns):
    for ann in anns:
        keys = list(ann.keys())
        assert "id" in keys and isinstance(ann["id"], int)
        assert "image_id" in keys and isinstance(ann["image_id"], int)
        assert "category_id" in keys and isinstance(ann["category_id"], int)
        assert "segmentation" in keys and isinstance(ann["segmentation"], dict)
        assert "area" in keys and isinstance(ann["area"], float)
        assert "bbox" in keys and isinstance(ann["bbox"], list)
        assert "iscrowd" in keys and ann["iscrowd"] == 0


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
        check_image(img)
        im = Image.open(os.path.join(args.image_root, img["file_name"]))
        ax.imshow(im)
        ax.axis("off")
        annids = coco.getAnnIds(imgIds=[imgid])
        anns = coco.loadAnns(annids)
        check_anns(anns)
        coco.showAnns(anns, draw_bbox=True)
    plt.savefig(args.out_file, bbox_inches="tight")
