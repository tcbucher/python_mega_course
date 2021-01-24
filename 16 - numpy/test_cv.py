import numpy
import cv2

im_g = cv2.imread("smallgray.png", 0) # 0 flag Gets an array with the grayscale values of each pixel

print(im_g)

# 1 flag retrieves a two dimensional array,
# Each list within the list represents channel values for the grid of pixels 
# the 0 array is blue, 1 is green, and 2 is red
# Note that this is backwards from the RGB that most systems use (e.g. hex codes in CSS)
im_bgr = cv2.imread("smallgray.png", 1)

print(im_bgr)

cv2.imwrite("newsmallgray.png", im_g)

im_g[2,4] # This is how you get a specific index value in a multidimensional array (MDA)
im_g[0:2,2:4] # This is how you slice an MDA

# the .flat member flattens the MDA to a list of values
# in order from the top left to the bottom right
for i in im_g.flat:
    print(i)

# concatenating numpy arrays horizontally uses the numpy.hstack() function
# note that it needs to be passed a tuple that contains the arrays to be stacked
# below, I've stacked an array with itself
im_s = numpy.hstack((im_g, im_g))
print(im_s)
# stacking vertically uses the vstack() method
# if the arrays have different dimensions, it will throw an exception

# Conversely, splitting a numpy array uses the .hsplit() and .vsplit() methods
# These methods take two arguments, an array to split and an integer telling it how many arrays to split it into
# If the number of split arrays does not divide into the dimensions of the original, it will throw an exception
im_sp = numpy.hsplit(im_s, 2)
print(im_sp)