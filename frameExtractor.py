# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 12:17:52 2020

@author: srush
"""

#from pytube import YouTube
import time
import os
import math
import datetime
import cv2

####################### making frames of vedios

class FrameExtractor():
    '''
    Class used for extracting frames from a video file.
    '''
    def __init__(self, video_path):
        self.video_path = video_path
        self.vid_cap = cv2.VideoCapture(video_path)
        self.n_frames = int(self.vid_cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.fps = int(self.vid_cap.get(cv2.CAP_PROP_FPS))
        
    def get_video_duration(self):
        duration = self.n_frames/self.fps
        print(f'Duration: {datetime.timedelta(seconds=duration)}')
        
    def get_n_images(self, every_x_frame):
        n_images = math.floor(self.n_frames / every_x_frame) + 1
        print(f'Extracting every {every_x_frame} (nd/rd/th) frame would result in {n_images} images.')
        
    def extract_frames(self, every_x_frame, img_name, dest_path=None, img_ext = '.jpg'):
        if not self.vid_cap.isOpened():
            self.vid_cap = cv2.VideoCapture(self.video_path)
        
        if dest_path is None:
            dest_path = os.getcwd()
        else:
            if not os.path.isdir(dest_path):
                os.mkdir(dest_path)
                print(f'Created the following directory: {dest_path}')
        
        frame_cnt = 0
        img_cnt = 0

        while self.vid_cap.isOpened():
            
            success,image = self.vid_cap.read() 
            
            if not success:
                break
            
            if frame_cnt % every_x_frame == 0:
                img_path = os.path.join(dest_path, ''.join([img_name, '_', str(img_cnt), img_ext]))
                cv2.imwrite(img_path, image)  
                img_cnt += 1
                
            frame_cnt += 1
        
        self.vid_cap.release()
        cv2.destroyAllWindows()
#######################################loop on each downloaded vedio
        
dire='D:/Sciffer_Analytics/EMOTION'  #main folder path
vedios=os.listdir(dire+'/'+'Downloaded_Videos'+'/')
for ind,vedio in enumerate(vedios):
    try:
        path=dire+'/'+'Downloaded_Videos'+'/'+vedio
        fe = FrameExtractor(path)
        fe.get_video_duration()
        fe.get_n_images(every_x_frame=20)
        fe.extract_frames(every_x_frame=20, img_name=str(ind)+'surprise',dest_path=dire+'/'+'frames')
    except Exception as e:
        print(e)
  