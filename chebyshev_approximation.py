import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 500)





def chebyshev_approximation_sin(f, n, x):
    T = [1, x]
    for i in range(2, n):
        print(i)


chebyshev_approximation_sin(np.sin, 100, x)

sin = np.sin(x)

plt.plot(x, sin, label="sin(x)")
plt.grid(True)
plt.show()