# Fichier latex.py
import numpy as np
import matplotlib.pyplot as plt


t = np.arange(0.0, 1.0 + 0.01, 0.01)
s = np.cos(4 * np.pi * t) + 2

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.plot(t, s)

plt.xlabel(r'\textbf{temps} (s)')
plt.ylabel(r'\textit{voltage} (mV)', fontsize=16)
plt.title(r"\LaTeX\ est un super"
          r"$\displaystyle\sum_{n=1}^\infty\frac{-e^{i\pi}}{2^n}$!",
          fontsize=16, color='gray')
plt.subplots_adjust(top=0.8)  # Fait de la place pour le titre
plt.show()
