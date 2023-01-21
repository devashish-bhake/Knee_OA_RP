import os
import random
import shutil

root = r"D:\kaggle_practice\Research_paper\knee_OA_dataset_2"

test_set = r"D:\kaggle_practice\Research_paper\test_data.txt"
train_set = r"D:\kaggle_practice\Research_paper\train_data.txt"
val_set = r"D:\kaggle_practice\Research_paper\valid_data.txt"

train_path = r"D:\kaggle_practice\Research_paper\knee_OA_dataset_2\train\images"
train_label = r"D:\kaggle_practice\Research_paper\knee_OA_dataset_2\train\labels"
test_path = r"D:\kaggle_practice\Research_paper\knee_OA_dataset_2\test\images"
test_label = r"D:\kaggle_practice\Research_paper\knee_OA_dataset_2\test\labels"
val_path = r"D:\kaggle_practice\Research_paper\knee_OA_dataset_2\valid\images"
val_label = r"D:\kaggle_practice\Research_paper\knee_OA_dataset_2\valid\labels"


def createFileNamesSet():
    image_dir = r"D:\kaggle_practice\Research_paper\knee_OA_dataset_2\images"
    # print(os.listdir(image_dir))
    write_file = open("file_names.txt", "w")
    for filename in os.listdir(image_dir):
        to_write = filename.split('.')[0]
        # write all the info in the text file
        write_file.writelines(to_write)
        write_file.writelines("\n")
    write_file.close()


def createTrainingTestingValidData():
    f_input = open(r"D:\kaggle_practice\Research_paper\file_names.txt", "r")
    train = open(r"D:\kaggle_practice\Research_paper\train_data.txt", "w")
    test = open(r"D:\kaggle_practice\Research_paper\test_data.txt", "w")
    valid = open("valid_data.txt", "w")
    for line in f_input:
        r = random.random()
        if 0.0 <= r <= 0.7:
            train.write(line)
        elif 0.7 < r <= 0.9:
            valid.write(line)
        elif 0.9 < r <= 1.0:
            test.write(line)
    print()


def createTrainingSet():
    train_file = open(train_set, 'r')
    for line in train_file:
        for filename in os.listdir(os.path.join(root, "images")):
            if filename.rsplit('.', 1)[0] == line.strip():
                shutil.copy(os.path.join(os.path.join(root, "images"), filename), train_path)
                print("moved ", filename, " To training set")

        for filename in os.listdir(os.path.join(root, "labels")):
            if filename.rsplit('.', 1)[0] == line.strip():
                shutil.copy(os.path.join(os.path.join(root, "labels"), filename), train_label)


def createTestingSet():
    test_file = open(test_set, 'r')
    for line in test_file:
        for filename in os.listdir(os.path.join(root, "images")):
            if filename.rsplit('.', 1)[0] == line.strip():
                shutil.copy(os.path.join(os.path.join(root, "images"), filename), test_path)
                print("moved ", filename, " To testing set")
        for filename in os.listdir(os.path.join(root, "labels")):
            if filename.rsplit('.', 1)[0] == line.strip():
                shutil.copy(os.path.join(os.path.join(root, "labels"), filename), test_label)


def createValidationSet():
    val_file = open(val_set, 'r')
    for line in val_file:
        for filename in os.listdir(os.path.join(root, "images")):
            if filename.rsplit('.', 1)[0] == line.strip():
                shutil.copy(os.path.join(os.path.join(root, "images"), filename), val_path)
                print("moved ", filename, " To Validation set")
        for filename in os.listdir(os.path.join(root, "labels")):
            if filename.rsplit('.', 1)[0] == line.strip():
                shutil.copy(os.path.join(os.path.join(root, "labels"), filename), val_label)


# createFileNamesSet()
#
# createTrainingTestingValidData()

createTrainingSet()

createTestingSet()

createValidationSet()

# python D:\kaggle_practice\yolov5\detect.py --weights D:\kaggle_practice\yolov5\runs\train\exp5\weights\best.pt --img 224 --conf 0.25 --source D:\kaggle_practice\Research_paper\knee_OA_dataset_2\test\images

# python D:\kaggle_practice\yolov5\train.py --img 224 --batch 8 --epochs 30 --data D:\kaggle_practice\Research_paper\data.yaml --weights yolov5s.pt