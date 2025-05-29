import numpy as np
import cv2
from numba import jit, prange


def indices(re_, ri_):
    ri_indices = []
    re_indices = []
    for i in range(-ri_, ri_ + 1):
        for j in range(-ri_, ri_ + 1):
            r = i ** 2 + j ** 2
            if r <= ri_ ** 2:
                if r <= re_ ** 2:
                    re_indices.append([i, j])
                else:
                    ri_indices.append([i, j])
    return np.array(re_indices), np.array(ri_indices)


@jit(nopython=True, parallel=True)
def step(C_, we_, wi_, re_idx_, ri_idx_):
    C_new_ = np.copy(C_)
    for i in prange(m):
        for j in prange(n):
            sum_ = 0
            for idx in re_idx_:
                p, q = (i + idx[0]) % m, (j + idx[1]) % n
                sum_ += we_ * C_[p, q]

            for idx in ri_idx_:
                p, q = (i + idx[0]) % m, (j + idx[1]) % n
                sum_ += wi_ * C_[p, q]

            if sum_ > 0:
                C_new_[i, j] = 1
            else:
                C_new_[i, j] = 0
    return C_new_


if __name__ == "__main__":
    m, n = 512, 512
    C = np.random.randint(0, 2, (m, n))

    we = 1
    wi = -0.12
    re = 4
    ri = 12

    re_idx, ri_idx = indices(re, ri)

    while True:
        C = step(C, we, wi, re_idx, ri_idx)
        img = cv2.applyColorMap((C * 255).astype(np.uint8), cv2.COLORMAP_BONE)
        img = cv2.resize(img, (1000, 1000), interpolation=cv2.INTER_NEAREST)
        cv2.imshow('image', img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('r'):
            print('resetting')
            C = np.random.randint(0, 2, (m, n))
        elif key == 82:
            wi += 0.01
            print('wi:', wi)
            re_idx, ri_idx = indices(re, ri)
        elif key == 84:
            wi -= 0.01
            print('wi:', wi)
            re_idx, ri_idx = indices(re, ri)
        elif key == 83:
            ri += 1
            print('ri:', ri)
            re_idx, ri_idx = indices(re, ri)
        elif key == 81:
            ri -= 1
            print('ri:', ri)
            re_idx, ri_idx = indices(re, ri)
        elif key == ord('s'):
            print('saving')
            cv2.imwrite('animal_coat' + str(np.random.randint(0, 1000)) + '.png', img)
