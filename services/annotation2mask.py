from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import json
import cv2

plt.rcParams['savefig.dpi'] = 130


def annotation2mask(annotations_path, images_path, result_path):
    annotationsFile = annotations_path
    coco = COCO(annotationsFile)

    # display COCO categories and supercategories
    cats = coco.loadCats(coco.getCatIds())
    nms = [cat['name'] for cat in cats]
    print('COCO categories: \n{}\n'.format(' '.join(nms)))

    nms = set([cat['supercategory'] for cat in cats])
    print('COCO supercategories: \n{}'.format(' '.join(nms)))

    catIds = coco.getCatIds(catNms=['person'])

    for i in coco.getImgIds():
        img = coco.loadImgs(i)[0]

        I = io.imread(
            "{images_path}/{file_name}".format(images_path=images_path, file_name=img['file_name']))
        h, w, _ = I.shape
        print(str(h), str(w))
        plt.subplots(figsize=(w/100, h/100))
        plt.imshow(I)
        plt.axis('off')

        annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
        anns = coco.loadAnns(annIds)
        coco.showAnns(anns)

        plt.savefig("{result_path}/{file_name}".format(result_path=result_path,
                    file_name=img['file_name']), bbox_inches='tight', pad_inches=0)
        plt.close()
        pass
