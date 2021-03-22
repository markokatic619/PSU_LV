import matplotlib.pyplot as plt
import numpy as np
import skimage.io


def rotiranje(img):
    width = img.shape[0]
    height = img.shape[1]
    img2 = np.zeros((height,width),np.uint8)
    for i in range(0,height):
        count = width-1
        for j in range(0,width):
            img2[i][count]=img[j][i]
            count = count - 1
    return img2

def posvijetli(brightnes,img):
    width = img.shape[0]
    height = img.shape[1]
    for i in range(0,height):
        for j in range(0,width):
            if (img[j][i]+brightnes)>255:
                img[j][i]=255
            if (img[j][i]+brightnes)<=255:
                img[j][i]=img[j][i]+brightnes


def zrcali(img):
    width = img.shape[1]
    height = img.shape[0]
    img2 = np.zeros((height,width),np.uint8)
    width2=width-1
    for i in range(0,width):
        img2[:,i]=img[:,width2]
        width2 = width2 - 1
    for j in range(0,width):
        img[:,j]=img2[:,j]

def smanjiRezoluciju(rez,img):
    width = img.shape[1]
    height = img.shape[0]
    newWidth = int(width/rez)
    newHeight = int(height/rez)
  
    img2 = np.zeros((newHeight,newWidth),np.uint8)
    for i in range(0,newHeight):
        for j in range(0,newWidth):
            sum=0
            for y in range(i*int(height/newHeight),(i+1)*int(height/newHeight)):
                for x in range(j*int(width/newWidth),(j+1)*int(width/newWidth)):
                    sum = sum + img[y][x]
            pixel=sum/((height/newHeight)*(width/newWidth))
            img2[i][j]=pixel
    return img2


brightnes = 150
img = skimage.io.imread('tiger.png', as_gray=True)
img2 = smanjiRezoluciju(10,img)
plt.figure(1)
plt.imshow(img2, cmap='gray', vmin=0, vmax=255)
plt.show()
