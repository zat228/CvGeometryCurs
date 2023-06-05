# Brick geometry defect recognition system
This project is aimed at analyzing the received images from the conveyor and comparing them with the reference object. The result of the program is the answer whether the object meets the specified requirements.
# Layout of the conveyor line on Unity
The Unity asset contains a conveyor line with cameras and a mechanism for influencing the object. The same message occurs with Unity using the ZeroMQ library.
This asset captures the image of a brick and sends a command to start processing with Unity scripts, receiving instructions on further actions in response.

![Screenshot_2](https://github.com/zat228/CvGeometryCurs/assets/29509544/18b8c9fe-edaf-47be-8ab5-464816ab7f92)

# Image processing using the OpenCV library
On the part of the python script, the image is processed and analyzed:
Image processing begins with the translation of images into achromatic colors.
Next, the image is converted to bitwise, where :1 is a white pixel, 0 is black.
All the contours in the image are found, the largest ones are selected among them.
The area is located along the contours and is compared with the original image.
For dimensioning, the contour measurement is determined and the side lengths are calculated.

![Screenshot_3](https://github.com/zat228/CvGeometryCurs/assets/29509544/d8524591-5695-40d7-a767-ea75028108d1)
