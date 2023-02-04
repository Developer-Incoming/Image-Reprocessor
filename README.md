# Image-Reprocessor
 Reprocesses images or just basically clears any traces if there is, anonymity it is.

 ### The python code uses those modules listed here:
  - sys, uses argv to get path.
  - os, listdir to loop through inputs folder.
  - PIL, uses Image to take the image's data and processes the processed image data from numpy.
  - numpy, ndarray and uint8 for cleaning the image's data taken from PIL.
 
 #### Speed?
  - Processed 2 4500x2500 images in less than a second.
 #### Transparent images?
  - Yessir (Check line 14).
 #### There's a lot of data in each image.
  - literally a 16.4mb image has been reprocessed into a about 15.4mb image, I was so surprised yet scared.
  - The amount of traces is tremendous, we need more knowledge about that.
 
 #### Example:
  - ![Example 1.2](https://github.com/Developer-Incoming/Image-Reprocessor/blob/main/outputs/test9 Data.png?raw=true)
    - Example 1.1 showing the original file's bytes, which are 149 bytes.
  - ![Example 1.2](https://github.com/Developer-Incoming/Image-Reprocessor/blob/main/outputs/Processed test9 Data.png?raw=true)
    - Example 1.2 showing the reprocessed file that lost 51 bytes out of 149 bytes of its original bytes, crazy isn't?