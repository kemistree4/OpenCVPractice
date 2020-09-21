# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import os


def video_to_frames(video, path_output_dir, count=0):
    # extract frames from a video and save to directory as 'x.png' where 
    # x is the frame index
    vidcap = cv2.VideoCapture(video)
    while vidcap.isOpened():
        success, image = vidcap.read()
        if success:
            cv2.imwrite(os.path.join(path_output_dir, '%d.png') % count, image)
            count += 1
        else:
            break
    cv2.destroyAllWindows()
    vidcap.release()
    return count

video_to_frames('/home/kemistree4/Desktop/nat_light_bugs.mp4', '/media/kemistree4/SP PHD U3/Bug_pics/Nat_light_bugs')