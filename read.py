class Read:
    def __init__(self):
        self.list_nodes = []
        self.list_edges = []

    def nodes(self):
        file_nodes = open('nodes.txt')
        # cnt = 0
        while True:
            line = file_nodes.readline()
            if not line:
                break
            txt = line.split('-')
            self.list_nodes.append([txt[0], float(txt[1])])
            # cnt += 1

    def edges(self):
        file_edges = open('edges.txt')
        # cnt = 0
        while True:
            line = file_edges.readline()
            if not line:
                break
            txt = line.split('-')
            self.list_edges.append([txt[0], txt[1], float(txt[2])])
            # cnt += 1
