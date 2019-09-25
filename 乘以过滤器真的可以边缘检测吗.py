# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：乘以过滤器真的可以边缘检测吗
   Description :
   Author : zhang
   date：2019/9/25
-------------------------------------------------
   Change Activity: 2019/9/25:
-------------------------------------------------
"""
__author__ = 'zhang'

import cv2
import numpy as np


def sumandmul(list1, list2):
    # result = sum(a*b for a, b in zip(list1, list2))
    result = np.sum(list1 * list2)
    return result


def conv(weight, height, count, newimg, t):
    while count:
        if height - count >= t:
            for i in range(0, weight):
                if i >= t and i <= weight-t:
                    newimg[i-t, height-count-t] = sumandmul(image[i-t:i+1, height-count-t: height-count+1], filter)

        if count == height:
            count -= t
        else:
            count -= 1

if __name__ == '__main__':
    # filter = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])  # 横向
    filter = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])  # 竖直方向

    image = cv2.imread('1.jpg', 0)
    weight, height = image.shape
    t = 2  # 2 = ? + 2 *0 -3 +1 = ? - 2
    newimg = np.zeros((int((weight + 2*0 - 3)/1 + 1), int((height + 2*0 - 3)/1 + 1)))
    count = height
    conv(weight, height, count, newimg, t)
    cv2.imshow('one', newimg)
    cv2.waitKey(0)



