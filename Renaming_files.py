# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:29:28 2020

@author: akash
"""


import os
# Function to rename multiple files


def main():
    path = "D:/Mangal/AdI/extra frames/"
    for i, filename in enumerate(os.listdir(path), start=1937):
        my_dest = "CAGE" + ' ' + str(i) + ".jpeg"
        my_source = path + filename
        my_dest = path + my_dest
        # rename() function will
        # rename all the files
        os.rename(my_source, my_dest)
    print('Done Bro!!')


# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
