# importando as bibliotecas
import numpy as np
import pandas as pd

z = np.zeros((4,))
print("z: ", z)

z = np.zeros((4,))
z[1] = 1.
print("z: ", z)

z = np.zeros((4,))
z[1:] = 1.
print("z: ", z)

z = np.zeros((4,))
z[:3] = 1.
print("z: ", z)

z = np.ones((4,))
z[-1] = 0.
print("z: ", z)

z = np.zeros((4,))
z[:-1] = 1.
print("z: ", z)

x = np.array([[2.,2.] , [2.,2.]])
print("x: \n", x)

x = np.array([2.] * 4).reshape(2, 2)
print("x: \n", x)

x = np.ones((2, 2)) + np.ones((2, 2))
print("x: \n", x)

x = 2 * np.ones((2, 2))
print("x: \n", x)

x = np.array([[1,2] , [3,4]])
y = x[0, :]
y[1] = 10
print("x: \n", x)

x = np.array([[1,3] , [11,10]])
print(np.mean(x[x > np.pi]))

data = {'animal' : ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age' : [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits' : [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority' : ['yes', 'yes', 'no', 'yes', 'no',
                      'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data=data, index=labels)
y_true = np.array([1., 2., 1.])
y_pred = np.array([1.1, 1.98, 1.05])
print(df)

