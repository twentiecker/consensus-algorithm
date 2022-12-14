import networkx as nx


class Network:
    def __init__(self):
        self.grp = nx.Graph()
        self.spn_tree = ""

    def graph(self, nodes, edges):
        for i in nodes:
            self.grp.add_node(str(i[0]), sval=float(i[1]))

        for i in edges:
            self.grp.add_edge(str(i[0]), str(i[1]), weight=float(i[2]))

    def spanning_tree(self, grp):
        self.spn_tree = nx.minimum_spanning_tree(grp, weight='weight', algorithm="kruskal")

    def articulation(self, grp):
        list_articulation = list(nx.articulation_points(grp))
        print(f"\nArticulation point(s) dari graph:")
        for articulation in list_articulation:
            print(articulation)

    def bridge(self, grp):
        list_bridges = list(nx.bridges(grp))
        print(f"\nBridge edge(s) dari graph:")
        for bridge in list_bridges:
            print(f"{bridge[0]}-{bridge[1]}")
