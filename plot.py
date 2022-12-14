import matplotlib.pyplot as plt
import networkx as nx


class Plot:
    def graph(self, data):
        plt.title("Graph")
        label_edge = nx.get_edge_attributes(data, 'weight')
        pos = nx.spring_layout(data)
        nx.draw(data, pos, with_labels=True, node_color="orange")
        nx.draw_networkx_edge_labels(data, pos, edge_labels=label_edge)
        plt.show()

    def consensus(self, itr, cons):
        plt.title("Grafik Konsensus (Average Consensus Algorithm)")
        list_x = []
        for i in range(0, itr + 1):
            list_x.append(i)
        list_constp = [list(i) for i in zip(*cons)]
        for c in list_constp:
            plt.plot(list_x, c)
        plt.show()
