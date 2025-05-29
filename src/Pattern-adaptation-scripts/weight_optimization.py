import numpy as np
import cv2
from numba import jit, prange
from scipy.optimize import minimize

img = cv2.imread("data/4_processed.jpg")
filename = "data/w4.npy"
c_ = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# c_ = cv2.resize(c_, (256, 256), interpolation=cv2.INTER_NEAREST)
c_ = cv2.threshold(c_, 127, 1, cv2.THRESH_BINARY)[1]

m, n = c_.shape
r = 25
p, q = 2 * r + 1, 2 * r + 1


@jit(nopython=True, parallel=True)
def cost(x):
    global c_, m, n, p, q
    w_ = x.reshape((p, q))
    c_n = np.copy(c_)

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
    cst = np.sum((c_ - c_n) ** 2)
    # print(cst)
    return cst


def cust_opt(x0):
    cst_prev = cost(x0)
    x = np.copy(x0)
    cst0 = cst_prev
    it = 1000
    step = 0.001
    for i in range(it):
        for ix in range(len(x0)):
            x[ix] += step
            cst = cost(x)
            if cst > cst_prev:
                x[ix] -= step
                cst = cst_prev
            else:
                cst_prev = cst
            x[ix] -= step
            cst = cost(x)
            if cst > cst_prev:
                x[ix] += step
                cst = cst_prev
            else:
                cst_prev = cst
            print(cst)
            w = x.reshape((p, q))
            np.save(filename, w)
    return x


if __name__ == "__main__":
    # w = np.load("data/w4.npy")
    # x0 = w.reshape((p * q))
    x0 = np.random.rand(p * q) * 2 - 1
    # x0 = np.ones(p * q)
    # res = minimize(cost, x0, method='Nelder-Mead', tol=1e-6)
    # print(res.x)
    res = cust_opt(x0)
    # w = res.x.reshape((p, q))
    w = res.reshape((p, q))
    np.save(filename, w)
