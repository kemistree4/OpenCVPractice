import cv2
import numpy as np
import os
import matplotlib
from PIL import Image

#Load image in grayscale

background_img_path = '/media/kemistree4/SP PHD U3/Bug_pics/Neat_horse'
foreground_img_path = '/home/kemistree4/code/OpenCVPractice/TransparentImage.png'
img_bkgd = cv2.imread(background_img_path)
img_frgd = cv2.imread(foreground_img_path)

background_lst = []

# Make a list of file paths for photos
for filename in os.listdir(background_img_path):
    background_lst.append(background_img_path + "/" + filename)

# Set empty list meant to hold arrays
array_list = []

# Iterate through list of photo filepaths and convert each to grayscale. Add that 2D array 
# to the list of arrays

for filepath in background_lst:
    array = cv2.cvtColor(cv2.imread(filepath), cv2.COLOR_BGR2GRAY)
    array_list.append(array)

# Calculate a sum of all arrays in list and dividee by the length of the list to get mean array
sum_array = np.sum(array_list, axis=0)
mean_array = np.uint8(np.divide(sum_array, len(array_list)))

# Show mean image
#matplotlib.pyplot.imshow(mean_array)

# Import grayscale foreground
gray_frgd = cv2.cvtColor(img_frgd, cv2.COLOR_BGR2GRAY)

# Assign background shape to variable
bkgd_size = mean_array.shape

# Resize foreground to fit size of background variable
resized_foreground = cv2.resize(gray_frgd, dsize=(bkgd_size[1],bkgd_size[0]), interpolation=cv2.INTER_CUBIC)

images = np.array(array_list)

#Shows any differences between the mean value and the last image. Can be used on any still of from the video
dif_image = images[-1].astype(int) - mean_array.astype(int)

#Finds the minimum pixel value in the array
dif_image.min()

# brings the minimum pixel value back up to 0
dif_image = dif_image - dif_image.min()

# Shows difference image
matplotlib.pyplot.imshow(dif_image, cmap='gray')

