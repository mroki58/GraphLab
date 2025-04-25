from Network import Network

def createNetwork(layers):
    net = Network()
    net.createLayers(layers)
    net.addRandomEdges()
    net.addWeights()
    # net.draw()
    return net


if __name__ == "__main__":
    net = createNetwork(2)
    net.draw()