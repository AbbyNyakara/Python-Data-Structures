class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex, val in self.adj_list.items():
            print(f"{vertex}: {val}")

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:  # Does not allow duplicates
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, vertex1, vertex2):
        # Before adding an edge between two nvertices, I have to ensure that they actually exist
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)
            return True
        return False

    # The edeges may exist, but there is no edge between them which will result in value error!
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            try:
                self.adj_list[vertex1].remove(vertex2)
                self.adj_list[vertex2].remove(vertex1)
            except ValueError:
                pass
                return True
        return False


my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_edge("A", "B")
my_graph.add_edge("B", "C")


my_graph.print_graph()

my_graph.remove_edge("A", "C")  # Incase the
my_graph.print_graph()
