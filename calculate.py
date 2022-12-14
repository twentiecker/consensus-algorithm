class Calculate:
    def __init__(self):
        self.list_consensus = []
        self.iterasi = 1

    def consensus(self, spn_tree):
        def average(list_input):
            n = len(list_input)
            xs = 0
            for xi in list_input:
                xs += xi
            avg = xs / n
            return avg

        input_threshold = input("Masukkan threshold penghitungan konsensus: ")
        threshold = float(input_threshold)
        dict_iter = {}
        list_temp = []

        spn_tree1 = spn_tree
        print(f"spn_tree.nodes: {spn_tree.nodes}")  # mendapatkan nodes
        for u in spn_tree.nodes:
            list_temp.append(spn_tree.nodes[u]['sval'])  # sval untuk mendapatkan nilai skalar yang disimpan
        print(f"list_temp: {list_temp}")
        self.list_consensus.append(list_temp)
        while True:
            list_avg = []
            for u in spn_tree.nodes:
                x = spn_tree.nodes[u]['sval']
                dict_iter[u] = [x]
                for v in spn_tree.nodes:
                    if spn_tree.has_edge(u, v):
                        y = spn_tree.nodes[v]['sval']
                        dict_iter[u].append(y)
            print(f"dict_iter: {dict_iter}")
            for u in spn_tree.nodes:
                avgu = average(dict_iter[u])
                dict_iter[u] = avgu
                list_avg.append(avgu)
                spn_tree.nodes[u]['sval'] = avgu
            self.list_consensus.append(list_avg)
            if ((max(list_avg)) - (min(list_avg))) <= threshold:
                break
            self.iterasi += 1
        print(f"\nKonsensus pada iterasi ke-{self.iterasi}, dengan nilai Skalar tiap node sebagai berikut:")
        list_sf = []
        for i in spn_tree1.nodes:
            print(f"{i}: {dict_iter[i]}")
            list_sf.append(dict_iter[i])
        print(f"\nRata-rata nilai Skalar semua node = {average(list_sf)}")
