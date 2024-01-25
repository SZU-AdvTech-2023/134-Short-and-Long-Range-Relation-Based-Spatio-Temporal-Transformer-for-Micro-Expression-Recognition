import os
from os.path import join
DIR_DATA = "../preprocess/databases"
data_folder = join(DIR_DATA, 'samm', 'data')

for dir1 in os.listdir(data_folder):
    # print("dir1: ", dir1)
    for dir2 in os.listdir(join(data_folder, dir1)):
        # print("dir2: ", dir2)
        for file in os.listdir(join(data_folder, dir1, dir2)):
            original_file = join(data_folder, dir1, dir2, file)
            print('original_file:', original_file)
            t1 = file.split('.')[0].split('_')[0]
            t2 = file.split('.')[0].split('_')[1].zfill(5)
            t = t1 + '_' + t2 + '.jpg'
            new_file = join(data_folder, dir1, dir2, t)
            print('new_file:', new_file)

            os.rename(original_file, new_file)


