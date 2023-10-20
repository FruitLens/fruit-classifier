import os
import cv2 as cv

labels = ['raw', 'unripe', 'ripe', 'overripe', 'rotten']

def group_images(file):
    with open(file) as f:
        lines = f.readlines()

        # count = 0
        for line in lines:
            (img_name, index) = line.split(',')
            label = labels[int(index)]

            img_file = cv.imread(r"./grouped_banana/{}".format(img_name))
            cv.imwrite(r"./fruits_dataset/{}/{}".format(label, img_name), img_file)
            # count = count + 1
            # if (count == 2):
            #     break

def show_total_images_per_label():
    for label in labels:
        files = os.listdir(r'./fruits_dataset/{}'.format(label))
        print('{}: {}'.format(label, len(files)))

# group_images('./grouped_banana/labels/images_with_labels.txt')
show_total_images_per_label()