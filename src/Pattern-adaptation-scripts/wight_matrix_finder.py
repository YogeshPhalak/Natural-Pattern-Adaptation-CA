import numpy as np
import cv2
import tqdm
from numba import jit, prange


@jit(nopython=True, parallel=True)
def find_optimal_wights(c, r=20):
    m, n = c.shape
    p, q = 2 * r + 1, 2 * r + 1
    w = np.zeros((2 * r + 1, 2 * r + 1))

    CX = np.zeros((m * n, p * q))
    Y = np.zeros(m * n)

    # bar = tqdm.tqdm(total=m * n)
    for i in prange(m):
        for j in prange(n):
            s = 0
            iy = i - p // 2
            jx = j - q // 2

            cxi = np.zeros(p * q)
            cx_idx = 0
            for im in range(p):
                for jm in range(q):
                    cxi[cx_idx] = c[(im + iy) % m, (jm + jx) % n]
                    cx_idx += 1

            CX[i * n + j] = cxi
            Y[i * n + j] = c[i, j]
            # bar.update(1)

    w = np.linalg.pinv(CX) @ Y
    w = w.reshape((p, q))
    return w


if __name__ == "__main__":
    img = cv2.imread("Data/animal_coat49.png")
    # convert to 0 and 1 matrix
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    C = cv2.threshold(img, 127, 1, cv2.THRESH_BINARY)[1]
    # find optimal wights
    w = find_optimal_wights(C, 20)
    print(w)
    np.save("Data/w.npy", w)
