import Cv2_Handler


cv2,cap = Cv2_Handler.Get_Stream(webCam=0)


while True:

    Cv2_Handler.Stream(cap, cv2)
    
    if (cv2.waitKey(1) == 27):
        break
    
cv2.destroyAllWindows()
    