import cv2
import os

def ext_ocd(img_list,fpat):
    
 i=1
 for img in img_list:
    
    try:
        
        img_re=cv2.resize(img,(256,256)) #Resize image
        gray=cv2.cvtColor(img_re,cv2.COLOR_BGR2GRAY) # Convert from RGB to Grayscale
        blur=cv2.GaussianBlur(gray,(5,5),0) # Smoothen image
        [miv,mav,mil,mal]=cv2.minMaxLoc(blur) # Find brightest region
        [x,y]=mal # Centre of brightest region
        img_r=img_re[y-40:y+40,x-40:x+40] # Extracting area around brightest region
        img_rs=cv2.resize(img_r,(256,256)) # Resizing that extracted area
        img_final=cv2.GaussianBlur(img_rs,(5,5),0) # Denoising image
        cv2.imwrite(fpat+str(i)+'.jpg',img_final) # Saving image
    except Exception as e:
         print(str(e)) # Error handling
    i=i+1
def load_imgs(folder):
    images = []
    for file in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,file)) # Accessing each image
        if img is not None:
            images.append(img) # Creating list of images
    return images

g_pat=r'C:\Users\Aniruddh\Desktop\OPTIC_DISC\NORMAL\n_disc';
s_pat=r'C:\Users\Aniruddh\Desktop\ORIGINAL_FUNDUS_DATASET\NORMAL_EYES'
ext_ocd(load_imgs(s_pat),g_pat)
print("Done with normal")
g_pat=r'C:\Users\Aniruddh\Desktop\OPTIC_DISC\GLAUCOMATIC\g_disc';
s_pat=r'C:\Users\Aniruddh\Desktop\ORIGINAL_FUNDUS_DATASET\GLAUCOMATIC_EYES'
ext_ocd(load_imgs(s_pat),g_pat)
print("Done with glaucomatic")

