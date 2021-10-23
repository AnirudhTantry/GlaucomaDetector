import os
import cv2
from sklearn.model_selection import train_test_split
def load_imgs(folder):
    images = []
    for file in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,file))
        if img is not None:
            images.append(img)
    return images
def write_img(ilist,fpat):
    i=1
    for img in ilist:
        cv2.imwrite(fpat+str(i)+'.jpg',img)
        i=i+1
neg_list=load_imgs(r'C:\Users\Aniruddh\Desktop\BLURRED_NA\NEGATIVE')
pos_list=load_imgs(r'C:\Users\Aniruddh\Desktop\BLURRED_NA\POSITIVE')
pos_train,pos_test=train_test_split(pos_list,train_size=0.8,test_size=0.2) # To divide images into 2 parts 80 percent train and 20 percent test
neg_train,neg_test=train_test_split(neg_list,train_size=0.8,test_size=0.2)
write_img(pos_train,r'C:\Users\Aniruddh\Desktop\FINAL_DATASET_NA\TRAIN\POSITIVE\train_p')
write_img(pos_test,r'C:\Users\Aniruddh\Desktop\FINAL_DATASET_NA\TEST\POSITIVE\test_p')
write_img(neg_train,r'C:\Users\Aniruddh\Desktop\FINAL_DATASET_NA\TRAIN\NEGATIVE\train_n')
write_img(neg_test,r'C:\Users\Aniruddh\Desktop\FINAL_DATASET_NA\TEST\NEGATIVE\test_n')
print("DONE")
