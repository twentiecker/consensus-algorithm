import read
import network
import plot
import calculate

# initiate class
read = read.Read()
network = network.Network()
plot = plot.Plot()
calculate = calculate.Calculate()

# baca database
read.nodes()
read.edges()

while True:
    print('''
=========================================
Major Assignment #2 - Consensus Algorithm
=========================================
1. Membentuk graph
2. Membentuk spanning tree
3. Mendapatkan articulation point
4. Mendapatkan bridge
5. Mendapatkan nilai konsensus
6. Keluar aplikasi
=========================================
    ''')

    input_pilihan = int(input("Masukkan pilihan: "))
    if input_pilihan == 1:
        # identifikasi graph
        network.graph(read.list_nodes, read.list_edges)
        print(network.grp)
        # gambar graphnya
        plot.graph(network.grp)
    elif input_pilihan == 2:
        # identifikasi spanning tree
        network.spanning_tree(network.grp)
        print(network.spn_tree)
        # gambar graphnya
        plot.graph(network.spn_tree)
    elif input_pilihan == 3:
        # mendapatkan articulation
        network.articulation(network.grp)
    elif input_pilihan == 4:
        # mendapatkan bridges
        network.bridge(network.grp)
    elif input_pilihan == 5:
        # identifikasi graph
        network.graph(read.list_nodes, read.list_edges)
        # identifikasi spanning tree
        network.spanning_tree(network.grp)
        # menghitung consensus
        calculate.consensus(network.spn_tree)
        # gambar grapphnya
        plot.consensus(calculate.iterasi, calculate.list_consensus)
    elif input_pilihan == 6:
        break
    else:
        print("Pilihan yang anda masukkan salah!")
