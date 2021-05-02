import numpy as np
import math

# TAMANHO MÍNIMO DO SISTEMA: 2 EQUAÇÕES
def jacobi(m):
    x1 = np.zeros_like(m[:, :-1])
    np.fill_diagonal(x1, 0)
    d1 = math.inf
    #print(x1)
    a = m[:, :-1]
    b = m[:, -1]
    #print(a)
    #print(b)
    parada = 0
    while True:
        #print(np.sum(a*x1, axis=1))
        x2 = (b-np.sum(a*x1, axis=1))/np.diagonal(m)
        x2 = np.repeat(np.reshape(x2, (1, x2.shape[0])), [x2.shape[0]], axis=0)
        np.fill_diagonal(x2, 0)
        print(x2)
        d2 = np.absolute(x2-x1)
        print(d2)
        # Variação absoluta
        if np.all(d2 < 0.001):
            x1 = np.copy(x2)
            break
        if np.sum(d2) > np.sum(d1):
            parada += 1
        else:
            parada = 0
        if parada == 4:
            return None
        x1 = np.copy(x2)
        d1 = d2

    x = x1[0, :]
    x[0] = x1[1][0]

    return x

m1 = [[3, -0.1, -0.2, -0.3, 7.85], [0.1, 7, -0.3, 0.3, -19.3], [0.3, -0.2, 10, 0.2, 71.4], [0.1, 0.4, -0.3, 12, 39.3]]
m2 = [[3, -0.1, -0.2, 7.85], [0.1, 7, -0.3, -19.3], [0.3, -0.2, 10, 71.4]]
m3 = [[0.1, 7, -19.3], [3, -0.2, 7.85]]
m2 = np.asarray(m2)
x = jacobi(m2)
print(x)