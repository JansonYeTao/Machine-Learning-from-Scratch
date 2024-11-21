def union_find():
    father = []

    def find(x):
        if father[x] == x:
            return x

        father[x] = find(father[x])
        return father[x]

    def union(a, b):
        """
        Given 2 employees a, and b
        find their leadership root_a and root_b.
        
        and then we merge the leadership.
        """

        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            father[root_a] = root_b # mutually connected



# connecting component I:
class Connector_1:

    def __init__(self, n: int):
        self.father = [i for i in range(n)]

    def _find(self, x):
        # find the x's leadership
        if self.father[x] == x:
            return x
        self.father[x] = self._find(self.father[x])
        return self.father[x]
    
    def _union(self, a, b):
        root_a = self._find(a)
        root_b = self._find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
        
    def connect(self, a, b):
        self._union(a, b)

    def query(self, a, b):
        root_a = self._find(a)
        root_b = self._find(b)
        if root_a == root_b:
            return True
        return False




# connecting component II
class Connector_2:

    def __init__(self, n):
        from collections import defaultdict
        self.father = [i for i in range(n)]
        self.num_by_father = defaultdict(int)
    
    def _find(self, x):
        """
        Find leadership of x
        """
        if self.father[x] == x:
            return x
    
        f = self.father[x]
        self.num_by_father[f] = self.num_by_father[f] + 1
        self.father[x] = self._find(f)
        return self.father[x]

    def _union(self, a, b):
        root_a = self._find(a)
        root_b = self._find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
    
    def connect(self, a, b):
        self._union(a, b)

    def query(self, x):
        """
        Return the number of members of x
        """
        f = self.father[x]
        return self.num_by_father[f]



# connecting component III
class Connector_3:
    """
    Return the number of connected components (query)
    """

    def __init__(self, n):
        self.father = [i for i in range(n)]
        self.n_component = n
    
    def _find(self, x):
        """get root of x"""
        if self.father[x] == x:
            return x
    
        f = self.father[x]
        self.father[x] = self.find(f)
        return self.father[x]
    
    def _union(self, a, b):
        # merge nodea and nodeb
        root_a = self._find(a)
        root_b = self._find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.n_component -= 1

    def connect(self, a, b):
        self._union(a, b)
    
    def query(self):
        return self.n_component



import math

class Connector_3:
    """
    Manages connected components based on distance criteria using node coordinates.
    """
    
    def __init__(self, n, coordinates, k):
        """
        Initialize the Connector_3 instance.

        :param n: Number of nodes
        :param coordinates: List of tuples where each tuple represents the (x, y) coordinates of a node
        :param k: Distance threshold for merging nodes
        """
        self.father = list(range(n))
        self.n_component = n
        self.coordinates = coordinates
        self.k = k

    def _find(self, x):
        """Find the root of x with path compression."""
        if self.father[x] != x:
            self.father[x] = self._find(self.father[x])
        return self.father[x]

    def _union(self, a, b):
        """Merge the sets containing a and b."""
        root_a = self._find(a)
        root_b = self._find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.n_component -= 1

    def _distance(self, a, b):
        """Calculate Euclidean distance between node a and node b."""
        xa, ya = self.coordinates[a]
        xb, yb = self.coordinates[b]
        return math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)

    def connect(self, a, b):
        """
        Connect nodes a and b if their distance is less than k.

        :param a: Node a
        :param b: Node b
        """
        if self._distance(a, b) < self.k:
            self._union(a, b)

    def query(self):
        """Return the number of connected components."""
        return self.n_component