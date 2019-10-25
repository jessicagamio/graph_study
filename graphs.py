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
        newVert = Vertex(key)
        self.vertlist[key]=newVert
        return newVert

    def getVertex(self, n):
        if n in self.vertlist:
            return self.verlist[n]
        else:
            return None

    def addEdge(self, f, t, weight):
        if f not in self.vertlist:
            self.addVertex(f)
        if t not in self.verlist:
            self.addVertex(t)
        self.vertlist[f].add_Neighbor(self.verlist[t], weight)


