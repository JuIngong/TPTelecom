from Signaux.TP1.tp1_0 import build_plot
from Signaux.TP1.tp1_usingClasses import SinSig


def build_melodie(freqs):
    niv = 0.8
    tmp = 0.
    for f, t in freqs:
        s = SinSig(127.5 * niv, f, 44100.0, duree=t)
        s.make(tmp)
        s.plot("b-", 3)
        tmp += t


def la440():
    niv = 0.8
    s = SinSig(127.5 * niv, 440, 44100.0, duree=5)
    s.make()
    s.plot("b-", 3)


if __name__ == '__main__':
    freq = [[264, 0.01], [297, 0.03], [330, 0.04], [352, 0.01], [396, 0.02], [440, 0.01], [495, 0.05],
            [528, 0.01]]
    # build_melodie(freq)
    la440()
    build_plot([-110, +110], "La 440")
