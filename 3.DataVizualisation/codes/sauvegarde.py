# Fichier sauvegarde.py
import numpy as np
import matplotlib.pyplot as plt


x1 = np.linspace(0.0, 5.0)
y1 = np.sin(2 * np.pi * x1) * np.exp(-x1)

plt.plot(x1, y1, 'yo-')
plt.title('Un exemple de figure')
plt.ylabel('Une oscillation')
plt.savefig('fig.pdf', format='pdf')
