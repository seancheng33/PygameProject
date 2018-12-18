"""
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/12/18
@Program      : 游戏功能的函数
"""

# 判断格子是否是选择状态
pressedX = -1
pressedY = -1


def tile_is_selected(col, row, pressedX, pressedY):

    if col == pressedX and row == pressedY:
        return True

    return False