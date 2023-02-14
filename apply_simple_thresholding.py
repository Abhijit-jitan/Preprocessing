import cv2

def simple_thresholding(image_path,choice,lower_limit=127,upper_limit=255):
    """ In: gray_image, thresholding_type, lower & upper limit 
        out: threshold image
    """
    
    gray_image=cv2.imread(image_path,0)
    
    if choice=="binary":
        _,binary=cv2.threshold(gray_image,lower_limit,upper_limit,cv2.THRESH_BINARY)
        return binary

    if choice=="binary_inverse":
        _,binary_inv=cv2.threshold(gray_image,lower_limit,upper_limit,cv2.THRESH_BINARY_INV)
        return binary_inv

    if choice=="trunc":
        _,trunc=cv2.threshold(gray_image,lower_limit,upper_limit,cv2.THRESH_TRUNC)
        return trunc

    if choice=="zero":
        _,zero=cv2.threshold(gray_image,lower_limit,upper_limit,cv2.THRESH_TOZERO)
        return zero

    if choice=="zero_inverse": 
        _,zero_inv=cv2.threshold(gray_image,lower_limit,upper_limit,cv2.THRESH_TOZERO_INV)
        return zero_inv
    
    
    
    
    
## choice: "binary","binary_inverse","trunc","zero","zero_inverse"    
out=simple_thresholding(image_path=r"D:\Resolute AI\Image Processing tool\data\image.png",lower_limit=127,upper_limit=255,choice="binary")

cv2.imshow("out",out)
cv2.waitKey(0)
cv2.destroyAllWindows()