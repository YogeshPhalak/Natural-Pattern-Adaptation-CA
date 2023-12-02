import numpy as np
import cv2


def any_fish(i_, j_, f_):
    nbr_idx = [[i_ - 1, j_], [i_ + 1, j_], [i_, j_ - 1], [i_, j_ + 1]]
    for idx in nbr_idx:
        if idx[0] < 0 or idx[0] >= m or idx[1] < 0 or idx[1] >= n:
            continue
        p = idx[0] % m
        q = idx[1] % n
        if f_[p, q] == 1:
            return True


def any_mother_shark(i_, j_, f_):
    nbr_idx = [[i_ - 1, j_], [i_ + 1, j_], [i_, j_ - 1], [i_, j_ + 1]]
    for idx in nbr_idx:
        if idx[0] < 0 or idx[0] >= m or idx[1] < 0 or idx[1] >= n:
            continue
        p = idx[0] % m
        q = idx[1] % n
        if f_[p, q] == 7:
            return True


def step(f_, stages_=8):
    f_new = np.copy(f_)
    # 0= empty, 1= fish, 2= shark2, 3= shark3, 4= shark4, 5= shark5, 6= shark6, 7= mother shark
    for i in range(m):
        for j in range(n):
            if f_[i, j] == 0:
                if any_fish(i, j, f_):
                    f_new[i, j] = 1
                elif any_mother_shark(i, j, f_):
                    f_new[i, j] = 2
            elif f_[i, j] == 1:
                if any_mother_shark(i, j, f_):
                    f_new[i, j] = 2
            elif f_[i, j] != 0 and f_[i, j] % 2 == 0:
                if not any_fish(i, j, f_):
                    f_new[i, j] = 0
                else:
                    f_new[i, j] = f_[i, j] + 1
            elif f_[i, j] != 7 and f_[i, j] % 2 == 1:
                if any_fish(i, j, f_):
                    f_new[i, j] = f_[i, j] + 1
                else:
                    f_new[i, j] = f_[i, j] + 1
            elif f_[i, j] == 7:
                if any_fish(i, j, f_):
                    f_new[i, j] = 2
                else:
                    f_new[i, j] = 2

    return f_new


if __name__ == '__main__':
    m, n = 100, 100
    stages = 8
    # f = np.zeros((m, n))
    f = np.random.randint(0, stages, (m, n))

    while True:
        f = step(f, stages_=stages)
        # print(f[0,0])

        img = cv2.applyColorMap((f * 255 // stages).astype(np.uint8), cv2.COLORMAP_JET)
        img = cv2.resize(img, (1000, 1000), interpolation=cv2.INTER_NEAREST)
        cv2.imshow("img", img)
        key = cv2.waitKey(10)
        if key == ord('q'):
            break
        elif key == ord('r'):
            print('resetting')
            f = np.random.randint(0, stages, (m, n))
        elif key == ord('s'):
            print('saving')
            cv2.imwrite('fish_shark' + str(np.random.randint(0, 1000)) + '.png', img)
