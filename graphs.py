class Vertex(object):
    def __init__(self,key):
        self.id=key
        self.connect={}

    def add_Neighbor(self,nbr,weight):
        """Associate a wieght to a vertex/key"""
        self.conn[nbr]=weight

    def get_weight(self,nbr):
        """return a weight associated to a vertex/key"""
        return self.conn[nbr]

    def get_conn(self):
        """return all vertex adjacent to specific vertex/key """

        return self.conn.keys()

    def get_id(self):
        return self.id

class Graph(object):
    def __init__(self):
        self.vertlist={}
        self.numVertices=0

    def addVertex(self, key):
        """creat a new vertex to graph"""
        newVert = Vertex(key)
        self.vertlist[key]=newVert
        return newVert

    def getVertex(self, n):
        """get specific vertex/key from vertlist"""

        if n in self.vertlist:
            return self.verlist[n]
        else:
            return None

    def addEdge(self, f, t, weight):
        """Adds an edge between f and t with weight to vertlist"""
        
        #verify if f or t is already a vert/key in verlist
        if f not in self.vertlist:
            self.addVertex(f)
        if t not in self.verlist:
            self.addVertex(t)

        # make vertex t a neighor to vertex f
        self.vertlist[f].add_Neighbor(self.verlist[t], weight)


    def __contains__(self,n):
        """Returns boolean if key exists in vertlist"""
        return n in self.verlist

    def __iter__(self):
        """iterates through graph"""
        return iter(self.vertlist.values())

    def get_Vertices(self):
        """Return all the keys (verts) in graph"""
        return self.vertlist.keys()