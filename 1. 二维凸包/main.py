import numpy as np
import matplotlib.pyplot as plt
import random
import time

import prettytable


def calcConvexHull(points):
    # sort rows according to x
    points = points[points[:, 0].argsort()]
    # 上半凸包
    ltop = [points[0], points[1]]
    for i in range(2, points.shape[0]):  # 依次插入每个点
        ltop.append(points[i])
        while len(ltop) >= 3:  # 检查最末尾三个点是否为右拐
            res = np.cross(ltop[-2] - ltop[-3], ltop[-1] - ltop[-3])
            if res[2] > 0:  # 倒数第二个点不构成凸包，删去
                ltop[-2] = ltop[-1]
                ltop.pop()
            else:  # 构成凸包，离开
                break

    # 下半凸包
    lbottom = [points[-1], points[-2]]
    for i in range(points.shape[0] - 3, -1, -1):  # 反向依次插入每个点
        lbottom.append(points[i])
        while len(lbottom) >= 3:  # 检查最末尾三个点是否为右拐
            res = np.cross(lbottom[-2] - lbottom[-3], lbottom[-1] - lbottom[-3])
            if res[2] > 0:  # 倒数第二个点不构成凸包，删去
                lbottom[-2] = lbottom[-1]
                lbottom.pop()
            else:  # 构成凸包，离开
                break

    return ltop, lbottom


# 性能测试
tb = prettytable.PrettyTable()
tb.field_names = ["Point Num", "Time Usage"]
for POINT_NUM in [20, 200, 2000, 20000]:
    points = np.array([
        [random.random() * 10, random.random() * 10, 0] for i in range(POINT_NUM)
    ])
    start = time.time()
    ltop, lbottom = calcConvexHull(points)
    end = time.time()
    tb.add_row([POINT_NUM, end - start])
print(tb)

# 绘制
POINT_NUM = 100
points = np.array([
    [random.random() * 10, random.random() * 10, 0] for i in range(POINT_NUM)
])
ltop, lbottom = calcConvexHull(points)

plt.scatter(points[:, 0], points[:, 1])
plt.plot([p[0] for p in ltop], [p[1] for p in ltop])
plt.plot([p[0] for p in lbottom], [p[1] for p in lbottom])
plt.show()
