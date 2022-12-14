import read
import network
import plot
import calculate

# Inisiasi class
read = read.Read()
network = network.Network()
plot = plot.Plot()
calculate = calculate.Calculate()

# Membaca data dari file txt (nodes.txt dan edges.txt)
read.nodes()
read.edges()

while True:
    print('''
=========================================
Major Assignment #2 - Consensus Algorithm
=========================================
1. Membentuk Graph
2. Membentuk Spanning Tree
3. Mendapatkan Articulation Point
4. Mendapatkan Bridge
5. Mendapatkan Consensus
6. Keluar Aplikasi
=========================================
    ''')

    input_pilihan = int(input("Masukkan Pilihan: "))
    if input_pilihan == 1:
        # Inisiasi graph
        network.graph(read.list_nodes, read.list_edges)
        print(network.grp)
        # Membentuk graph
        plot.graph(network.grp)
    elif input_pilihan == 2:
        # Inisiasi graph
        network.graph(read.list_nodes, read.list_edges)
        # Inisiasi spanning tree
        network.spanning_tree(network.grp)
        print(network.spn_tree)
        # Membentuk spanning tree
        plot.graph(network.spn_tree)
    elif input_pilihan == 3:
        # Inisiasi graph
        network.graph(read.list_nodes, read.list_edges)
        # Mendapatkan articulation point
        network.articulation(network.grp)
    elif input_pilihan == 4:
        # Inisiasi graph
        network.graph(read.list_nodes, read.list_edges)
        # Mendapatkan bridge
        network.bridge(network.grp)
    elif input_pilihan == 5:
        # Inisiasi graph
        network.graph(read.list_nodes, read.list_edges)
        # Inisiasi spanning tree
        network.spanning_tree(network.grp)
        # Mendapatkan consensus
        calculate.consensus(network.spn_tree)
        # Plot iterasi dan consensus
        plot.consensus(calculate.iterasi, calculate.list_consensus)
    elif input_pilihan == 6:
        break
    else:
        print("Pilihan yang anda masukkan salah!")
