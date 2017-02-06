import math
from abc import abstractmethod, ABCMeta

import matplotlib.pyplot as plt
import numpy as np

from Signaux.tp1_0 import build_plot


# Classe mère des signaux
class Signal(metaclass=ABCMeta):
    def __init__(self, a, f, fe, nT):
        self.a = a
        self.f = f
        self.fe = fe
        self.nT = nT

        self.N = int(self.fe / self.f)
        self.te = 1.0 / self.fe
        self.sig_t = []
        self.sig_s = []
        self.label = ""

    # construction du signal de facon vectoriel
    def make(self):
        n = np.arange(self.N * self.nT)
        t = self.te * n
        self.sig_t = t.tolist()

        # vectorisation de la fonction formule
        # f = np.vectorize(self.formule, otypes=[np.float])
        self.sig_s = self.formule(t).tolist()

    # generation de formule
    @abstractmethod
    def formule(self, t):
        return

    # generation de formule scal
    @abstractmethod
    def formule_scal(self, t):
        return

    # construction du signal de facon scalaire
    def make_scal(self):
        for i in range(self.N * self.nT):
            t = self.te * i
            self.sig_t.append(t)
            # utilisation de la fonction  pour le point en y
            self.sig_s.append(self.formule_scal(t))

    # methode de construction de label
    def build_label(self):
        return "{0} Hz, {1} V, {2} fe".format(self.two_float(self.f), self.two_float(self.a), self.two_float(self.fe))

    # methode de mise en forme des float
    def two_float(self, value):
        return ("{:.2f}".format(value)).rstrip('0').rstrip('.')

    def plot(self, format='-bo', size=7):
        plt.plot(self.sig_t, self.sig_s, format, markersize=size, label=self.build_label())  # Classe de signaux carré


class SquareSig(Signal):
    def formule_scal(self, t):
        return 2 * self.a * (2 * math.floor(self.f * t) - math.floor(2 * self.f * t) + 1) - self.a

    def formule(self, t):
        return 2 * self.a * (2 * np.floor(self.f * t) - np.floor(2 * self.f * t) + 1) - self.a


# Classe de signaux dent de scie
class SawSig(Signal):
    def formule_scal(self, t):
        T = 1 / self.f
        return 2 * self.a * (t / T - math.floor(t / T) - 1 / 2)

    def formule(self, t):
        T = 1 / self.f
        return 2 * self.a * (t / T - np.floor(t / T) - 1 / 2)


# Classe de signaux triangle
class TriSig(Signal):
    def formule_scal(self, t):
        T = 1 / self.f
        return self.a * (4 * (math.fabs(t / T - math.floor(t / T + 0.5))) - 1.0)

    def formule(self, t):
        T = 1 / self.f
        return self.a * (4 * (np.fabs(t / T - np.floor(t / T + 0.5))) - 1.0)


# Classe de signaux sinusoide
class SinSig(Signal):
    def __init__(self, a, f, fe, nT=1, ph=0., duree=None):
        self.nT = f * duree if duree is not None else nT
        super().__init__(a, f, fe, self.nT)
        self.ph = ph

    def formule_scal(self, t):
        omega = 2 * math.pi * self.f
        return self.a * math.sin((omega * t) + self.ph)

    def formule(self, t):
        omega = 2 * math.pi * self.f
        return self.a * np.sin((omega * t) + self.ph)

    # ajout de ph au build label parent
    def build_label(self):
        return super().build_label() + ", {0} ph".format(self.two_float(self.ph))


if __name__ == '__main__':
    sqr = SquareSig(3, 50.0, 1000.0, 3)
    sqr.make()
    sqr.plot("-r.")

    saw = SawSig(3, 50.0, 1000.0, 3)
    saw.make()
    saw.plot("-b.")

    tri = TriSig(3, 50.0, 1000.0, 3)
    tri.make()
    tri.plot("-g.")

    sin = SinSig(3, 50.0, 1000.0, 3, math.pi)
    sin.make()
    sin.plot("-y.")

    build_plot([-4, +4], "Des courbes")
