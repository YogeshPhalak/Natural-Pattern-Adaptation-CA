import numpy as np
import cv2


def neighbors_non_empty(i, j, x_):
    nbr_idx = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]
    for idx in nbr_idx:
        if idx[0] < 0 or idx[0] >= n or idx[1] < 0 or idx[1] >= m:
            continue
        if x_[idx[0], idx[1]] != 0:
            return True


def neighbor_with_one(i, j, x_):
    nbr_idx = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]
    for idx in nbr_idx:
        if idx[0] < 0 or idx[0] >= n or idx[1] < 0 or idx[1] >= m:
            continue
        if x_[idx[0], idx[1]] == 1:
            return True


def step(x_, stages_=6):
    x_new_ = np.copy(x_)
    for i in range(n):
        for j in range(m):
            if x_[i, j] == 0:
                if neighbor_with_one(i, j, x_):
                    x_new_[i, j] = 1
            else:
                x_new_[i, j] = (x[i, j] + 1) % stages_
    return x_new_


def init_random(x_, num_=2, stages_=6):
    # drop some random 1s in 10 locations
    for _ in range(num_):
        i, j = np.random.randint(0, n), np.random.randint(0, m)
        x_[i, j] = np.random.randint(1, stages_)
    return x_


def init_pair(x_, stages_=6):
    x_[n // 2, m // 2 + 6] = 1
    x_[n // 2 + 1, m // 2] = 1
    return x_


if __name__ == '__main__':
    m, n = 100, 100
    stages = 6
    x = np.zeros((n, m))
    x = init_random(x, num_=1000, stages_=stages)
    # x = init_pair(x, stages_=stages)

    while True:
        x = step(x, stages_=stages)
        img = cv2.applyColorMap((x * 255 // stages).astype(np.uint8), cv2.COLORMAP_AUTUMN)
        img = cv2.resize(img, (512, 512), interpolation=cv2.INTER_LINEAR)
        cv2.imshow('spiral', img.astype(np.uint8))
        key = cv2.waitKey(500)
        if key == ord('q'):
            break
        elif key == ord('r'):
            print('resetting')
            x = np.zeros((n, m))
            x = init_random(x, num_=1000, stages_=stages)
        elif key == ord('s'):
            print('saving')
            cv2.imwrite('ExcitableAutometaSprialPair' + str(np.random.randint(0, 1000)) + '.png', img)
