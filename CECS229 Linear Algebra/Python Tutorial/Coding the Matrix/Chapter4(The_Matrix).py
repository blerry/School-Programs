import numpy
import cv2

x = [[0 for j in range(4)] for i in range(3)]
'''
      1         2          3
  [0,0,0,0] [0,0,0,0]  [0,0,0,0]
  
  for(row)
      for(col)
'''
y = [[i-j for i in range(3)] for j in range(4)]

        
M = numpy.matrix( [[1,2,3],[11,12,13],[21,22,23]])
N = numpy.matrix(x)

A = numpy.array([[1,2],[3,4],[10,0]])
B = numpy.array([[3,-1]])

C = numpy.inner(A,B)

# You are given a high-resolution image. You would like a lower-resolution
# version to put on your web page so the page will load more quickly.
image = cv2.imread('grayLion.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Gray scale PIC