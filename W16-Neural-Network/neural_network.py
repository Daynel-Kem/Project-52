import numpy as np
import functions as fnc
import matplotlib.pyplot as plt


class DenseLayer:
    def __init__(self, input_size, output_size, activation):
        self.weights = np.random.randn(input_size, output_size) * 0.1
        self.bias = np.zeros(output_size)
        self.activation = activation

    def forward(self, x):
        self.x = x
        self.z = np.dot(self.x, self.weights,) + self.bias
        self.a = self.activation.forward(self.z)
        return self.a
    
    def backward(self, grad_a):
        grad_z = self.activation.backward(self.z, grad_a)
        self.dW = np.dot(self.x.T, grad_z)
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

    def back_prop(self, y_true, y_pred):
        grad = self.loss_fnc.backward(y_true, y_pred)

        for layer in reversed(self.layers):
            grad = layer.backward(grad)

    def update(self):
        for layer in self.layers:
            layer.update(self.lr)

    def train(self, X, y, epochs=1000):
        for epoch in range(epochs):
            y_pred = self.f_forward(X)

            # correct argument order
            loss = self.loss_fnc.forward(y, y_pred)

            # backprop: correct argument order
            self.back_prop(y, y_pred)

            self.update()

            if epoch % 100 == 0:
                print(f"Epoch {epoch}, Loss: {loss:.4f}")

    def predict(self, X):
        y_pred = self.f_forward(X)
        return y_pred

    def save_full(self, filename):
        model_data = {
            "lr": self.lr,
            "loss": self.loss_fnc.__class__.__name__,
            "layers": []
        }

        for layer in self.layers:
            layer_info = {
                "input_size": layer.weights.shape[0],
                "output_size": layer.weights.shape[1],
                "activation": layer.activation.__class__.__name__,
                "weights": layer.weights,
                "bias": layer.bias,
            }
            model_data["layers"].append(layer_info)

        np.save(filename, model_data, allow_pickle=True)

# Model Loader
activation_map = {
    "Sigmoid": fnc.Sigmoid,
    "Softmax": fnc.Softmax
}

loss_map = {
    "MSE": fnc.MeanSquaredError,
    "CrossEntropyWithSoftmax": fnc.CrossEntropyWithSoftmax
}

def load_full(filename):
    model_data = np.load(filename, allow_pickle=True).item()

    model = Neural_Network(loss_map[model_data["loss"]](), lr=model_data["lr"])

    for layer_info in model_data["layers"]:
        act = activation_map[layer_info["activation"]]()
        layer = DenseLayer(layer_info["input_size"], layer_info["output_size"], act)
        layer.weights = layer_info["weights"]
        layer.bias = layer_info["bias"]
        model.add_layer(layer)

    return model