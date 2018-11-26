from sklearn.neural_network import MLPClassifier
from numpy import loadtxt
from pickle import dump

def main():
    # carrego o dataset
    dataset = loadtxt("Blinky.txt", delimiter=";")

    # declaro a rede neural
    rede_neural = MLPClassifier()

    # treina a rede neural
    rede_neural.fit(dataset[:, :-1], dataset[:, -1].ravel())

    # salva a rede neural treinada no arquivo
    dump(rede_neural, open("RNAs Treinadas/Blinky.rna", "wb"))

if __name__ == '__main__':
    main()