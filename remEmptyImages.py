import cv2
import os


path = r'D:/Mangal/LOGIBRICKS/objects/CAGE/pictures/'

for file in os.listdir(path):
    im=cv2.imread(path+'/'+file)
    if im is None:
        os.remove(path+'/'+file)
        print(file)             
print('!done')
# a = cv2.imread(path+'/'+file)
