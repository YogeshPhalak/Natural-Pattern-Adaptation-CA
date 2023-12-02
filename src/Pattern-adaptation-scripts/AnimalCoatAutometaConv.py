import numpy as np
import cv2
from numba import jit, prange
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def w_r(r):
    if r <= ri:
        if r <= re:
            return we
        else:
            return wi
    else:
        return 0


def plot_w(w):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x, y = np.meshgrid(np.arange(-ri, ri + 1), np.arange(-ri, ri + 1))
    ax.plot_surface(x, y, w, cmap='viridis')
    plt.show()


def weight_matrix():
    # # random matrix varing from -1 to 1
    w = np.random.rand(2 * ri + 1, 2 * ri + 1) * 2 - 1
    # w = w * 4
    w = np.zeros((2 * ri + 1, 2 * ri + 1))
    for i in range(-ri, ri + 1):
        for j in range(-ri, ri + 1):
            r = (i ** 2 + j ** 2) ** 0.5
            w[i + ri, j + ri] = w_r(r)
    w = np.load("Data/w_.npy")
    # plot_w(w)
    return w


@jit(nopython=True, parallel=True)
def update(c_, w_, b_boundary=True):
    c_n = np.copy(c_)
    p, q = w_.shape
    if b_boundary:
        for i in prange(m):
            for j in prange(n):
                s = 0
                iy = i - p // 2
                jx = j - q // 2
                for im in prange(p):
                    for jm in prange(q):
                        s += c_[(im + iy) % m, (jm + jx) % n] * w_[im, jm]
                if s > 0:
                    c_n[i, j] = 1
                else:
                    c_n[i, j] = 0
    else:
        for i in prange(p // 2, m - p // 2):
            for j in prange(q // 2, n - q // 2):
                iy = i - p // 2
                jx = j - q // 2
                s = np.sum(c_[iy:iy + p, jx:jx + q] * w_)
                if s > 0:
                    c_n[i, j] = 1
                else:
                    c_n[i, j] = 0
    return c_n


if __name__ == "__main__":
    m, n = 512, 512
    c = np.random.randint(0, 2, (m, n))
    re, ri = 4, 25
    we, wi = 1, -0.1
    w = weight_matrix()
    while True:
        c = update(c, w, True)
        img = cv2.resize(np.array(c * 255, dtype=np.uint8), (512, 512), interpolation=cv2.INTER_NEAREST)
        cv2.imshow('YoungsModel', img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('r'):
            print('resetting')
            c = np.random.randint(0, 2, (m, n))
        elif key == 82:
            wi += 0.01
            print('wi:', wi)
            w = weight_matrix()
        elif key == 84:
            wi -= 0.01
            print('wi:', wi)
            w = weight_matrix()
        elif key == 83:
            ri += 1
            print('ri:', ri)
            w = weight_matrix()
        elif key == 81:
            ri -= 1
            print('ri:', ri)
            w = weight_matrix()
        elif key == ord('s'):
            print('saving')
            cv2.imwrite('animal_coat' + str(np.random.randint(0, 1000)) + '.png', img)
        elif key == ord('p'):
            print('pause')
            cv2.waitKey(0)

    cv2.destroyAllWindows()
