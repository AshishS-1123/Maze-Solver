
class PathFinder:
    def __init__(self, maze):
        self.maze = maze

    def get_possible_directions(self, loc):
        directions = []

        temp = [ [1,0], [-1,0], [0,1], [0,-1] ]
        neighbours = []

        # Remove those neighbours that cant be visited
        for point in temp:
            if self.maze[loc[0], loc[1]] & (1<<temp.index(point)) != 0:
                x, y = loc[0] + point[0], loc[1] + point[1]

                if x < 0 or y < 0:
                    continue
                elif x > self.maze.shape[0]-1 or y > self.maze.shape[0]-1:
                    continue

                neighbours.append( [x,y] )

        return neighbours

    def get_all_paths(self, start, end):
        path = [start]
        i = 0
        while start != end:
            i += 1
            next_start = []

            possible_directions = self.get_possible_directions(start)

            #for x,y in possible_directions:
            #    print("\tvalue", self.maze[x,y])

            for x,y in possible_directions:

                # If cell has been visited before, skip
                if [x,y] in path:
                    continue

                # Otherwise, this is the path we will follow
                next_start = [x, y]
                break

            path.append(next_start)

            start = next_start

            if next_start == end:
                break

        return path
