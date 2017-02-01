import math

from Signaux.tp1_0 import make_sin, plot
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x, y = make_sin(0.5, math.pi, 50.0, 1000.0, 2)
    plot(x, y, "s1", "r.", 3)
    x, y = make_sin(1.3, f=50.0, fe=500.0, nT=2)
    plot(x, y, "s2", "b.")

    plt.show()