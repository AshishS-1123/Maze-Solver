# Import matplotlib for displaying the 2 images side by side
import matplotlib.pyplot as plt
# Import OpenCV for drawing the path on the image
import cv2

# Create a class that handles all the displaying
class MazeDisplay:
    # Create a constructor. the first parameter is the original maze image,
    # the second is the one in which the path is marked
    def __init__(self, original, solved):
        self.original = original
        self.solved = solved

    # Create a method to draw the path lines on the images
    # path is the parameter containing the list of cells in the path
    #row_cell parameter contains the coordinates of start and end points of row
    def mark_path(self, path, row_cell, col_cell):
        # Create a tmeporary empty list
        temp = []

        # For every value in the row cell
        for cell in row_cell:
            # Append the mid point of the cell
            temp.append( (cell[0]+cell[1]) // 2 )

        # Copy this temporary list to row_cell
        row_cell = temp

        # Reinitialise the temporary list to empty
        temp = []

        # For every value in the col cell
        for cell in col_cell:
            # Append the mid point of the cell
            temp.append( (cell[0]+cell[1]) // 2 )

        # Copy this temporary list to col_cell
        col_cell = temp

        # Loop through pairs of consecutive elements in the path
        for a,b in zip( path[0:-1], path[1:] ):
            # Get the coordinates of starting point of line from path and cell locations
            start = ( col_cell[a[1]] , row_cell[a[0]] )
            # Get the coordinates of ending point of line from path amd cell locations
            end = ( col_cell[b[1]] , row_cell[b[0]] )

            # Draw a line from the start point to the end point
            cv2.line(self.solved, start, end, (0,255,0), 2)

    # Method to show the images side by side
    def show(self):
        # Create a figure with 1 row and 2 columns
        fig = plt.figure(figsize = (1,2))

        # Add the first subplot
        fig.add_subplot(1,2,1)
        # Show the original image in the first subplot
        plt.imshow(self.original, cmap = "gray")

        # Add the second subplot
        fig.add_subplot(1,2,2)
        # Show the solved maze image in the second subplot
        plt.imshow(self.solved)

        # Display the plots
        plt.show()
