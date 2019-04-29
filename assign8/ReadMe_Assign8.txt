# Please keep all these files under one folder !!!!

# This project is capable of detecting faces in a picture or video

# Notice that this project requires OpenCV ,numpy and imutils library
# To install the library,one can use the following commands

python3 -m pip install numpy
python3 -m pip install opencv-python
python3 -m pip install imutils

# To run the project, type following command

# this one detects faces in a picture and you can
# replace the 'image' argument with the real image path
# or you can use the example image provided in this project
python3 face_detection.py --image [your image path]

# this one detects faces using the camera so make sure you run
# this on a laptop or a computer that has a camera
python3 face_detection_video.py

