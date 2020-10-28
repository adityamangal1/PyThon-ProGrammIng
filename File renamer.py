# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:29:28 2020

@author: akash
"""


import os

# Function to rename multiple files


def main():

    for count, filename in enumerate(os.listdir('D:/Mangal/LOGIBRICKS/objects/CAGE/pictures/')):
        dst = "CAGE" + str(count) + ".jpeg"
        src = 'D:/Mangal/LOGIBRICKS/objects/CAGE/pictures/' + filename
        dst = 'D:/Mangal/LOGIBRICKS/objects/CAGE/pictures/' + dst

        # rename() function will
        # rename all the files
        os.rename(src, dst)


# Driver Code
if __name__ == '__main__':

    # Calling main() function
    main()
