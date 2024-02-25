# Created by Shahrokh Hamidi
# PhD., Electrical & Computer Engineering

from skimage import io, color
from copy import deepcopy
import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib
import matplotlib as mpl
from scipy import signal 
import math
import os



#%matplotlib qt


class readImage:
    
    def __init__(self):
        
        pass
    


    @staticmethod
    def read_image(path):

        img = io.imread(path)[:,:,0:3]
        return readImage.color_gray(img)
    
    def color_gray(img):
         return color.rgb2gray(img)
        
        



        
def fft_2D(data, nfftu, nfftv):

    return  np.fft.fft2(data, (nfftu, nfftv))   





def Weiner_Filter(Img, H, K = 0.2):

    Img_deblurred = Img*(np.conj(H)/(abs(H)**2+K))
    img_deblurred = np.fft.ifft2(Img_deblurred)

    return np.fft.fftshift(img_deblurred)






def Display(img, img_blurry, img_deblurred):

        
        mpl.rcParams['toolbar'] = 'None'
        plt.subplot(131)
        plt.imshow(img, cmap = 'gray')
        plt.title('Original Image', fontsize = 12)
        plt.axis('off')
        plt.subplot(132)
        plt.imshow(img_blurry, cmap = 'gray')
        plt.title('Blurry Image', fontsize = 12)
        plt.axis('off')
        plt.subplot(133)
        plt.imshow(abs(img_deblurred[256:-12, 256:-15]), cmap = 'gray')
        plt.title('Deblurred Image', fontsize = 12)
        plt.axis('off')

        plt.show()




if __name__ == "__main__":


    os.getcwd()
    os.chdir("../images")
    img =  readImage.read_image(os.path.join('camera_man.png'))
    img_blurry =  readImage.read_image(os.path.join('blurry_image.png'))
    h =  readImage.read_image(os.path.join('kernel.png'))

    nfftu = 2**math.ceil(math.log2(img.shape[0] + h.shape[0]))*1
    nfftv = 2**math.ceil(math.log2(img.shape[1] + h.shape[1]))*1



    H = fft_2D(h, nfftu, nfftv)
    Img = fft_2D(img_blurry, nfftu, nfftv)

    img_deblurred = Weiner_Filter(Img, H)

    Display(img, img_blurry, img_deblurred)
