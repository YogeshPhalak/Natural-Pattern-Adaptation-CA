import numpy as np
import cv2


def step(b_, w0_, w1_, w2_, th1_, th2_):
    b_new = np.copy(b_)
    b_c = np.zeros_like(b_)
    for i in range(m):
        for j in range(n):
            p = (m - i - 1) % m
            q = (n - j - 1) % n
            b_c[i, j] = b[p, q]
    # b_c = np.copy(b_)

    for i in range(m):
        for j in range(n):
            n_ = b_[(i - 1) % m, j]
            s_ = b_[(i + 1) % m, j]
            e_ = b_[i, (j + 1) % n]
            w_ = b_[i, (j - 1) % n]

            n_c = b_c[(i - 1) % m, j]
            s_c = b_c[(i + 1) % m, j]
            e_c = b_c[i, (j + 1) % n]
            w_c = b_c[i, (j - 1) % n]

            h = w0_ * b_c[i, j] + w1_ * (n_c + s_c + e_c + w_c) + w2_ * (n_ * e_c + n_ * w_c + s_ * e_c + s_ * w_c)
            # print(h)
            if th1_ <= h < th2_:
                b_new[i, j] = min(b_c[i, j] + 1, states - 1)
            else:
                b_new[i, j] = max(b_c[i, j] - 1, 0)

    return b_new


if __name__ == "__main__":
    m, n = 50, 50
    states = 16
    b = np.random.randint(0, states, (m, n))
    # C = np.ones((m, n))

    w0 = 0.5
    w1 = 0.12
    w2 = 0.3
    th1 = 5
    th2 = 25

    while True:
        b = step(b, w0, w1, w2, th1, th2)
        img = cv2.applyColorMap((b * 255).astype(np.uint8), cv2.COLORMAP_JET)
        img = cv2.resize(img, (1000, 1000), interpolation=cv2.INTER_NEAREST)
        cv2.imshow("img", img)
        key = cv2.waitKey(10)
        if key == ord('q'):
            break
        elif key == ord('r'):
            print('resetting')
            b = np.random.randint(0, states, (m, n))
        elif key == ord('s'):
            print('saving')
            cv2.imwrite('immunological_model' + str(np.random.randint(0, 1000)) + '.png', img)
