import sys
import cv2
sys.path.append('/home/pi/mlf/api')

from client import ClientWrapper

def get_frame():
    c = ClientWrapper()
    img = c.get_single_frame()

    cv2.imwrite('image.jpg', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return print('Frame guardado')