import random
import time

import numpy as np
import matplotlib.pyplot as plt
import prettytable


def calIntersection(x1, y1, x2, y2, x3, y3, x4, y4):
    # 线段为空
    if (x1 == x2 and y1 == y2) or (x3 == x4 and y3 == y4):
        return None
    try:
        res = np.linalg.solve(
            np.matrix([
                [y2 - y1, x1 - x2],
                [y4 - y3, x3 - x4]
            ]),
            np.matrix([
                [y2 * x1 - x2 * y1],
                [y4 * x3 - x4 * y3]
            ])
        )
    except:
        return None

    # 超出范围的也不行
    insectX = res.item((0, 0))
    if insectX < x1 and insectX < x2:
        return None
    if insectX > x1 and insectX > x2:
        return None
    if insectX < x3 and insectX < x4:
        return None
    if insectX > x3 and insectX > x4:
        return None

    return res

tb = prettytable.PrettyTable()
tb.field_names = ["Line Num", "Time Usage"]

for n in [10, 50, 100, 500, 1000]:
    points = [[], []]
    lines = []
    # 生成需要计算的线段
    for i in range(n):
        lines.append([random.random() * 100 for _ in range(4)])
    start = time.time()
    # 计算交点
    for i in range(n):
        for j in range(i + 1, n):
            res = calIntersection(lines[i][0], lines[i][1], lines[i][2], lines[i][3], lines[j][0], lines[j][1], lines[j][2], lines[j][3])
            if res is not None:
                points[0].append(res.item((0, 0)))
                points[1].append(res.item((1, 0)))
    end = time.time()
    tb.add_row([n, end-start])

    if n == 50:
        plt.scatter(points[0], points[1])
        for i in range(n):
            plt.plot([lines[i][0], lines[i][2]], [lines[i][1], lines[i][3]])

plt.show()
print(tb)



