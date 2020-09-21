# Standard imports

import cv2 
import numpy as np 
  
# Load image 
image = cv2.imread(r"/home/kemistree4/code/Deep-Neural-Network/group-dead-flies.jpg", cv2.IMREAD_GRAYSCALE) 

# Set our filtering parameters 

# Initialize parameter settiing using cv2.SimpleBlobDetector 
params = cv2.SimpleBlobDetector_Params() 
  
# Set Area filtering parameters 
params.filterByArea = True
params.minArea = 45 
#params.maxArea = 100 

# Set Thresholds range 
params.minThreshold = 20
#params.maxThreshold = 255

# Set Circularity filtering parameters 
params.filterByCircularity = True
params.minCircularity = 0.2
#params.maxCircularity = 1

# Set Convexity filtering parameters 
params.filterByConvexity = True
params.minConvexity = 0.2
#params.maxConvexity = 0.5
      
# Set Inertia filtering parameters 
params.filterByInertia = True
params.minInertiaRatio = 0.01
#params.maxInertiaRatio = 1

#Checks OpenCV version and instantiates blob detector accordingly
print(cv2.__version__)

if cv2.__version__.startswith('2.'):
    detector = cv2.SimpleBlobDetector(params)
else:
    detector = cv2.SimpleBlobDetector_create(params)   
      
# Detect blobs 
keypoints = detector.detect(image) 
  
# Draw blobs on our image as red circles 
blank = np.zeros((1, 1))  
blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 0, 255), 
                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) 

# Generates a count of the number of a blobs that fit the given parameters  
number_of_blobs = len(keypoints) 
text = "Number of Dead Flies: " + str(len(keypoints))   
  
# Show blobs 
cv2.imshow("Dead Flies", blobs) 
print(text)
cv2.waitKey(0) 
cv2.destroyAllWindows() 

