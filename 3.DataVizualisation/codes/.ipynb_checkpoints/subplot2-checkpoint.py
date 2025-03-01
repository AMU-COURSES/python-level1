# Fichier subplot2.py
import numpy as np
import matplotlib.pyplot as plt
x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)
y1 = np.sin(2 * np.pi * x1) * np.exp(-x1)
y2 = np.sin(2 * np.pi * x2)
fig, (ax1, ax2) = plt.subplots(2, 1)
plt.suptitle('Un exemple avec deux sous-figures')
ax1.plot(x1, y1, 'yo-', label ='avec frottement')

ax1.set_ylabel('Une oscillation')
ax1.legend()
ax2.plot(x2, y2, 'r.-', label ='sans frottement')
ax2.set_xlabel('temps (s)')
ax2.set_xlabel('Sans frottements')
ax2.legend()
plt.show()
