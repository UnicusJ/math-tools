class Graph:
    def __init__(self, edge_dict={}):
        self.data = edge_dict

    def get_node_number(self):
        return len(self.data)

    def get_edge_number(self):
        return len(self.get_edge_list())

    def get_edge_list(self):
        edge_list = []
        for key in self.data:
            for value in self.data[key]:
                if tuple(sorted([key, value])) not in edge_list:
                    edge_list.append((key, value))
        return edge_list

    def get_vertex_list(self):
        return [key for key in self.data]

    def get_neighbours(self, node):
        return self.data[node]

    def get_degree(self, node):
        return len(self.data[node])

    def add_node(self, node):
        self.data[node] = []

    def add_edge(self, n1, n2):
        self.data[n1].append(n2)
        self.data[n2].append(n1)

