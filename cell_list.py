# -*- coding = utf8 -*-

import numpy as np
import random
from memory_profiler import profile


class CellList:
    """CellList.

    细胞网格类，所有细胞都处在一个长x 宽y的二维数组中.
    """

    def __init__(self, num):
        """构造函数.

        @param num: 输入生成的网格边长
        """
        self.cell_list = []
        self.num = num
        for i in range(num + 2):
            self.cell_list.append([])
            for j in range(num + 2):
                self.cell_list[i].append(0)
        print('nit=', self.cell_list)

    def set_example(self):
        """设置初始结构.

        @return: None
        """
        for i in range(1, self.num + 1):
            for j in range(1, self.num + 1):
                self.cell_list[i][j] = int(random.random() > 0.5)

        # 稳定方格
        # self.cell_list[0][0] = 1
        # self.cell_list[0][1] = 1
        # self.cell_list[1][0] = 1
        # self.cell_list[1][1] = 1
        # 滑翔机
        # self.cell_list[1][1] = 1
        # self.cell_list[1][3] = 1
        # self.cell_list[2][2] = 1
        # self.cell_list[2][3] = 1
        # self.cell_list[3][2] = 1

        # for i in range(12):
        #     for j in range(12):
        #         print(self.cell_list[i][j], end=' ')
        #     print()
        # print()

    def get_cell_list(self):
        """获取celllist.

        :return: 返回已创建的2为数组
        """
        return self.cell_list

    def get_cell_width(self):
        """获取长度.

        @return: 返回生成区域的边长
        """
        return self.num

    @profile
    def change_life(self):
        """更新细胞状态.

        @return: 返回了更新后的状态
        """

        next_one = []
        for i in range(self.num + 2):
            next_one.append([])
            for j in range(self.num + 2):
                next_one[i].append(0)

        for i in range(1, self.num + 1):
            for j in range(1, self.num + 1):
                summary = self.cell_list[i][j - 1] + \
                          self.cell_list[i][j + 1] + \
                          self.cell_list[i - 1][j - 1] \
                          + self.cell_list[i - 1][j] + \
                          self.cell_list[i - 1][j + 1] + \
                          self.cell_list[i + 1][j - 1] + \
                          self.cell_list[i + 1][j] + \
                          self.cell_list[i + 1][j + 1]
                # 由死亡条件，列真值表进行逻辑电路分析 sum==3 sum==2 alive[][]==true
                if summary == 3:
                    next_one[i][j] = 1
                elif summary == 2:
                    next_one[i][j] = self.cell_list[i][j]
                else:
                    next_one[i][j] = 0
        print('next_one=', next_one)
        print('len_next_one=', len(next_one))
        print('len=', len(self.cell_list))
        self.cell_list.clear()
        self.cell_list = next_one.copy()
        print('cell_list=', self.cell_list)
        return next_one
