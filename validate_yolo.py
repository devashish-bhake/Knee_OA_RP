# compare file names in images folder and labels folder
# if there is a file in images folder but not in labels folder, delete it
# if there is a file in labels folder but not in images folder, delete it

import os


def validate_yolo():
    ct = 0
    images = os.listdir('D:\kaggle_practice\Research_paper\knee_OA_dataset_2\images')
    labels = os.listdir('D:\kaggle_practice\Research_paper\knee_OA_dataset_2\labels')
    for image in images:
        if image[:-4] + '.txt' in labels:
            ct = ct+1
    if ct == len(images):
        print('All images have labels')

validate_yolo()