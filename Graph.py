import heapq  
  
class Graph:  
    def __init__(self, directed=False):  
        """  
        Initializes the graph.  
          
        :param directed: Boolean indicating if the graph is directed.  
        """  
        self.adj_list = {}  
        self.directed = directed  
  
    def add_vertex(self, vertex):  
        """  
        Adds a vertex to the graph.  
          
        :param vertex: The vertex to add.  
        """  
        if vertex not in self.adj_list:  
            self.adj_list[vertex] = []  
            print(f"Added vertex: {vertex}")  
  
    def add_edge(self, u, v, weight=None):  
        """  
        Adds an edge to the graph. If the graph is undirected, adds edge in both directions.  
          
        :param u: The starting vertex.  
        :param v: The ending vertex.  
        :param weight: The weight of the edge (optional).  
        """  
        if u not in self.adj_list:  
            self.add_vertex(u)  
        if v not in self.adj_list:  
            self.add_vertex(v)  
          
        self.adj_list[u].append((v, weight) if weight is not None else v)  
        if not self.directed:  
            self.adj_list[v].append((u, weight) if weight is not None else u)  
        print(f"Added edge: {u} -> {v}" + (f" with weight {weight}" if weight else ""))  
  
    def remove_vertex(self, vertex):  
        """  
        Removes a vertex and all associated edges from the graph.  
          
        :param vertex: The vertex to remove.  
        """  
        if vertex in self.adj_list:  
            del self.adj_list[vertex]  
            for u in self.adj_list:  
                # Remove all occurrences of the vertex in adjacency lists  
                self.adj_list[u] = [item for item in self.adj_list[u] if item[0] != vertex if isinstance(item, tuple) else item != vertex]  
            print(f"Removed vertex and all associated edges: {vertex}")  
        else:  
            print(f"Vertex {vertex} does not exist.")  
  
    def remove_edge(self, u, v):  
        """  
        Removes an edge from the graph.  
          
        :param u: The starting vertex.  
        :param v: The ending vertex.  
        """  
        if u in self.adj_list:  
            original_length = len(self.adj_list[u])  
            self.adj_list[u] = [item for item in self.adj_list[u] if item[0] != v if isinstance(item, tuple) else item != v]  
            if len(self.adj_list[u]) < original_length:  
                print(f"Removed edge: {u} -> {v}")  
            else:  
                print(f"Edge {u} -> {v} not found.")  
        else:  
            print(f"Vertex {u} does not exist.")  
          
        if not self.directed:  
            if v in self.adj_list:  
                original_length = len(self.adj_list[v])  
                self.adj_list[v] = [item for item in self.adj_list[v] if item[0] != u if isinstance(item, tuple) else item != u]  
                if len(self.adj_list[v]) < original_length:  
                    print(f"Removed edge: {v} -> {u}")  
                else:  
                    print(f"Edge {v} -> {u} not found.")  
            else:  
                print(f"Vertex {v} does not exist.")  
  
    def get_neighbors(self, vertex):  
        """  
        Retrieves all neighboring vertices of a given vertex.  
          
        :param vertex: The vertex whose neighbors to retrieve.  
        :return: List of neighbors.  
        """  
        if vertex in self.adj_list:  
            return self.adj_list[vertex]  
        else:  
            print(f"Vertex {vertex} does not exist.")  
            return []  
  
    def is_connected(self, start, end):  
        """  
        Checks if two vertices are connected in the graph using DFS.  
          
        :param start: The starting vertex.  
        :param end: The ending vertex.  
        :return: Boolean indicating if there's a path from start to end.  
        """  
        visited = set()  
        return self._dfs(start, end, visited)  
      
    def _dfs(self, current, target, visited):  
        if current == target:  
            return True  
        visited.add(current)  
        for neighbor in self.get_neighbors(current):  
            if isinstance(neighbor, tuple):  
                neighbor = neighbor[0]  
            if neighbor not in visited:  
                if self._dfs(neighbor, target, visited):  
                    return True  
        return False  
  
    def print_graph(self):  
        """  
        Prints the adjacency list representation of the graph.  
        """  
        for vertex in self.adj_list:  
            print(f"{vertex} -> {self.adj_list[vertex]}")  
  
  
def prim_mst(graph, start_vertex):  
    """  
    Finds the Minimum Spanning Tree (MST) of a graph using Prim's algorithm.  
      
    :param graph: Graph object  
    :param start_vertex: Starting vertex for Prim's algorithm  
    :return: List of edges in the MST  
    """  
    mst = []  
    visited = set()  
    min_heap = []  
      
    def add_edges(vertex):  
        visited.add(vertex)  
        for neighbor in graph.get_neighbors(vertex):  
            if isinstance(neighbor, tuple):  
                neighbor_vertex, weight = neighbor  
            else:  
                neighbor_vertex, weight = neighbor, 1  # Default weight  
            if neighbor_vertex not in visited:  
                heapq.heappush(min_heap, (weight, vertex, neighbor_vertex))  
      
    add_edges(start_vertex)  
      
    while min_heap and len(visited) < len(graph.adj_list):  
        weight, u, v = heapq.heappop(min_heap)  
        if v not in visited:  
            mst.append((u, v, weight))  
            add_edges(v)  
      
    return mst  
  
  
