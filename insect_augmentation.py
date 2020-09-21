#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on Wed Aug 11 10:38:44 2020

@author: kemistree4
"""


from PIL import Image, ImageFilter
import random

def random_paste(bug_number=1500):
    """Populate single photo with a set of fake insects
    
    >>> random_paste
    """
    
    background_img = Image.open(r'/media/kemistree4/SP PHD U3/Nat_light_bugs/0.png')
    background_paste = background_img.copy()

    # uses these to set the boundaries in which the bugs can be pasted
    background_length = background_img.size[0]
    background_height = background_img.size[1]
    
    count = 0
    while count <= bug_number:
        # opens file and rotates it counterclockwise a random number of degrees between 1 and 359
        im_bug = Image.open('/home/kemistree4/Desktop/bug_1.png').rotate(random.randint(1,359)).filter(ImageFilter.SMOOTH)
        # assigns the alpha channel of the rotated image
        alpha = im_bug.split()[-1]
        # pastes rotated image onto the background image using its mask
        background_paste.paste(im_bug, 
                               (random.randint(1,background_length),random.randint(1,background_height)), 
                               alpha)
        count = count + 1
    return background_paste

def create_multiple_images(image_count=20, output_directory='/home/kemistree4/Desktop/Synthetic_bug_images/'):
    image_number = 0
    while image_number <= image_count:
        bug_number = random.randint(1,1500)
        final = random_paste(bug_number=bug_number)
        final.save(output_directory + f'{image_number}_with_{bug_number}_bugs.png')  
        image_number = image_number + 1
   
if __name__ == '__main__': 
    create_multiple_images()