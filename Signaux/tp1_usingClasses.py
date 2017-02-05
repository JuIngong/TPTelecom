import math
import numpy as np

from Signaux.tp1_0 import plot, build_plot
from Signaux.tp1_2 import build_label


class Signal:
    def __init__(self, a, f, fe, nT):
        self.a = a
        self.f = f
        self.fe = fe
        self.nT = nT

    def make(self):
        N = int(self.fe / self.f)
        te = 1.0 / self.fe
        sig_t = []
        sig_s = []
        return N, te, sig_t, sig_s


class SquareSig(Signal):
    def __init__(self, a, f, fe, nT):
        super().__init__(a, f, fe, nT)

    def make_scal(self):
        N, te, sig_t, sig_s = super().make()
        for i in range(N * self.nT):
            t = te * i
            sig_t.append(t)
            # utilisation de la fonction  pour le point en y
            sig_s.append(2 * self.a * (2 * math.floor(self.f * t) - math.floor(2 * self.f * t) + 1) - self.a)
        return sig_t, sig_s, " sqr : " + build_label(self.a, self.f, self.fe)


class SawSig(Signal):
    def __init__(self, a, f, fe, nT):
        super().__init__(a, f, fe, nT)

    def make_scal(self):
        N, te, sig_t, sig_s = super().make()
        T = 1 / self.f
        for i in range(N * self.nT):
            t = te * i
            sig_t.append(t)
            # utilisation de la fonction  pour le point en y
            sig_s.append(2 * self.a * (t / T - math.floor(t / T) - 1 / 2))
        return sig_t, sig_s, " saw : " + build_label(self.a, self.f, self.fe)


class TriSig(Signal):
    def __init__(self, a, f, fe, nT):
        super().__init__(a, f, fe, nT)

    def make_scal(self):
        N, te, sig_t, sig_s = super().make()
        T = 1 / self.f
        for i in range(N * self.nT):
            t = te * i
            sig_t.append(t)
            # utilisation de la fonction  pour le point en y
            sig_s.append(self.a * (4 * (math.fabs(t / T - math.floor(t / T + 0.5))) - 1.0))
        return sig_t, sig_s, " tri : " + build_label(self.a, self.f, self.fe)


class SinSig(Signal):
    def __init__(self, a, f, fe, nT, ph=0):
        super().__init__(a, f, fe, nT)
        self.ph = ph

    def make_scal(self):
        N, te, sig_t, sig_s = super().make()
        omega = 2 * math.pi * self.f
        for i in range(N * self.nT):
            t = te * i
            sig_t.append(t)
            sig_s.append(self.a * math.sin((omega * t) + self.ph))
        return sig_t, sig_s, " sin : " + build_label(self.a, self.f, self.fe)


if __name__ == '__main__':
    x, y, label = SquareSig(3, 50.0, 1000.0, 3).make_scal()
    plot(x, y, label, "-r.")

    x, y, label = SawSig(3, 50.0, 1000.0, 3).make_scal()
    plot(x, y, label, "-b.")

    x, y, label = TriSig(3, 50.0, 1000.0, 3).make_scal()
    plot(x, y, label, "-g.")

    x, y, label = SinSig(3, 50.0, 1000.0, 3).make_scal()
    plot(x, y, label, "-y.")

    build_plot([-4, +4], "Des courbes")
