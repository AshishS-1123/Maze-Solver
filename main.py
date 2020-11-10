# import OpenCV for image processing
import cv2

# Import MazeRepr for converting the image to a suitable data structure
from MazeUtils.MazeRepr import MazeRepr
# Import MazeSolver for simplifying the maze
from MazeUtils.MazeSimplify import MazeSimplyfier
# Imprt PathFinder to make sense of the simplified maze
from MazeUtils.PathFinder import PathFinder
# Import MazeDisplay to display the final solution
from  MazeUtils.MazeDisplay import MazeDisplay

# A variable to hold the path of the image to be processed
file = "images/maze04.jpg"

from time import time as timer
b = timer()

# Read the maze image in grayscale
image =cv2.imread(file, 0)
# The the same image in color
color = cv2.imread(file)

# Binarize the grayscale image with threshold set to 10
image = (image > 10) * 255

# Create an object for the MazeRepr class using the binarized image
mr = MazeRepr(image)
# Parse the image to get the maze representation
maze_representation = mr.parse_image()

# Create a MazeSimplyfier object for simplifying the maze
ms = MazeSimplyfier(maze_representation)
# Get the final path from the simplified maze
#(this path is still the maze representation array, but contains some blocked cells)
ms.get_final_path()

# Get the maze representation from the MazeSimplyfier
maze = ms.maze_repr
# Get the number of rows in the maze
size = maze.shape[0]
#print(maze)

# Create an objeect of the PathFinder class with the simplyfied maze as parameter
pf = PathFinder(maze)

# Get the path (in the form of list)
path = pf.get_all_paths( [0,0], [size-1,size-1] )
#print(path)

print(timer()-b)
# Create an object of the MazeDisplay class to display the images
md = MazeDisplay(image, color)
# Mark the path in the colored image
md.mark_path( path, mr.get_cell_along_axis(0), mr.get_cell_along_axis(1) )
# Show the images
md.show()