class UnionFind:  
    """  
    Union-Find (Disjoint Set) data structure implementation.  
    """  
    def __init__(self):  
        self.parent = {}  
      
    def find(self, item):  
        if self.parent[item] != item:  
            self.parent[item] = self.find(self.parent[item])  # Path compression  
        return self.parent[item]  
      
    def union(self, set1, set2):  
        root1 = self.find(set1)  
        root2 = self.find(set2)  
        if root1 != root2:  
            self.parent[root2] = root1  
      
    def make_set(self, item):  
        if item not in self.parent:  
            self.parent[item] = item  
  
  
def kruskal_mst(graph):  
    """  
    Finds the Minimum Spanning Tree (MST) of a graph using Kruskal's algorithm.  
      
    :param graph: Graph object  
    :return: List of edges in the MST  
    """  
    mst = []  
    uf = UnionFind()  
    edges = []  
      
    # Initialize Union-Find  
    for vertex in graph.adj_list:  
        uf.make_set(vertex)  
      
    # Create a list of all edges with weights  
    for u in graph.adj_list:  
        for neighbor in graph.get_neighbors(u):  
            if isinstance(neighbor, tuple):  
                v, weight = neighbor  
            else:  
                v, weight = neighbor, 1  # Default weight  
            if u < v:  # Avoid duplicate edges in undirected graph  
                edges.append((weight, u, v))  
      
    # Sort edges by weight  
    edges.sort()  
      
    for edge in edges:  
        weight, u, v = edge  
        # If adding this edge doesn't form a cycle  
        if uf.find(u) != uf.find(v):  
            uf.union(u, v)  
            mst.append(edge)  
      
    return mst  
  
  
def dijkstra_shortest_paths(graph, start_vertex):  
    """  
    Finds the shortest paths from start_vertex to all other vertices using Dijkstra's algorithm.  
      
    :param graph: Graph object  
    :param start_vertex: The source vertex  
    :return: Tuple of (distance, predecessor) dictionaries  
    """  
    distances = {vertex: float('infinity') for vertex in graph.adj_list}  
    predecessor = {vertex: None for vertex in graph.adj_list}  
    distances[start_vertex] = 0  
    min_heap = [(0, start_vertex)]  
      
    while min_heap:  
        current_distance, u = heapq.heappop(min_heap)  
          
        # If the distance is outdated, skip  
        if current_distance > distances[u]:  
            continue  
          
        for neighbor in graph.get_neighbors(u):  
            if isinstance(neighbor, tuple):  
                v, weight = neighbor  
            else:  
                v, weight = neighbor, 1  # Default weight  
              
            distance_through_u = current_distance + weight  
            if distance_through_u < distances[v]:  
                distances[v] = distance_through_u  
                predecessor[v] = u  
                heapq.heappush(min_heap, (distance_through_u, v))  
                print(f"Updated distance of {v} to {distance_through_u} via {u}")  
      
    return distances, predecessor  

def create_sample_graph():  
    """  
    Creates a sample undirected weighted graph.  
      
    Graph Structure:  
        A --1--- B  
        | \     |  
        4  3    2  
        |   \   |  
        D --5--- C  
    """  
    graph = Graph(directed=False)  
    graph.add_edge('A', 'B', 1)  
    graph.add_edge('A', 'D', 4)  
    graph.add_edge('A', 'C', 3)  
    graph.add_edge('B', 'C', 2)  
    graph.add_edge('C', 'D', 5)  
    return graph  
  
  
def prims_example():  
    print("=== Prim's Algorithm Example ===")  
    graph = create_sample_graph()  
    graph.print_graph()  
      
    mst = prim_mst(graph, 'A')  
    print("\nMinimum Spanning Tree (Prim's):")  
    total_weight = 0  
    for edge in mst:  
        u, v, weight = edge  
        print(f"{u} --{weight}--> {v}")  
        total_weight += weight  
    print(f"Total Weight: {total_weight}")  
  
  
def kruskals_example():  
    print("\n=== Kruskal's Algorithm Example ===")  
    graph = create_sample_graph()  
    graph.print_graph()  
      
    mst = kruskal_mst(graph)  
    print("\nMinimum Spanning Tree (Kruskal's):")  
    total_weight = 0  
    for edge in mst:  
        weight, u, v = edge  
        print(f"{u} --{weight}--> {v}")  
        total_weight += weight  
    print(f"Total Weight: {total_weight}")  
  
  
def dijkstra_example():  
    print("\n=== Dijkstra's Algorithm Example ===")  
    graph = create_sample_graph()  
    graph.print_graph()  
      
    start_vertex = 'A'  
    distances, predecessor = dijkstra_shortest_paths(graph, start_vertex)  
      
    print(f"\nShortest distances from {start_vertex}:")  
    for vertex in distances:  
        print(f"Distance to {vertex}: {distances[vertex]}")  
      
    # Reconstruct and print the path  
    def reconstruct_path(predecessor, start, end):  
        path = []  
        at = end  
        while at is not None:  
            path.append(at)  
            at = predecessor[at]  
        path.reverse()  
        if path[0] == start:  
            return path  
        return []  
      
    print(f"\nShortest paths from {start_vertex}:")  
    for vertex in distances:  
        if vertex == start_vertex:  
            continue  
        path = reconstruct_path(predecessor, start_vertex, vertex)  
        path_str = " -> ".join(path)  
        print(f"Path to {vertex}: {path_str} with distance {distances[vertex]}")  
  
  
if __name__ == "__main__":  
    prims_example()  
    kruskals_example()  
    dijkstra_example()  
