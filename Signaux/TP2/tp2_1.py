from Signaux.TP1.tp1_0 import build_plot
from Signaux.TP1.tp1_usingClasses import SinSig, SquareSig


class Melodie:
    def __init__(self, signals):
        self.signals = signals

    # Assemblage de la melodie a partir de signaux passé dans le constructeur
    def build_melodie(self):
        tmp = 0.
        for s in self.signals:
            s.make(tmp)
            s.plot("-", 3)
            tmp += s.nT / s.f


def la440():
    niv = 0.8
    s = SinSig(127.5 * niv, 440, 44100.0, duree=5)
    s.make()
    s.plot("b-", 3)


if __name__ == '__main__':
    freq = [[264, 0.01], [297, 0.03], [330, 0.04], [352, 0.01], [396, 0.02], [440, 0.01], [495, 0.05],
            [528, 0.01]]
    signals = []
    for f, d in freq:
        signals.append(SinSig(127.5 * 0.8, f, 44100.0, duree=d))

    Melodie(signals).build_melodie()
    # la440()
    build_plot([-110, +110], "melodie")

