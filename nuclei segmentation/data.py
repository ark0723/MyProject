
# coding: utf-8

# In[1]:


from __future__ import print_function
from PIL import Image
import os
import numpy as np
import glob


# In[2]:


class dataProcess(object):

    def __init__(self, out_rows, out_cols, data_path = 'train/gray_resized_image', label_path = "train/label", test_path = "test/gray_resized_image",                      img_type = "png"):

        self.out_rows = out_rows
        self.out_cols = out_cols
        self.data_path = data_path
        self.label_path = label_path
        self.img_type = img_type
        self.test_path = test_path

    def create_train_data(self):
        images = os.listdir(self.data_path +'/.')
        total = len(images)

        train_image_path = self.data_path + "/{}." + self.img_type
        train_mask_path = self.label_path + "/{}." + self.img_type

        imgs = np.ndarray((total, self.out_rows, self.out_cols), dtype=np.uint8)
        imgs_mask = np.ndarray((total, self.out_rows, self.out_cols), dtype=np.uint8)

        print('-'*30)
        print('Creating training images...')
        print('-'*30)

        for i in range(total):
            im = Image.open(train_image_path.format(i+1))
            mask = Image.open(train_mask_path.format(i+1))
            im = np.array(im)
            im_mask = np.array(mask)

            imgs[i] = im
            imgs_mask[i] = im_mask

        print('Loading done.')

        np.save('imgs_train.npy',imgs)
        np.save('imgs_mask_train.npy', imgs_mask)
        print('Saving to .npy files done.')

    def load_train_data(self):
        imgs_train = np.load('imgs_train.npy')
        imgs_mask_train = np.load('imgs_mask_train.npy')
        
        return imgs_train, imgs_mask_train


    def create_test_data(self):
        images = os.listdir(self.test_path +'/.')
        total = len(images)

        test_image_path = self.test_path + "/{}." + self.img_type

        imgs = np.ndarray((total, self.out_rows, self.out_cols), dtype=np.uint8)
        imgs_id = np.ndarray((total, ), dtype=np.int32)

        i = 0
        print('-'*30)
        print('Creating test images...')
        print('-'*30)


        for i in range(total):
            img_id = int(i+1)
            im = Image.open(test_image_path.format(i+1))
            im = np.array(im)

            imgs[i] = im
            imgs_id[i] = img_id
        print('Loading done.')

        np.save('imgs_test.npy', imgs)
        np.save('imgs_id_test.npy', imgs_id)
        print('Saving to .npy files done.')

    def load_test_data(self):
        imgs_test = np.load('imgs_test.npy')
        imgs_id = np.load('imgs_id_test.npy')
        
        return imgs_test, imgs_id


# In[3]:


if __name__ == '__main__':
    myprocess = dataProcess(256,256)
    myprocess.create_train_data()
    myprocess.create_test_data()

