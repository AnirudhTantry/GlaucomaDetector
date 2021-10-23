import os
import cv2
import random

def load_imgs(folder):
    images = []
    for file in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,file))
        if img is not None:
            images.append(img)
    return images

def flip_and_rot(fin_pat,img,n):
    f_nam=str(n)+'.jpg' 
    img_loco=fin_pat+'orig'
    cv2.imwrite(img_loco+f_nam,img) # Saving original image 
    img_loch=fin_pat+'hflip'
    h_img=cv2.flip(img,1) # Horizontally flipping image
    cv2.imwrite(img_loch+f_nam,h_img)
    img_locv=fin_pat+'vflip'
    v_img=cv2.flip(img,0) # Vertically flipping image
    cv2.imwrite(img_locv+f_nam,v_img)
    rc_img=cv2.rotate(img,cv2.cv2.ROTATE_90_CLOCKWISE) # Rotating image by 90 degrees clockwise
    glauc_locrc=fin_pat+'rotcra'
    cv2.imwrite(glauc_locrc+f_nam,rc_img)
    ra_img=cv2.rotate(img,cv2.cv2.ROTATE_90_COUNTERCLOCKWISE) # Rotating image by 90 degrees anticlockwise
    glauc_locra=fin_pat+'rotara'
    cv2.imwrite(glauc_locra+f_nam,ra_img)
    
def augment_img(aug_pat,img_list):
    i=1
    for img in img_list:
        flip_and_rot(aug_pat,img,i)
        i=i+1

glauc_loc=r'C:\Users\Aniruddh\Desktop\FILTERED\GLAUCOMATIC'
gaug_pat=r'C:\Users\Aniruddh\Desktop\AUGMENTED_DATASET\GLAUCOMATIC_EYES\g_'
glauc_list=load_imgs(glauc_loc)
augment_img(gaug_pat,glauc_list)
print("Done with Augmentation of Glaucomatic Dataset")
norm_loc=r'C:\Users\Aniruddh\Desktop\FILTERED\NEGATIVE'
naug_pat=r'C:\Users\Aniruddh\Desktop\AUGMENTED_DATASET\NORMAL_EYES\n_'
norm_list=load_imgs(norm_loc)
us_norm_list=random.sample(norm_list,167) # To make number of images in both classes close to each other
augment_img(naug_pat,us_norm_list)
print("Done with Augmentation of Negative Dataset")



