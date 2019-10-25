class Vertex(object):
    def __init__(self,key):
        self.id=key
        self.connect={}

    def add_Neighbor(self,nbr,weight):
        self.conn[nbr]=weight

class Graph(object):
    def __init__(self):
        self.vertlist={}
        self.numVertices=0

    def addVertex(self, key):
        