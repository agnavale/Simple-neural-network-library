import numpy as np
from layers import Dense
from models import Sequential
from activations import Softmax
from losses import cross_entropy,cross_entropy_prime

# 2 to 4 decoder , classification problem
X = np.reshape([[0, 0], [0, 1], [1, 0], [1, 1]], (4, 2, 1))
Y = np.reshape([[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]], (4, 4, 1))


model = Sequential()
model.add(Dense(input_size=2,output_size=10))
model.add(Softmax())
model.add(Dense(input_size=15,output_size=4))
model.add(Softmax())

model.compile(loss='cross_entropy')
model.fit(X,Y, epochs = 10000, learning_rate= 0.01)

x1 = 0
while x1!= 100:
    x1 = int(input("x1: "))
    x2 = int(input("x2: "))
    x = np.reshape([x1,x2],(2,1))
    print(model.predict(x))
