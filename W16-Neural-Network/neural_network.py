import numpy as np
import functions as fnc
import matplotlib.pylot as plt

class DenseLayer:
    def __init__(self, input_size, output_size, activation):
        self.weights = np.random.randn(input_size, output_size) * 0.1
        self.bias = np.zeroes(output_size)
        self.activation = activation

    def forward(self, x):
        self.x = x
        self.z = np.dot(self.weights, self.x) + self.bias
        self.a = self.activation.forward(self.z)
        return self.a
    
    def backward(self, grad_a):
        grad_z = grad_a * self.activation.backward(self.z, grad_a)
        self.dW = np.dot(self.x, grad_z)
        self.db = np.sum(grad_z, axis=0)
        grad_x = grad_z @ self.weights.T
        return grad_x
    
    def update(self, lr):
        self.weights -= lr * self.dW
        self.bias -= lr * self.db
        

class Neural_Network:
    def __init__(self, loss_fnc, lr=0.1):
        self.layers = []
        self.loss_fnc = loss_fnc
        self.lr = lr # Learning Rate

    def add_layer(self, layer):
        self.layers.append(layer)

    def f_forward(self, x):
        for layer in self.layers:
            x = layer.forward(x)
        return x

    def back_prop(self, y_pred, y_true):
        # Special case: Softmax + CrossEntropy
        if isinstance(self.loss_fn, fnc.CrossEntropyWithSoftmax):
            grad = self.loss_fn.backward(y_pred, y_true)
        else:
            grad = self.loss_fn.backward(y_pred, y_true)

            # Need to backprop through activation of last layer
            grad = self.layers[-1].activation.backward(self.layers[-1].z, grad)

        for layer in reversed(self.layers):
            grad = layer.backward(grad)

    def update(self):
        for layer in self.layers:
            layer.update(self.lr)

    def train(self, X, y, epochs=1000):
        for epoch in range(epochs):
            # forward
            y_pred = self.f_forward(X)

            # loss
            loss = self.loss_fnc.forward(y, y_pred)

            # backward
            self.back_prop(y, y_pred)

            # update weights
            self.update()

            if epoch % 100 == 0:
                print(f"Epoch {epoch}, Loss: {loss:.4f}")


    def predict():
        pass

