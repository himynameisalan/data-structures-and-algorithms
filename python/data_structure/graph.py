class MyGraph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list = {}

    def add_vertex(self, node):
        self.adjacent_list[node] = []
        self.number_of_nodes += 1

    def add_edge(self, node1, node2):
        if node2 not in self.adjacent_list.get(node1):
            self.adjacent_list.get(node1).append(node2)
        if node1 not in self.adjacent_list.get(node2):
            self.adjacent_list.get(node2).append(node1)

    def show_connections(self):
        for node, edge in self.adjacent_list.items():
            print(node, edge)


myGraph = MyGraph()
myGraph.add_vertex('0')
myGraph.add_vertex('1')
myGraph.add_vertex('2')
myGraph.add_vertex('3')
myGraph.add_vertex('4')
myGraph.add_vertex('5')
myGraph.add_edge('1', '2')
myGraph.add_edge('2', '1')
myGraph.add_edge('1', '2')
myGraph.add_edge('3', '2')
myGraph.add_edge('1', '5')

print(myGraph.adjacent_list)
myGraph.show_connections()