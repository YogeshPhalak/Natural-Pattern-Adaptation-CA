import numpy as np
import cv2
from numba import jit, prange
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_w(w_):
    r = w_.shape[0] // 2
    fig = plt.figure('Weight Matrix')
    ax = fig.add_subplot(111, projection='3d')
    x, y = np.meshgrid(np.arange(-r, r + 1), np.arange(-r, r + 1))
    ax.plot_surface(x, y, w_, cmap='viridis')
    plt.show()


def youngs_weight():
    def w_r(r_):
        if r_ <= r:
            if r_ <= re:
                return we
            else:
                return wi
        else:
            return 0

    w = np.zeros((2 * r + 1, 2 * r + 1))
    for i in range(-r, r + 1):
        for j in range(-r, r + 1):
            r0 = (i ** 2 + j ** 2) ** 0.5
            w[i + r, j + r] = w_r(r0)
    return w


def radial_weight():
    w_r = lambda r: 1.1 * np.exp(-0.1 * r) * np.cos(0.6 * r)
    w = np.zeros((2 * r + 1, 2 * r + 1))
    for i in range(-r, r + 1):
        for j in range(-r, r + 1):
            w[i + r, j + r] = w_r((i ** 2 + j ** 2) ** 0.5)
    return w


def random_weight(r):
    w_ = np.random.rand(2 * r + 1, 2 * r + 1) * 2 - 1
    w_ = w_ * 4
    return w_


def weight_matrix():
    # return random_weight(r)
    # return radial_weight()
    # return youngs_weight()
    return np.load("data/w8.npy")
    # return np.load("data/w4.npy")
    # return np.load("data/w7.npy")
    # return np.load("data/w_.npy")


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
    im_w, im_h = 1000, 1000
    c = np.random.randint(0, 2, (m, n))
    re, r = 4, 12
    we, wi = 1, -0.1

    w = weight_matrix()
    plot_w(w)

    while True:
        c = update(c, w, True)
        img = cv2.resize(np.array(c * 255, dtype=np.uint8), (im_h, im_w), interpolation=cv2.INTER_NEAREST)
        cv2.imshow('Cellular Autometa Pattern', img)
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
            r += 1
            print('r:', r)
            w = weight_matrix()
        elif key == 81:
            r -= 1
            print('r:', r)
            w = weight_matrix()
        elif key == ord('s'):
            print('saving')
            cv2.imwrite('animal_coat' + str(np.random.randint(0, 1000)) + '.png', img)
        elif key == ord('p'):
            print('pause')
            cv2.waitKey(0)

    cv2.destroyAllWindows()
