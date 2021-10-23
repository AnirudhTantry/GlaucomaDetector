import cv2
import os
import random
def load_imgs(folder):
    images = []
    for file in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,file))
        if img is not None:
            images.append(img)
    return images

def noise_remov(img_list,f_pat):
    i=1
    for img in img_list:
        img_d=cv2.GaussianBlur(img,(5,5),0) #Applying Gaussian Blur with 5x5 kernel
        cv2.imwrite(f_pat+str(i)+'.jpg',img_d)
        i=i+1
        
pat2=r'C:\Users\Aniruddh\Desktop\FILTERED\NEGATIVE'
np_pat=r'C:\Users\Aniruddh\Desktop\BLURRED_NA\NORMAL\neg'
norm_list=load_imgs(pat2)
new_list=random.sample(norm_list,167)
noise_remov(new_list,np_pat)
print("DONE WITH NORMAL")
pat2=r'C:\Users\Aniruddh\Desktop\FILTERED\GLAUCOMATIC'
np_pat=r'C:\Users\Aniruddh\Desktop\BLURRED_NA\ABNORMAL\pos'
norm_list=load_imgs(pat2)
new_list=random.sample(norm_list,167)
noise_remov(new_list,np_pat)
print("DONE WITH ABNORMAL")
