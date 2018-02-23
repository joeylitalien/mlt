import numpy as np
import cv2
import random

mutations = 64*660*660
img = cv2.imread('lion.jpg',0)


def makeHistogram(img):
    
    height, width = img.shape[:2]
    spp = float(mutations) / float(height * width)
    histogram = np.zeros((height,width))
    print (height,width)
    x0 = random.randint(0,width-1)
    x1 = random.randint(0,height-1)
    Fx = img[x1,x0]
    

    #T is the transition probability (from pixel x to y and vice versa)
    Txy = 1.0/(width * height)
    Tyx = 1.0/(width * height)

    for i in range(mutations):
        #choose a tentative next sample using T
        y0 = random.randint(0,width-1)
        y1 = random.randint(0, height-1)
        Fy = img[y1,y0]
        Axy = min(1,(Fy*Txy)/(Fx*Tyx))
        if (random.uniform(0,1) < Axy):#probability of moving from sample x to sample y. If failed, we stay at current sample
            x0=y0
            x1=y1
            Fx=Fy
        histogram[x1,x0] = histogram[x1,x0] + 1.0/(spp*3) # accumulate histogram. Final histogram is a scaled version of original image, so we heuristically determine 3 as the scaling factor
    cv2.imshow('image',histogram)


makeHistogram(img)
cv2.waitKey(0)
cv2.destroyAllWindows()