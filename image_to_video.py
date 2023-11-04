"""
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import os,sys
import cv2
import numpy as np

imgfile        = "Hooded_mountain_tanager_Buthraupis_montana_cucullata_Caldas-1024x683.jpg"
# File directory
File_directory = os.getcwd()
# Read and Show image
img = cv2.imread(str(File_directory)+'/'+str(imgfile), cv2.IMREAD_COLOR)
cv2.imshow("bird", img)
cv2.waitKey(0)
#
#print(img)
'''Ken Burns effect is to zoom and pan. 
'''
#
##
#imgfile = "Hooded_mountain_tanager_Buthraupis_montana_cucullata_Caldas.jpg"
# Create the video dimension
video_dim = (1280, 720)
# Frame Per Session FPS
fps = 25
# Video Duration
duration = 2.0
# Coordinates definition
start_center = (0.4, 0.6)
end_center = (0.5, 0.5)
start_scale = 0.7
end_scale = 1.0
##
img       = cv2.imread(imgfile, cv2.IMREAD_COLOR)
orig_shape = img.shape[:2]
###
def crop(img, x, y, w, h):
    x0, y0 = max(0, x-w//2), max(0, y-h//2)
    x1, y1 = x0+w, y0+h
    return img[y0:y1, x0:x1]

num_frames = int(fps * duration)
frames = []
for alpha in np.linspace(0, 1, num_frames):
    rx = end_center[0]*alpha + start_center[0]*(1-alpha)
    ry = end_center[1]*alpha + start_center[1]*(1-alpha)
    x = int(orig_shape[1]*rx)
    y = int(orig_shape[0]*rx)
    scale = end_scale*alpha + start_scale*(1-alpha)
    # determined how to crop based on the aspect ratio of width/height
    if orig_shape[1]/orig_shape[0] > video_dim[0]/video_dim[1]:
        h = int(orig_shape[0]*scale)
        w = int(h * video_dim[0] / video_dim[1])
    else:
        w = int(orig_shape[1]*scale)
        h = int(w * video_dim[1] / video_dim[0])
    # crop, scale to video size, and save the frame
    cropped = crop(img, x, y, w, h)
    scaled = cv2.resize(cropped, dsize=video_dim, interpolation=cv2.INTER_LINEAR)
    frames.append(scaled)

# write to MP4 file
vidwriter = cv2.VideoWriter("video_output.mp4", cv2.VideoWriter_fourcc(*"mp4v"), fps, video_dim)
for frame in frames:
    vidwriter.write(frame)
vidwriter.release()


# To test some different codec format

# try:
#     fourcc = cv2.VideoWriter_fourcc(*"mp4v")
#     writer = cv2.VideoWriter('temp.mkv', fourcc, 30, (640, 480))
#     assert writer.isOpened()
#     print("Supported")
# except:
#     print("Not supported")
