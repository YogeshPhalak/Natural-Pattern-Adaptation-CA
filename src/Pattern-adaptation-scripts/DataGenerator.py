import numpy as np
import cv2

if __name__ == "__main__":
    n = 3
    img_raw = cv2.imread("Data/{}.jpg".format(n))
    img0 = cv2.resize(img_raw, (512, 512), interpolation=cv2.INTER_NEAREST)
    blr, mx, mn = 5, 255, 0

    while True:
        img = cv2.medianBlur(img0, blr)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.threshold(img, mn, mx, cv2.THRESH_BINARY)[1]
        cv2.imshow("Image", img)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
        elif k == ord('s'):
            cv2.imwrite("Data/{}_processed.jpg".format(n), img)
            n += 1
            blr, mx, mn = 5, 255, 0
            img_raw = cv2.imread("Data/{}.jpg".format(n))
            img0 = cv2.resize(img_raw, (512, 512), interpolation=cv2.INTER_NEAREST)
            print("Saved image {}".format(n))
        elif k == ord('B'):
            blr += 2
            print("Blur kernel size = {}".format(blr))
        elif k == ord('b'):
            blr -= 2
            print("Blur kernel size = {}".format(blr))
        elif k == ord('M'):
            mx += 1
            print("Max threshold = {}".format(mx))
        elif k == ord('m'):
            mx -= 1
            print("Max threshold = {}".format(mx))
        elif k == ord('N'):
            mn += 1
            print("Min threshold = {}".format(mn))
        elif k == ord('n'):
            mn -= 1
            print("Min threshold = {}".format(mn))

    cv2.destroyAllWindows()
