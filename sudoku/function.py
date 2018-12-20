"""
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/12/18
@Program      : 游戏功能的函数
"""
from sudoku.SetVar import SetVar

setting = SetVar()

def selected_array(row, col):
    selectedArray = [[0 for i in range(9)] for j in range(9)]
    selectedArray[col][row] = 1
    setting.set_selected_array(selectedArray)
