import numpy as np
import matplotlib.pyplot as plt

# Dados dos pontos
x = [1, 2, 3, 4, 5]
y = [3, 5, 4, 6, 7]

# Ajuste de polinômio de grau 2
coef = np.polyfit(x, y, 2)
p = np.poly1d(coef)

# Plot dos pontos e do polinômio ajustado
plt.plot(x, y, 'o')
plt.plot(x, p(x), '-')
plt.show()
