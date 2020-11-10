import numpy as np

class MazeSimplyfier:
    def __init__(self, maze_repr):
        self.maze_repr = maze_repr
        self.maze_shape = maze_repr.shape[0]

    def find_deadend_cells(self):
        # Create a empty list to hold the dead end cells
        dead_ends = []

        # Cells with only  1 side open are dead ends
        # 0b1000 (8), 0b0100 (4), 0b0010 (2), 0b0001 (1)
        possible_values = [ 8, 4, 2, 1 ]

        # Both loops start from 1 because the upper left and lower right are start and end coords
        for i in range(0, self.maze_shape):
            for j in range(0, self.maze_shape):
                if i == 0 and j == 0:
                    continue
                if i == self.maze_shape-1 and j == self.maze_shape-1:
                    continue
                if self.maze_repr[i,j] in possible_values:
                    dead_ends.append( [i,j] )

        return dead_ends

    def remove_dead_end_cells(self, dead_ends):

        # Loop through all the dead end Cells
        for cell in dead_ends:
            # Change the representation of its neighbouring Cells
            if self.maze_repr[ cell[0], cell[1] ] == 8:
                # if cell opened on LEFT
                # Toggle the right bit of its left cell
                self.maze_repr[cell[0], cell[1]-1] &= 11
                # Mark this cell as eliminated from the maze representation
                self.maze_repr[cell[0], cell[1]] = -1

            if self.maze_repr[ cell[0], cell[1] ] == 4:
                # if cell opened on RIGHT
                # Toggle the left bit of its right cell
                self.maze_repr[cell[0], cell[1]+1] &= 7
                # Mark this cell as eliminated from the maze representation
                self.maze_repr[cell[0], cell[1]] = -1

            if self.maze_repr[ cell[0], cell[1] ] == 2:
                # if cell opened on UP
                # Toggle the down bit of its up cell
                self.maze_repr[cell[0]-1, cell[1]] &= 14
                # Mark this cell as eliminated from the maze representation
                self.maze_repr[cell[0], cell[1]] = -1

            if self.maze_repr[ cell[0], cell[1] ] == 1:
                # if cell opened on DOWN
                # Toggle the up bit of its down cell
                self.maze_repr[cell[0]+1, cell[1]] &= 13
                # Mark this cell as eliminated from the maze representation
                self.maze_repr[cell[0], cell[1]] = -1

    def get_final_path(self):

        while True:
            dead_ends = self.find_deadend_cells()
            # If no dead ends are found, end the loop
            if len(dead_ends) == 0:
                break

            self.remove_dead_end_cells(dead_ends)
