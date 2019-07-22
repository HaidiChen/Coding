class GraphVertex:
    white, gray, black = range(3)

    def __init__(self):
        self.color = GraphVertext.white
        self.edges = []

def is_deadlocked(G):
    def has_cycle(cur):
        if cur.color == GraphVertex.gray:
            return True

        cur.color = GraphVertex.gray

        if any(next.color != GraphVertex.black and has_cycle(next)
                for next in cur.edges):
            return True

        cur.color = GraphVertex.black

        return False

    return any(vertex.color == GraphVertex.white and has_cycle(vertex)
            for vertex in G)
