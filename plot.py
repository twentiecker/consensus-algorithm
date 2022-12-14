import matplotlib.pyplot as plt
import networkx as nx


class Plot:
    def graph(self, data):
        plt.title("Graph")
        lbl_edge = nx.get_edge_attributes(data, 'weight')
        pos = nx.spring_layout(data)
        nx.draw(data, pos, with_labels=True, node_color="orange")
        nx.draw_networkx_edge_labels(data, pos, edge_labels=lbl_edge)
        plt.show()

    def consensus(self, itr, cons):
        # plot3 = plt.figure(3)
        plt.title("Grafik Konsensus (Average Consensus Algorithm)")
        ls_x = []
        for i in range(0, itr + 1):
            ls_x.append(i)
        ls_constp = []
        ls_constp = [list(i) for i in zip(*cons)]
        for c in ls_constp:
            plt.plot(ls_x, c)
        plt.show()
