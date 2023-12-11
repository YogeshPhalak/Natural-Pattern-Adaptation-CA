import numpy as np
import cv2


def neighbour_containing_one(i, j, x_, B_=1):
    nbr_idx = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]
    bs = 0
    for idx in nbr_idx:
        if idx[0] < 0 or idx[0] >= m or idx[1] < 0 or idx[1] >= n:
            continue
        p = idx[0]
        q = idx[1]

        if x_[p, q] == B_:
            bs += 1
    if bs == 1:
        return True


def neighbor_with_any(i, j, x_, F_=5):
    nbr_idx = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]
    for idx in nbr_idx:
        if idx[0] < 0 or idx[0] >= m or idx[1] < 0 or idx[1] >= n:
            continue
        p = idx[0]
        q = idx[1]

        if x_[p, q] == F_:
            return True


def step(x_, stages_, B_=1, F_=5):
    x_new = np.copy(x_)
    for i in range(m):
        for j in range(n):
            if x_[i, j] == B_ - 1:
                if neighbour_containing_one(i, j, x_, B_):
                    x_new[i, j] = B_
            elif x_[i, j] == F_ - 1:
                if neighbor_with_any(i, j, x_, F_):
                    x_new[i, j] = F_
            else:
                x_new[i, j] = (x_[i, j] + 1) % stages_
    return x_new


if __name__ == '__main__':
    m, n = 200, 200
    stages = 15

    x = np.random.randint(0, stages, (m, n))
    b = 2
    f = stages // 2 + 1

    while True:
        x = step(x, stages_=stages, B_=b, F_=f)
        img = cv2.applyColorMap((x * 255 // stages).astype(np.uint8), cv2.COLORMAP_HOT)
        img = cv2.resize(img, (512, 512), interpolation=cv2.INTER_LINEAR)
        cv2.imshow('img', img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('r'):
            print('resetting')
            x = np.random.randint(0, stages, (m, n))
        elif key == ord('s'):
            print('saving')
            cv2.imwrite('HostParasitoid' + str(np.random.randint(0, 1000)) + '.png', img)
