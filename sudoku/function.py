"""
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/12/18
@Program      : 游戏功能的函数
"""


def selected_array(col, row):
    selectedArray = [[0 for i in range(9)] for j in range(9)]
    selectedArray[col][row] = 1
    return selectedArray
