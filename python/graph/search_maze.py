# given a white/black colored maze, and an entrance and a exit, find if
# there's a path from entrance to the exit.

# time complexity is O(|V| + |E|)
import collections

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

class Solution(object):
    def search_maze(self, maze, s, e):
        self.path = []
        if not self._search_maze_helper(maze, s):
            return []
        return self.path
    
    def _search_maze_helper(self, maze, cur):
        if (not (0 <= cur.x < len(maze) 
                and 0 <= cur.y < len(maze[cur.x])
                and maze[cur.x][cur.y] == WHITE):
            return False
        self.path.append(cur)
        maze[cur.x][cur.y] = BLACK

        if (any(
            self._search_maze_helper(maze, Coordinate(cur.x + 1, cur.y)),
            self._search_maze_helper(maze, Coordinate(cur.x - 1, cur.y)),
            self._search_maze_helper(maze, Coordinate(cur.x, cur.y + 1)),
            self._search_maze_helper(maze, Coordinate(cur.x, cur.y - 1))
            )):
            return True

        del self.path[-1]

        return False
