#get_grames.py
'''
Author: David Westerhaus
Date: 4.12.2023
Last Updated: 4.12.2023
Description: Program to take folder of videos and create folders of all frames of videos for
                use in AI modification
'''

import os
import cv2



def export(video, scene_num, file_path):

    filename = "scene"+str(scene_num)
    
    path = file_path+video
    cam = cv2.VideoCapture(path)
    
    try:
        if not os.path.exists(filename):
            os.makedirs(filename)

    except OSError:
        print("Error: creating directory of data...")
    currentframe = 0

    while(True):
        ret,frame = cam.read()
        if ret:
            name = './'+str(filename)+'/frame'+str(currentframe)+'.jpg'
            print("Creating..." + name)
            cv2.imwrite(name, frame)
            currentframe += 1
        else:
            break
    cam.release()
    print("Scene: "+str(scene_num)+" COMPLETED")
    print()


def main():
    path = str(input("What is the file path for your video folder? : "))+'/'
    directory = 'files'
    i = 1
    for file in os.listdir(directory):
        if file[0] != ".":
            export(file, i, path)
            i+=1


main()