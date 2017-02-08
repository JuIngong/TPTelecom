import math

from Signaux.TP1.tp1_0 import plot, build_plot, two_float


# generation de courbe carre
def make_sqr(a=1.0, f=440.0, fe=8000.0, nT=1):
    N = int(fe / f)
    te = 1.0 / fe
    sig_t = []
    sig_s = []
    for i in range(N * nT):
        t = te * i
        sig_t.append(t)
        # utilisation de la fonction  pour le point en y
        sig_s.append(2 * a * (2 * math.floor(f * t) - math.floor(2 * f * t) + 1) - a)

    # construction du label
    label = build_label(a, f, fe)
    return sig_t, sig_s, label


# generation de courbe à dent de scie
def make_saw(a=1.0, f=440.0, fe=8000.0, nT=1):
    N = int(fe / f)
    te = 1.0 / fe
    T = 1 / f
    sig_t = []
    sig_s = []
    for i in range(N * nT):
        t = te * i
        sig_t.append(t)
        # utilisation de la fonction  pour le point en y
        sig_s.append(2 * a * (t / T - math.floor(t / T) - 1 / 2))

    # construction du label
    label = build_label(a, f, fe)
    return sig_t, sig_s, label


# generation de courbe triangle
def make_tri(a=1.0, f=440.0, fe=8000.0, nT=1):
    N = int(fe / f)
    te = 1.0 / fe
    T = 1 / f
    sig_t = []
    sig_s = []
    for i in range(N * nT):
        t = te * i
        sig_t.append(t)
        # utilisation de la fonction  pour le point en y
        sig_s.append(a * (4 * (math.fabs(t / T - math.floor(t / T + 0.5))) - 1.0))

    # construction du label
    label = build_label(a, f, fe)
    return sig_t, sig_s, label


def build_label(a, f, fe):
    return "{0} Hz, {1} V, {2} fe".format(two_float(f), two_float(a), two_float(fe))


if __name__ == '__main__':
    x, y, label = make_sqr(3, 50.0, 1000.0, 3)
    plot(x, y, label, "-r.")
    # build_plot([-4, +4], "Un carre")

    x, y, label = make_saw(3, 50.0, 1000.0, 3)
    plot(x, y, label, "-b.")
    # build_plot([-3, +3], "Une Dent de scie")

    x, y, label = make_tri(3, 50.0, 1000.0, 3)
    plot(x, y, label, "-g.")
    # build_plot([-4, +4], "Un triangle")
    build_plot([-4, +4], "Des courbes")
