# Fichier subplot.py
import numpy as np
import matplotlib.pyplot as plt
x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)
y1 = np.sin(2 * np.pi * x1) * np.exp(-x1)
y2 = np.sin(2 * np.pi * x2)

plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'yo-', label ='avec frottement')
plt.title('Un exemple avec deux sous-figures')
plt.ylabel('Une oscillation')
plt.legend()
plt.subplot(2, 1, 2)
plt.plot(x2, y2, 'r.-', label ='sans frottement')
plt.xlabel('temps (s)')
plt.ylabel('Sans frottements')
plt.legend()
plt.show()
