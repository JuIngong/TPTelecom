import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
import math

if __name__ == '__main__':
    SZ = 64  # taille de l'image
    SP = int(SZ / 2)  # Coordonnee max/min
    im = np.zeros((SZ, SZ), np.uint8)  # Image comme un tableau
    all_i = range(-SP, SP)
    all_j = range(-SP, SP)

    # fp periode sur une image
    fp = 4.0  # 1.0;2.0;4.0;8.0;16.0
    fr = fp / SZ  # frequence reduite
    for i in all_i:
        for j in all_j:
            im[i, j] = 128 + 128 * math.sin(2 * 3.14 * fr * i)

    plt.figure(1)
    plt.clf()
    plt.imshow(im, cmap=plt.cm.gray)

    IG, JG = np.meshgrid(all_i, all_j)
    fig = plt.figure(2)
    plt.clf()
    ax = Axes3D(fig)
    ax.plot_surface(IG, JG, im, rstride=1, cstride=1, cmap=cm.jet)
    plt.show()