import numpy as np

# Create a class that processes the image and solve the maze
class MazeRepr:

    # Contructor for class
    def __init__(self, image):
        self.image = image
        self.maze = []
        self.shape = image.shape[0]

    def get_cell_along_axis(self, axis):
        # Step 1 : Not all the walls in the maze are located at the same place,
        # So we will find these points by projecting the images

        # Create a variable to hold the threshold for classifying the cells and walls
        threshold = 20
        # Create a variable to hold the row wise sum of image
        row_sum = np.sum( self.image, axis = axis) // self.image.shape[0] // 10
        #row_sum = (row_sum > 18) * 255

        # Create a empty list to hold the wall coordinates
        cell = []
        # Loop through the row_sum to get potential wall points
        i = 0
        temp = []

        while i < row_sum.shape[0]:
            # Check if the current element is less than threshold

            if row_sum[i] < threshold:
                i += 1
                continue

            # If the element is greater than the threshold,
            # Add it to the temporary list
            temp.append( i )

            # Loop through the list upto the end point of the wall
            while row_sum[i] >= threshold and i < row_sum.shape[0]:
                i += 1
            #i -= 1

            # Append the end point to the temp list
            temp.append( i )

            # Append the start and end point to the wall list
            cell.append( temp )

            # Reset the temp list to 0 elements
            temp = []

            i += 1

        return cell

    def convert_cell_to_wall(self, cell):
        prev = 0
        wall = []

        for element in cell:
            wall.append( (prev + element[0]) // 2 )
            prev = element[1]

        wall.append( (prev + self.image.shape[0]-1) // 2 )

        return wall

    def parse_image(self):

        row_cell = self.get_cell_along_axis(0)
        col_cell = self.get_cell_along_axis(1)

        row_wall = self.convert_cell_to_wall(row_cell)
        col_wall = self.convert_cell_to_wall(col_cell)

        shape = len(row_wall) - 1

        maze_rep = np.empty( (shape,shape), dtype = np.int32 )
        maze_rep[:,:] = 15

        row_number = 0
        col_number = 1

        for limit in row_cell:
            index = ( limit[0] + limit[1] ) // 2
            slice = self.image[ index, : ]

            for i in range(0,shape):
                if slice[ col_wall[i] ] == 0:
                    maze_rep[row_number, i] &= 7 #0b0111 LEFT
                if slice[ col_wall[i+1] ] == 0:
                    maze_rep[row_number, i] &= 11
            row_number += 1

        row_number = 0

        for limit in col_cell:
            index = ( limit[0] + limit[1] ) // 2
            slice = self.image[ :, index ]

            for i in range(0,shape):
                if slice[ row_wall[i] ] == 0:
                    maze_rep[i, row_number] &= 13
                if slice[ row_wall[i+1] ] == 0:
                    maze_rep[i, row_number] &= 14
            row_number += 1

        return maze_rep
