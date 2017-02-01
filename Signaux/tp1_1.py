import math

from Signaux.tp1_0 import make_sin, plot, build_plot

if __name__ == '__main__':
    x, y, label = make_sin(0.5, math.pi, 50.0, 1000.0, 2)
    plot(x, y, "s1 : " + label, "r.", 3)
    x, y, label = make_sin(1.3, f=50.0, fe=500.0, nT=2)
    plot(x, y, "s2 : " + label, "b.")
    build_plot([-1.5, +1.5], "Deux sinusoides ...")
