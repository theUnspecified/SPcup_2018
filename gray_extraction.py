import cv2
import os
import numpy as np
from scipy.stats import skew
import pandas as pd
path1 = "./input/train/"
images = []
image_name = []
path_name = ['HTC-1-M7', 'LG-Nexus-5x', 'Motorola-Droid-Maxx']
def stats_moment(image):
        noise = image - cv2.fastNlMeansDenoising(image)
        b,g,r = cv2.split(noise)
        sb = cv2.meanStdDev(b)
        sg = cv2.meanStdDev(g)
        sr = cv2.meanStdDev(r)
        return np.ndarray.flatten(np.matrix.transpose(np.asarray([sr[0][0],sr[1][0],[skew(np.ravel(r))],sg[0][0],sg[1][0],[skew(np.ravel(g))],sb[0][0],sb[1][0],[skew(np.ravel(b))]])))


#path2 = "./input/train/HTC-1-M7/(HTC-1-M7)1.jpg"
#path3 = "./input/train/HTC-1-M7/(HTC-1-M7)2.jpg"
#print(np.asarray(stats_moment(cv2.imread(path2))))
#print(stats_moment(cv2.imread(path2)))

def load_images_from_folder(folder):
    c = 0 
    print(folder)          
    for filename in os.listdir(folder):
  #      print(stats_moment(cv2.imread(os.path.join(folder,filename))))
        images.append(stats_moment(cv2.imread(os.path.join(folder,filename))))
        image_name.append(filename)
        c = c + 1
        print(c)

 #       np.savetxt('HTC.csv', stats_moment(cv2.imread(os.path.join(folder,filename))),fmt='%.2f', delimiter='\t', header="m1,  s1,  sk1,  m2,  s2,  sk2,  m3,  s3,  sk3")
 #       images.update()


for folder in path_name:
	path = "./input/train/" + folder + "/"
	load_images_from_folder(path)
	name_df = pd.DataFrame(image_name)
	my_df = pd.DataFrame(images)
	my_df.to_csv(folder + '_noise'+'.csv', index=False, header=False)
	name_df.to_csv(folder+'_im_name' +'.csv', index=False, header=False)
	image_name = []
	images = []
