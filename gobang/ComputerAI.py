"""
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2019/2/21
@Program      : 实现电脑下棋的决策ai算法
"""
import random

from gobang import ROW, COL


def ai_scan(chess_array):
    blackPoint = {}
    whitePoint = {}

    for x in range(ROW):
        for y in range(COL):
            defance = 0
            attack = 0
            # 如果当前不是空的，是有棋子的，就当前的坐标格不用做计算。
            if chess_array[x][y] != None:
                continue
            # 判断各种形状形成的权重，来作为ai落子的参考
            # |竖
            if (y + 4) < COL and chess_array[x][y + 1] == 'black' and chess_array[x][y + 2] == 'black' and \
                    chess_array[x][y + 3] == 'black' and chess_array[x][y + 4] == 'black':
                defance += 4
            elif (y + 3) < COL and chess_array[x][y + 1] == 'black' and chess_array[x][y + 2] == 'black' and \
                    chess_array[x][y + 3] == 'black':
                defance += 2
            elif (y + 2) < COL and chess_array[x][y + 1] == 'black' and chess_array[x][y + 2] == 'black':
                defance += 1

            if (y + 4) < COL and chess_array[x][y + 1] == 'white' and chess_array[x][y + 2] == 'white' and \
                    chess_array[x][y + 3] == 'white' and chess_array[x][y + 4] == 'white':
                attack += 8
            elif (y + 3) < COL and chess_array[x][y + 1] == 'white' and chess_array[x][y + 2] == 'white' and \
                    chess_array[x][y + 3] == 'white':
                attack += 2
            elif (y + 2) < COL and chess_array[x][y + 1] == 'white' and chess_array[x][y + 2] == 'white':
                attack += 1

            if (y - 4) > 0 and chess_array[x][y - 1] == 'black' and chess_array[x][y - 2] == 'black' and \
                    chess_array[x][y - 3] == 'black' and chess_array[x][y - 3] == 'black':
                defance += 8
            elif (y - 3) > 0 and chess_array[x][y - 1] == 'black' and chess_array[x][y - 2] == 'black' and \
                    chess_array[x][y - 3] == 'black':
                defance += 2
            elif (y - 2) > 0 and chess_array[x][y - 1] == 'black' and chess_array[x][y - 2] == 'black':
                defance += 1

            if (y - 4) > 0 and chess_array[x][y - 1] == 'white' and chess_array[x][y - 2] == 'white' and \
                    chess_array[x][y - 3] == 'white' and chess_array[x][y - 4] == 'white':
                attack += 8
            elif (y - 3) > 0 and chess_array[x][y - 1] == 'white' and chess_array[x][y - 2] == 'white' and \
                    chess_array[x][y - 3] == 'white':
                attack += 4
            elif (y - 2) > 0 and chess_array[x][y - 1] == 'white' and chess_array[x][y - 2] == 'white':
                attack += 1

            # -横
            if (x + 4) < ROW and chess_array[x + 1][y] == 'black' and chess_array[x + 2][y] == 'black' and \
                    chess_array[x + 3][y] == 'black' and chess_array[x + 4][y] == 'black':
                defance += 8
            elif (x + 3) < ROW and chess_array[x + 1][y] == 'black' and chess_array[x + 2][y] == 'black' and \
                    chess_array[x + 3][y] == 'black':
                defance += 2
            elif (x + 2) < ROW and chess_array[x + 1][y] == 'black' and chess_array[x + 2][y] == 'black':
                defance += 1

            if (x + 4) < ROW and chess_array[x + 1][y] == 'white' and chess_array[x + 2][y] == 'white' and \
                    chess_array[x + 3][y] == 'white' and chess_array[x + 4][y] == 'white':
                attack += 8
            elif (x + 3) < ROW and chess_array[x + 1][y] == 'white' and chess_array[x + 2][y] == 'white' and \
                    chess_array[x + 3][y] == 'white':
                attack += 4
            elif (x + 2) < ROW and chess_array[x + 1][y] == 'white' and chess_array[x + 2][y] == 'white':
                attack += 1

            if (x - 4) > 0 and chess_array[x - 1][y] == 'black' and chess_array[x - 2][y] == 'black' and \
                    chess_array[x - 3][y] == 'black' and chess_array[x - 4][y] == 'black':
                defance += 8
            elif (x - 3) > 0 and chess_array[x - 1][y] == 'black' and chess_array[x - 2][y] == 'black' and \
                    chess_array[x - 3][y] == 'black':
                defance += 2
            elif (x - 2) > 0 and chess_array[x - 1][y] == 'black' and chess_array[x - 2][y] == 'black':
                defance += 1

            if (x - 4) > 0 and chess_array[x - 1][y] == 'white' and chess_array[x - 2][y] == 'white' and \
                    chess_array[x - 3][y] == 'white' and chess_array[x - 4][y] == 'white':
                attack += 8
            elif (x - 3) > 0 and chess_array[x - 1][y] == 'white' and chess_array[x - 2][y] == 'white' and \
                    chess_array[x - 3][y] == 'white':
                attack += 4
            elif (x - 2) > 0 and chess_array[x - 1][y] == 'white' and chess_array[x - 2][y] == 'white':
                attack += 1

            # \斜
            if (y + 4) < COL and (x + 4) < ROW and chess_array[x + 1][y + 1] == 'black' and \
                    chess_array[x + 2][y + 2] == 'black' and chess_array[x + 3][y + 3] == 'black' and \
                    chess_array[x + 4][y + 4] == 'black':
                defance += 8
            elif (y + 3) < COL and (x + 3) < ROW and chess_array[x + 1][y + 1] == 'black' and \
                    chess_array[x + 2][y + 2] == 'black' and chess_array[x + 3][y + 3] == 'black':
                defance += 2
            elif (y + 2) < COL and (x + 2) < ROW and chess_array[x + 1][y + 1] == 'black' and \
                    chess_array[x + 2][y + 2] == 'black':
                defance += 1

            if (y + 4) < COL and (x + 4) < ROW and chess_array[x + 1][y + 1] == 'white' and \
                    chess_array[x + 2][y + 2] == 'white' and chess_array[x + 3][y + 3] == 'white' and \
                    chess_array[x + 4][y + 4] == 'white':
                attack += 8
            elif (y + 3) < COL and (x + 3) < ROW and chess_array[x + 1][y + 1] == 'white' and \
                    chess_array[x + 2][y + 2] == 'white' and chess_array[x + 3][y + 3] == 'white':
                attack += 4
            elif (y + 2) < COL and (x + 2) < ROW and chess_array[x + 1][y + 1] == 'white' and \
                    chess_array[x + 2][y + 2] == 'white':
                attack += 1

            if (y - 4) > 0 and (x - 4) > 0 and chess_array[x - 1][y - 1] == 'black' and \
                    chess_array[x - 2][y - 2] == 'black' and chess_array[x - 3][y - 3] == 'black' and \
                    chess_array[x - 4][y - 4] == 'black':
                defance += 8
            elif (y - 3) > 0 and (x - 3) > 0 and chess_array[x - 1][y - 1] == 'black' and \
                    chess_array[x - 2][y - 2] == 'black' and chess_array[x - 3][y - 3] == 'black':
                defance += 2
            elif (y - 2) > 0 and (x - 2) > 0 and chess_array[x - 1][y - 1] == 'black' and \
                    chess_array[x - 2][y - 2] == 'black':
                defance += 1

            if (y - 4) > 0 and (x - 4) > 0 and chess_array[x - 1][y - 1] == 'white' and \
                    chess_array[x - 2][y - 2] == 'white' and chess_array[x - 3][y - 3] == 'white' and \
                    chess_array[x - 4][y - 4] == 'white':
                attack += 8
            elif (y - 3) > 0 and (x - 3) > 0 and chess_array[x - 1][y - 1] == 'white' and \
                    chess_array[x - 2][y - 2] == 'white' and chess_array[x - 3][y - 3] == 'white':
                attack += 4
            elif (y - 2) > 0 and (x - 2) > 0 and chess_array[x - 1][y - 1] == 'white' and \
                    chess_array[x - 2][y - 2] == 'white':
                attack += 1

            # /斜
            if (y - 4) > 0 and (x + 4) < ROW and chess_array[x + 1][y - 1] == 'black' and \
                    chess_array[x + 2][y - 2] == 'black' and chess_array[x + 3][y - 3] == 'black' and \
                    chess_array[x + 4][y - 4] == 'black':
                defance += 8
            elif (y - 3) > 0 and (x + 3) < ROW and chess_array[x + 1][y - 1] == 'black' and \
                    chess_array[x + 2][y - 2] == 'black' and chess_array[x + 3][y - 3] == 'black':
                defance += 2
            elif (y - 2) > 0 and (x + 2) < ROW and chess_array[x + 1][y - 1] == 'black' and \
                    chess_array[x + 2][y - 2] == 'black':
                defance += 1

            if (y - 4) > 0 and (x + 4) < ROW and chess_array[x + 1][y - 1] == 'white' and \
                    chess_array[x + 2][y - 2] == 'white' and chess_array[x + 3][y - 3] == 'white' and \
                    chess_array[x + 4][y - 4] == 'white':
                attack += 8
            elif (y - 3) > 0 and (x + 3) < ROW and chess_array[x + 1][y - 1] == 'white' and \
                    chess_array[x + 2][y - 2] == 'white' and chess_array[x + 3][y - 3] == 'white':
                attack += 4
            elif (y - 2) > 0 and (x + 2) < ROW and chess_array[x + 1][y - 1] == 'white' and \
                    chess_array[x + 2][y - 2] == 'white':
                attack += 1

            if (y + 4) < COL and (x - 4) > 0 and chess_array[x - 1][y + 1] == 'black' and \
                    chess_array[x - 2][y + 2] == 'black' and chess_array[x - 3][y + 3] == 'black' and \
                    chess_array[x - 4][y + 4] == 'black':
                defance += 8
            elif (y + 3) < COL and (x - 3) > 0 and chess_array[x - 1][y + 1] == 'black' and \
                    chess_array[x - 2][y + 2] == 'black' and chess_array[x - 3][y - 3] == 'black':
                defance += 2
            elif (y + 2) < COL and (x - 2) > 0 and chess_array[x - 1][y + 1] == 'black' and \
                    chess_array[x - 2][y + 2] == 'black':
                defance += 1

            if (y + 4) < COL and (x - 4) > 0 and chess_array[x - 1][y + 1] == 'white' and \
                    chess_array[x - 2][y + 2] == 'white' and chess_array[x - 3][y + 3] == 'white' and \
                    chess_array[x - 4][y + 4] == 'white':
                attack += 8
            elif (y + 3) < COL and (x - 3) > 0 and chess_array[x - 1][y + 1] == 'white' and \
                    chess_array[x - 2][y + 2] == 'white' and chess_array[x - 3][y + 3] == 'white':
                attack += 4
            elif (y + 2) < COL and (x - 2) > 0 and chess_array[x - 1][y + 1] == 'white' and \
                    chess_array[x - 2][y + 2] == 'white':
                attack += 1

            # 各种卡在中间的情况，例如：xoxx，xxoxx，xxox等
            # 检测黑色
            # -
            if (x - 2) > 0 and (x + 1) < ROW and chess_array[x + 1][y] == 'black' and chess_array[x - 1][y] == 'black' \
                    and chess_array[x - 2][y] == 'black':
                defance += 4
            if (x - 1) > 0 and (x + 2) < ROW and chess_array[x - 1][y] == 'black' and chess_array[x + 1][y] == 'black' \
                    and chess_array[x + 2][y] == 'black':
                defance += 4
            if (x - 2) > 0 and (x + 2) < ROW and chess_array[x - 1][y] == 'black' and chess_array[x - 2][y] == 'black' \
                    and chess_array[x + 1][y] == 'black' and chess_array[x + 2][y] == 'black':
                defance += 8
            # |
            if (y - 2) > 0 and (y + 1) < COL and chess_array[x][y + 1] == 'black' and chess_array[x][y - 1] == 'black' \
                    and chess_array[x][y - 2] == 'black':
                defance += 4
            if (y - 1) > 0 and (y + 2) < COL and chess_array[x][y - 1] == 'black' and chess_array[x][y + 1] == 'black' \
                    and chess_array[x][y + 2] == 'black':
                defance += 4
            if (y - 2) > 0 and (y + 2) < COL and chess_array[x][y - 1] == 'black' and chess_array[x][y - 2] == 'black' \
                    and chess_array[x][y + 1] == 'black' and chess_array[x][y + 2] == 'black':
                defance += 8
            # \
            if (x - 2) > 0 and (x + 1) < ROW and (y - 2) > 0 and (y + 1) < COL and chess_array[x + 1][y + 1] == 'black' \
                    and chess_array[x - 1][y - 1] == 'black' and chess_array[x - 2][y - 2] == 'black':
                defance += 4
            if (x - 1) > 0 and (x + 2) < ROW and (y - 1) > 0 and (y + 2) < COL and chess_array[x - 1][y - 1] == 'black' \
                    and chess_array[x + 1][y + 1] == 'black' and chess_array[x + 2][y + 2] == 'black':
                defance += 4
            if (x - 2) > 0 and (x + 2) < ROW and (y - 2) > 0 and (y + 2) < COL and chess_array[x - 1][y - 1] == 'black' \
                    and chess_array[x - 2][y - 2] == 'black' and chess_array[x + 1][y + 1] == 'black' and \
                    chess_array[x + 2][y + 2] == 'black':
                defance += 8
            # /
            if (x - 1) > 0 and (x + 2) < ROW and (y - 2) > 0 and (y + 1) < COL and chess_array[x - 1][y + 1] == 'black' \
                    and chess_array[x + 1][y - 1] == 'black' and chess_array[x + 2][y - 2] == 'black':
                defance += 4
            if (x - 2) > 0 and (x + 1) < ROW and (y - 1) > 0 and (y + 2) < COL and chess_array[x + 1][y - 1] == 'black' \
                    and chess_array[x - 1][y + 1] == 'black' and chess_array[x - 2][y + 2] == 'black':
                defance += 4
            if (x - 2) > 0 and (x + 2) < ROW and (y - 2) > 0 and (y + 2) < COL and chess_array[x + 1][y - 1] == 'black' \
                    and chess_array[x + 2][y - 2] == 'black' and chess_array[x - 1][y + 1] == 'black' and \
                    chess_array[x - 2][y + 2] == 'black':
                defance += 8

                # 检测白色
                # -
                if (x - 2) > 0 and (x + 1) < ROW and chess_array[x + 1][y] == 'white' and chess_array[x - 1][
                    y] == 'white' \
                        and chess_array[x - 2][y] == 'white':
                    defance += 4
                if (x - 1) > 0 and (x + 2) < ROW and chess_array[x - 1][y] == 'white' and chess_array[x + 1][
                    y] == 'white' \
                        and chess_array[x + 2][y] == 'white':
                    defance += 4
                if (x - 2) > 0 and (x + 2) < ROW and chess_array[x - 1][y] == 'white' and chess_array[x - 2][
                    y] == 'white' \
                        and chess_array[x + 1][y] == 'white' and chess_array[x + 2][y] == 'white':
                    defance += 8
                # |
                if (y - 2) > 0 and (y + 1) < COL and chess_array[x][y + 1] == 'white' and chess_array[x][
                    y - 1] == 'white' \
                        and chess_array[x][y - 2] == 'white':
                    defance += 4
                if (y - 1) > 0 and (y + 2) < COL and chess_array[x][y - 1] == 'white' and chess_array[x][
                    y + 1] == 'white' \
                        and chess_array[x][y + 2] == 'white':
                    defance += 4
                if (y - 2) > 0 and (y + 2) < COL and chess_array[x][y - 1] == 'white' and chess_array[x][
                    y - 2] == 'white' \
                        and chess_array[x][y + 1] == 'white' and chess_array[x][y + 2] == 'white':
                    defance += 8
                # \
                if (x - 2) > 0 and (x + 1) < ROW and (y - 2) > 0 and (y + 1) < COL and chess_array[x + 1][
                    y + 1] == 'white' \
                        and chess_array[x - 1][y - 1] == 'white' and chess_array[x - 2][y - 2] == 'white':
                    defance += 4
                if (x - 1) > 0 and (x + 2) < ROW and (y - 1) > 0 and (y + 2) < COL and chess_array[x - 1][
                    y - 1] == 'white' \
                        and chess_array[x + 1][y + 1] == 'white' and chess_array[x + 2][y + 2] == 'white':
                    defance += 4
                if (x - 2) > 0 and (x + 2) < ROW and (y - 2) > 0 and (y + 2) < COL and chess_array[x - 1][
                    y - 1] == 'white' \
                        and chess_array[x - 2][y - 2] == 'white' and chess_array[x + 1][y + 1] == 'white' and \
                        chess_array[x + 2][y + 2] == 'white':
                    defance += 8
                # /
                if (x - 1) > 0 and (x + 2) < ROW and (y - 2) > 0 and (y + 1) < COL and chess_array[x - 1][
                    y + 1] == 'white' \
                        and chess_array[x + 1][y - 1] == 'white' and chess_array[x + 2][y - 2] == 'white':
                    defance += 4
                if (x - 2) > 0 and (x + 1) < ROW and (y - 1) > 0 and (y + 2) < COL and chess_array[x + 1][
                    y - 1] == 'white' \
                        and chess_array[x - 1][y + 1] == 'white' and chess_array[x - 2][y + 2] == 'white':
                    defance += 4
                if (x - 2) > 0 and (x + 2) < ROW and (y - 2) > 0 and (y + 2) < COL and chess_array[x + 1][
                    y - 1] == 'white' \
                        and chess_array[x + 2][y - 2] == 'white' and chess_array[x - 1][y + 1] == 'white' and \
                        chess_array[x - 2][y + 2] == 'white':
                    defance += 8

            if defance not in blackPoint.keys():
                blackPoint[defance] = []
            blackPoint[defance].append((x, y))

            if attack not in whitePoint.keys():
                whitePoint[attack] = []
            whitePoint[attack].append((x, y))

    maxBlack = 0
    maxWhite = 0
    for i in blackPoint.keys():
        if i > maxBlack:
            maxBlack = i

    for i in whitePoint.keys():
        if i > maxWhite:
            maxWhite = i

    if maxBlack > maxWhite:
        if len(blackPoint[maxBlack]) == 1:
            x, y = blackPoint[maxBlack][0]
        else:
            x, y = random.choice(blackPoint[maxBlack])
    else:
        if len(whitePoint[maxWhite]) == 1:
            #
            x, y = whitePoint[maxWhite][0]
        elif len(whitePoint[maxWhite]) == 224 and chess_array[7][7] == None:
            # 这个判断的意义在于，如果黑子落子正中间的位置，则白子抢占这个位置，数组长度224表示只有黑子下了一子属于判断白子第一步的位置
            x, y = 7, 7
        elif len(whitePoint[maxWhite]) > 221:
            # 如果白子权重数组的长度大于221，黑子之前的两步是在任意位置，没有形成构成威胁的直线的联系。
            x, y = random.choice([(6, 6), (6, 7), (6, 8), (7, 6), (7, 8), (8, 6), (8, 7), (8, 8)])
            while not chess_array[x][y] == None:
                # 这里需要判断选择的点是不是有棋子，如果有的话，就重新选择另外一个点
                x, y = random.choice([(6, 6), (6, 7), (6, 8), (7, 6), (7, 8), (8, 6), (8, 7), (8, 8)])
        else:
            x, y = random.choice(whitePoint[maxWhite])

    return x, y
