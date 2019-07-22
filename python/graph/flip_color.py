# flip the color in a white/black matrix.
import collections

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

class Solution(object):
    # BFS version
    def flip_color(self, matrix, x, y):
        color  = matrix[x][y]
        queue = collections.deque([Coordinate(x, y)])
        matrix[x][y] = 1 ^ matrix[x][y]

        while queue:
            x, y = queue.popleft()

            for d in (0, 1), (0, -1), (1, 0), (-1, 0):
                next_x, next_y = x + d[0], y + d[1]
                if (0 <= next_x < len(matrix) 
                        and 0 <= next_y < len(matrix[next_x])
                        and matrix[next_x][next_y] == color):
                    matrix[next_x][next_y] = 1 ^ matrix[next_x][next_y]
                    queue.append(Coordinate(next_x, next_y))

    # DFS version
    def flip_color_dfs(self, matrix, x, y):
        color = matrix[x][y]
        matrix[x][y] = matrix[x][y] ^ 1

        for d in (0, 1), (0, -1), (1, 0), (-1, 0):
            next_x, next_y = x + d[0], y + d[1]
            if (0 <= next_x < len(matrix)
                    and 0 <= next_y < len(matrix[next_x])
                    and matrix[next_x][next_y] == color):
                flip_color_dfs(matrix, next_x, next_y)
