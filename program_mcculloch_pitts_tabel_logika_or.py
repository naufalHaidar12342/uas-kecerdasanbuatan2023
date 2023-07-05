# import library numpy
import numpy as np

# deklarasi tabel kebenaran logika OR dengan numpy
column_x1 = np.array([0, 1, 0, 1])
column_x2 = np.array([0, 0, 1, 1])
column_y = np.array([0, 1, 1, 1])


# deklarasi bobot/weight dan threshold
weight_1 = 1
weight_2 = 1
threshold = 1


# melakukan perhitungan nilai net
net = (column_x1 * weight_1) + (column_x2 * weight_2)

# melakukan perhitungan f(net) atau activation function
y_net = (net >= threshold).astype(int)


def showFNetColumnY():
    print("Nilai y_net: ", y_net)
    print("Nilai kolom y: ", column_y)


def compareColumnYColumnFNet():
    # loop to check if all members of y match with y_net
    for i in range(len(column_y)):
        if column_y[i] != y_net[i]:
            print("Nilai dari kolom output tabel kebenaran logika OR tidak sesuai dengan hasil perhitungan McCulloch Pitts")
            showFNetColumnY()
    print("Nilai dari kolom output tabel kebenaran logika OR sesuai dengan hasil perhitungan McCulloch Pitts")
    showFNetColumnY()


# uji coba
model_neuron = compareColumnYColumnFNet()
model_neuron
