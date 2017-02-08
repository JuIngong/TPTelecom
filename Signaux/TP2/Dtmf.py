import math

import numpy as np

from Signaux.TP1.tp1_0 import build_plot
from Signaux.TP1.tp1_usingClasses import SinSig


class Dtmf(SinSig):
    def __init__(self, a, f, f2, fe, nT=1, duree=None):
        self.nT = f * duree if duree is not None else nT
        super().__init__(a, f, fe, self.nT, duree=duree)
        self.f2 = f2

    def formule(self, t):
        omega = 2 * math.pi * self.f
        omega2 = 2 * math.pi * self.f2
        return self.a * np.sin((omega * t) + self.ph) + self.a * np.sin((omega2 * t) + self.ph)

    def make(self, offset=0):
        super().make(offset)
        self.sig_t.append(self.sig_t[len(self.sig_t)-1])
        self.sig_s.append(0)
        self.sig_t.append(self.sig_t[len(self.sig_t)-1]+0.04)
        self.sig_s.append(0)


if __name__ == '__main__':
    dtmf = Dtmf(100, 852, 1477, 44100, duree=0.04)
    dtmf.make()
    dtmf.plot("b-", 3)
    build_plot([-200, +200], "9")
