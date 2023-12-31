# create_video_in_opencv
Use OpenCV to create video from images.
![Hooded_mountain_tanager_Buthraupis_montana_cucullata_Caldas-1024x683](https://github.com/ShebMichel/create_video_in_opencv/assets/45086441/c919a03d-3806-4659-8aac-87ef26a4b7ae)


# Brief Description
In this OpenCV exercise, you work with an image to create to create an animation. This example can be served as a guide to create a smart animation from from multiple images. 

This can be very useful to show images in rapid succession which can help you extract different insight to visualize your work by introducing a time axis.

This code let you:
- Manipulate images as numpy array
- Use OpenCV function to understand images 
- Finally, to create video file in OpenCV

The main work focus on Ken Burns Effect and the second part is the writing of the output video into an mp4 format

# Writing Video
 From the example in the previous section, you saw how we create a VideoWriter object
 -vidwriter = cv2.VideoWriter() 

If you are up to this point of this post, you learned to create a video in OpenCV, built from a sequence of frames (i.e., no audio). Also, you learned how to apply the Ken Burns effect to a picture, which in particular, you applied:

# Key takes:
 - The technique of cropping an image using numpy slicing syntax
 - The technique of resizing an image using OpenCV functions
 - Using affine transform to calculate the parameters of zoom and pan, and create frames of the   video 
 -And finally, you write the frames into a video file using the VideoWriter object in OpenCV.

# Video Result is shown below:


https://github.com/ShebMichel/create_video_in_opencv/assets/45086441/c8021055-90e9-43a2-a370-69ab37265988



<video width="630" height="300" src="https://github.com/ShebMichel/my_video/blob/main/video_output.mp4"></video>


 
