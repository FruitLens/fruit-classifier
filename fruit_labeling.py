import os
import cv2 as cv

def group_imgs():
    dataset = r"../dataset_pca_50/"
    count = 0
    for folder in os.listdir(dataset):
        data_dir = r"{}/{}".format(dataset, folder)
        for img_class in os.listdir(data_dir):
            for idx, img in enumerate(os.listdir(os.path.join(data_dir, img_class))):
                if img.startswith('.'):
                    continue
                img_path = os.path.join(data_dir, img_class, img)
                try:
                    img_read = cv.imread(img_path)
                    # new_img = pca_fit(img_read) * 255
                    
                    # name_file_class = ''
                    # if img_class == 'apple':
                    #     name_file_class = 'a'
                    # elif img_class == 'orange':
                    #     name_file_class = 'o'
                    # elif img_class == 'banana':
                    #     name_file_class = 'b'
                    
                    new_name =  f'IMG{str(idx + 1 + count).zfill(4)}.jpg'
                    # if (idx == 2):
                    #     break
                    cv.imwrite(r"./grouped_banana/{}".format(new_name), img_read)
                except Exception as e:
                    print(e)
                    print("issue with image {}".format(img_path))

            print("Classe {} concluída para {}".format(img_class, folder))
            count = count + len(os.listdir(os.path.join(data_dir, img_class)))
    
    generate_labels_file("./labels/images_with_labels.txt")

def generate_labels_file(file_name):
    data_dir = r'./grouped_banana'

    with open(file_name, 'w') as labels_file:
        for file in os.listdir(data_dir):
            labels_file.write(file + ',\n')

# group_imgs()
generate_labels_file("./grouped_banana/labels/images_with_labels.txt")
# generate_labels_file('train', 'train_labels.txt')
# group_imgs('test')
# generate_labels_file('test', 'test_labels.txt')

# total images should be 1958