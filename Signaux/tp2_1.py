from Signaux.tp1_0 import build_plot
from Signaux.tp1_usingClasses import SinSig

if __name__ == '__main__':
    niv = 0.8
    s = SinSig(127.5 * niv, 440, 44100.0, duree=5)
    s.make()
    s.plot("b-", 3)

    build_plot([-110, +110], "La 440")
