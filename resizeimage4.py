import cv2
img = cv2.imread('sunset1920.jpg')

print('Original Dimensions : ',img.shape)

width = input ('Enter the width [value is between 0.1 - 0.9]: ')
height = input ('Enter the height [value is between 0.1 - 0.9]: ')

def resizeimgvalue(fxv,fyv):
    resizeimg = cv2.resize(img,None,fx=fxv,fy=fyv)
        
    cv2.imshow('Resized Image',resizeimg)
    
    print('Resized Dimensions : ',resizeimg.shape)

def main():
    resizeimgvalue(float(width), float(height))

main()

cv2.waitKey(0)
cv2.destoryAllWindows()
