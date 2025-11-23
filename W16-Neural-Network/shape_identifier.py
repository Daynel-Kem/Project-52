from neural_network import Neural_Network, DenseLayer
import functions as fnc

"""
10 x 10 input of 0 and 1
2 hidden layers with 6 and 7 nodes respectively
3 output options (rectangle, circle, triangle)

"""

model = Neural_Network(loss_fnc=fnc.CrossEntropyWithSoftmax(), lr=0.01)

model.add_layer(DenseLayer(100, 6, fnc.MSE()))
model.add_layer(DenseLayer(6, 7, fnc.MSE()))
model.add_layer(DenseLayer(7, 3, fnc.Softmax()))

# Make the dataset
model.train()

