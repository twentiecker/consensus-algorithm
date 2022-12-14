class Calculate:
    def __init__(self):
        self.list_consensus = []
        self.iterasi = 1

    def consensus(self, spn_tree):
        def average(list_input):
            n = len(list_input)
            total = 0
            for val in list_input:
                total += val
            avg = total / n
            return avg

        input_threshold = input("Masukkan threshold penghitungan konsensus: ")
        threshold = float(input_threshold)
        dict_iterasi = {}
        list_temp = []

        spn_tree1 = spn_tree
        print(f"spn_tree.nodes: {spn_tree.nodes}")  # mendapatkan seluruh node
        for u in spn_tree.nodes:
            list_temp.append(spn_tree.nodes[u]['sval'])  # sval untuk mendapatkan nilai skalar tiap node
        print(f"list_temp: {list_temp}")
        self.list_consensus.append(list_temp)
        while True:
            list_avg = []
            for u in spn_tree.nodes:
                x = spn_tree.nodes[u]['sval']
                dict_iterasi[u] = [x]
                for v in spn_tree.nodes:
                    if spn_tree.has_edge(u, v):
                        y = spn_tree.nodes[v]['sval']
                        dict_iterasi[u].append(y)
            print(f"dict_iterasi: {dict_iterasi}")
            for u in spn_tree.nodes:
                avg_u = average(dict_iterasi[u])
                dict_iterasi[u] = avg_u
                list_avg.append(avg_u)
                spn_tree.nodes[u]['sval'] = avg_u
            self.list_consensus.append(list_avg)

            # Memeriksa apakah selisih nilai max dan min sudah mencapai threshold
            if ((max(list_avg)) - (min(list_avg))) <= threshold:
                break
            self.iterasi += 1
        print(f"\nKonsensus pada iterasi ke-{self.iterasi}, dengan nilai Skalar tiap node sebagai berikut:")
        list_sf = []
        for i in spn_tree1.nodes:
            print(f"{i}: {dict_iterasi[i]}")
            list_sf.append(dict_iterasi[i])
        print(f"\nRata-rata nilai Skalar semua node = {average(list_sf)}")
