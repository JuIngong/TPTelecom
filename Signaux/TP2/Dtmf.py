import math

import numpy as np

from Signaux.TP1.tp1_0 import build_plot
from Signaux.TP1.tp1_usingClasses import SinSig, Signal
from Signaux.TP2.tp2_1 import Melodie


# Obsolete
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
        self.sig_t.append(self.sig_t[len(self.sig_t) - 1])
        self.sig_s.append(0)
        self.sig_t.append(self.sig_t[len(self.sig_t) - 1] + 0.04)
        self.sig_s.append(0)


# Herite de signal et permet de construire un signal ajoutant le resultat de chaque formule
class Composite(Signal):
    def __init__(self, signals):
        super().__init__(signals[0].a, signals[0].f, signals[0].fe, signals[0].nT)
        self.signals = signals

    def formule(self, t):
        val = 0.
        for s in self.signals:
            val += s.formule(t)
        return val

    def formule_scal(self, t):
        val = 0.
        for s in self.signals:
            val += s.formule_scal(t)
        return val


if __name__ == '__main__':
    freq = [[941, 1336], [697, 1209], [697, 1336], [697, 1477],
            [770, 1209], [770, 1336], [770, 1477],
            [852, 1209], [852, 1336], [852, 1477]]

    in_mun = input("Number ? ")
    nums = list(in_mun)
    tmp = 0.

    # for num in nums:
    #     dtmf = Dtmf(100, freq[int(num)][0], freq[int(num)][1], 44100, duree=0.04)
    #     dtmf.make(tmp)
    #     dtmf.plot("b-", 3)
    #     tmp += 0.08

    sigs = []
    for num in nums:
        sigs.append(Composite(
            [SinSig(100, freq[int(num)][0], 44100, duree=0.04), SinSig(100, freq[int(num)][1], 44100, duree=0.04)]))
        sigs.append(SinSig(0, 100, 44100, duree=0.04))

    Melodie(sigs).build_melodie()

    build_plot([-300, +300], in_mun)
