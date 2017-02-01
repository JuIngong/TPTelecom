#!usr/bin/python
# -*- coding: utf-8 *-*

import math
import matplotlib.pyplot as plt
import numpy as np


def make_sin(a=1.0, ph=0, f=440.0, fe=8000.0, nT=1):
    """
    Create a synthetic 'sine wave'
    First version : use classic Python lists
    """
    omega = 2 * math.pi * f
    N = int(fe / f)
    te = 1.0 / fe
    sig_t = []
    sig_s = []
    for i in range(N * nT):
        t = te * i
        sig_t.append(t)
        sig_s.append(a * math.sin((omega * t) + ph))

    label = "{0} Hz, {1} V, {2} pH, {3} fe".format(two_float(f), two_float(a), two_float(ph), two_float(fe))
    return sig_t, sig_s, label


def two_float(value):
    return ("{:.2f}".format(value)).rstrip('0').rstrip('.')


def plot(inx, iny, label, format='-bo', size=7):
    plt.plot(inx, iny, format, markersize=size, label=label)


def build_plot(ylim, title, grid_style=":"):
    plt.xlabel('time (s)')
    plt.ylabel('voltage (V)')
    plt.title(title)
    plt.ylim(ylim)
    plt.grid(linestyle=grid_style, visible=True)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    x, y, label = make_sin(2, f=50.0, fe=1000.0, nT=2)
    plot(x, y, "s1 " + label)
    build_plot([-2, +2], "Une sinusoide ...")
