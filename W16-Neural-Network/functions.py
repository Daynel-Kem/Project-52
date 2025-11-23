import numpy as np

[
# # Hard coded Neural Network
# # Creating data set

# # A
# a =[0, 0, 1, 1, 0, 0,
#    0, 1, 0, 0, 1, 0,
#    1, 1, 1, 1, 1, 1,
#    1, 0, 0, 0, 0, 1,
#    1, 0, 0, 0, 0, 1]
# # B
# b =[0, 1, 1, 1, 1, 0,
#    0, 1, 0, 0, 1, 0,
#    0, 1, 1, 1, 1, 0,
#    0, 1, 0, 0, 1, 0,
#    0, 1, 1, 1, 1, 0]
# # C
# c =[0, 1, 1, 1, 1, 0,
#    0, 1, 0, 0, 0, 0,
#    0, 1, 0, 0, 0, 0,
#    0, 1, 0, 0, 0, 0,
#    0, 1, 1, 1, 1, 0]

# b_kinda = [0, 1, 1, 1, 1, 0,
#            0, 1, 0, 0, 1, 0,
#            0, 1, 1, 1, 0, 0,
#            1, 1, 0, 0, 1, 1,
#            1, 1, 0, 1, 1, 1]

# x_test = np.array(b_kinda).reshape(1, 30)

# # Creating labels
# y =[[1, 0, 0],
#    [0, 1, 0],
#    [0, 0, 1]]

# # converting data and labels into numpy array
# x = [np.array(a).reshape(1, 30), np.array(b).reshape(1, 30), 
#                                 np.array(c).reshape(1, 30)]
# y = np.array(y)


# # Activation Function
# def sigmoid(x):
#     return(1/(1+np.exp(-x)))

# # Mean Squared Error, Loss Function
# def loss(out, Y):   
#     s = np.square(Y - out)
#     s = np.sum(s)/len(y)
#     return s

# # Feed Forward Algorithm
# def f_forward(x, w1, w2):
#     z1 = x.dot(w1)
#     a1 = sigmoid(z1)
#     z2 = a1.dot(w2)
#     a2 = sigmoid(z2)
#     return a2

# def generate_wt(x, y):
#     li = []
#     for i in range(x * y):
#         li.append(np.random.randn())
#     return np.array(li).reshape(x,y)

# def back_prop(x, y, w1, w2, alpha):

#     # hidden layer
#     z1 = x.dot(w1)
#     a1 = sigmoid(z1)
#     z2 = a1.dot(w2)
#     a2 = sigmoid(z2)

#     d2 = (a2-y)
#     d1 = np.multiply((w2.dot((d2.transpose()))).transpose(), 
# 								(np.multiply(a1, 1-a1)))
#     # Gradient for w1 and w2
#     w1_adj = x.transpose().dot(d1)
#     w2_adj = a1.transpose().dot(d2)
	
#     # Updating parameters
#     w1 = w1-(alpha*(w1_adj))
#     w2 = w2-(alpha*(w2_adj))
	
#     return(w1, w2)



# w1 = generate_wt(30, 5)
# w2 = generate_wt(5, 3)

# print(w1)
# print("\n")
# print(w2)


# def train(x, Y, w1, w2, alpha = 0.01, epoch = 10):
#     acc = []
#     lossStat = []

#     for j in range(epoch):
#         l = []
#         for i in range(len(x)):
#             out = f_forward(x[i], w1, w2)
#             print(out)
#             l.append(loss(out, Y[i]))
#             w1, w2 = back_prop(x[i], y[i], w1, w2, alpha)
#         print("epochs:", j + 1, "======== acc:", (1-(sum(l)/len(x)))*100) 
#         acc.append((1-(sum(l)/len(x)))*100)
#         lossStat.append(sum(l)/len(x))
#     return (acc, lossStat, w1, w2)


# acc, losss, w1, w2 = train(x, y, w1, w2, 0.1, 100)


# # plotting accuracy
# plt.plot(acc)
# plt.ylabel('Accuracy')
# plt.xlabel("Epochs:")
# plt.show()

# # plotting Loss
# plt.plot(losss)
# plt.ylabel('Loss')
# plt.xlabel("Epochs:")
# plt.show()

# def predict(x, w1, w2):
#     Out = f_forward(x, w1, w2)
#     maxm = 0
#     k = 0
#     for i in range(len(Out[0])):
#         if (maxm < Out[0][i]):
#             maxm = Out[0][i]
#             k = i
#     if (k == 0):
#         print("Image is A")
#     elif (k == 1):
#         print("Image is B")
#     else:
#         print("Image is C")

#     plt.imshow(x.reshape(5, 6))
#     plt.show()

# predict(x_test, w1, w2)

]

# Activation Functions and their Derivatives Available
class Activation():
    def forward(self, z):
        raise NotImplementedError
    def backward(self, z, grad_output):
        raise NotImplementedError
    
class Sigmoid(Activation):
    def forward(self, z):
        return (1 / (1+np.exp(-z)))
    
    def backward(self, z, grad_output):
        s = self.forward(z)
        return grad_output * s * (1 - s)

class Softmax(Activation):
    def forward(self, z):
        if z.ndim == 1:
            z = z.reshape(1, -1)
        exp = np.exp(z - np.max(z, axis=1, keepdims=True))
        return exp / np.sum(exp, axis=1, keepdims=True)

    def backward(self, z, grad_output):
        # general softmax derivative (slower but flexible)
        s = self.forward(z)
        batch, n = s.shape
        grad = np.zeros_like(s)

        for i in range(batch):
            S = np.diag(s[i]) - np.outer(s[i], s[i])
            grad[i] = S @ grad_output[i]

        return grad

# Loss Functions amd Derivatives
class Loss():
    def forward(self, y_true, y_pred):
        raise NotImplementedError
    def backward(self, y_true, y_pred):
        raise NotImplementedError
    
class MeanSquaredError(Loss):
    def forward(self, y_true, y_pred):
        s = np.square(y_true - y_pred)
        s = np.sum(s)/y_true.size
        return s
    
    def backward(self, y_true, y_pred):
        return 2 * (y_true - y_pred) / y_pred.shape[0]
    
class CrossEntropyWithSoftmax(Loss):
    def forward(self, y_true, y_pred):
        eps = 1e-12
        return -np.mean(np.sum(y_true * np.log(y_pred + eps), axis=1))
    def backward(self, y_true, y_pred):
        return (y_pred - y_true) / y_true.shape[0]


