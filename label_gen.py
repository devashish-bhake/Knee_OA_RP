import os


def img2label0():
    root_dir = r"D:\kaggle_practice\Research_paper\knee_OA_dataset_2\images\0"
    label_dir = "D:\kaggle_practice\Research_paper\knee_OA_dataset_2\labels"
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.png'):
                img_name = file.split('.')[0]
                label_name = img_name + '.txt'
                with open(os.path.join(label_dir, label_name), 'w') as f:
                    f.write('0 0.5 0.5 1 1')


def img2label1():
    root_dir = r"D:\kaggle_practice\Research_paper\knee_OA_dataset_2\images\1"
    label_dir = "D:\kaggle_practice\Research_paper\knee_OA_dataset_2\labels"
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.png'):
                img_name = file.split('.')[0]
                label_name = img_name + '.txt'
                with open(os.path.join(label_dir, label_name), 'w') as f:
                    f.write('1 0.5 0.5 1 1')


def img2label2():
    root_dir = r"D:\kaggle_practice\Research_paper\knee_OA_dataset_2\images\2"
    label_dir = "D:\kaggle_practice\Research_paper\knee_OA_dataset_2\labels"
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.png'):
                img_name = file.split('.')[0]
                label_name = img_name + '.txt'
                with open(os.path.join(label_dir, label_name), 'w') as f:
                    f.write('2 0.5 0.5 1 1')


def img2label3():
    root_dir = r"D:\kaggle_practice\Research_paper\knee_OA_dataset_2\images\3"
    label_dir = "D:\kaggle_practice\Research_paper\knee_OA_dataset_2\labels"
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.png'):
                img_name = file.split('.')[0]
                label_name = img_name + '.txt'
                with open(os.path.join(label_dir, label_name), 'w') as f:
                    f.write('3 0.5 0.5 1 1')


def img2label4():
    root_dir = r"D:\kaggle_practice\Research_paper\knee_OA_dataset_2\images\4"
    label_dir = "D:\kaggle_practice\Research_paper\knee_OA_dataset_2\labels"
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.png'):
                img_name = file.split('.')[0]
                label_name = img_name + '.txt'
                with open(os.path.join(label_dir, label_name), 'w') as f:
                    f.write('4 0.5 0.5 1 1')

img2label0()

img2label1()

img2label2()

img2label3()

img2label4()