"""
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/9/10
@Program      : 全局变量的保存
"""
import random


class SettingVar:
    def __init__(self):
        # 颜色词典
        self.COLOR_DICT = {'white': (255, 255, 255),  # 白色
                           'ivory': (255, 255, 240),  # 象牙色
                           'yellow': (255, 255, 0),  # 黄色
                           'seashell': (255, 245, 238),  # 海贝色
                           'bisque': (255, 228, 196),  # 橘黄色
                           'gold': (255, 215, 0),  # 金色
                           'pink': (255, 192, 203),  # 粉红色
                           'lightpink': (255, 182, 193),  # 亮粉红色
                           'orange': (255, 165, 0),  # 橙色
                           'coral': (255, 127, 80),  # 珊瑚色
                           'tomato': (255, 99, 71),  # 番茄色
                           'magenta': (255, 0, 255),  # 洋红色
                           'wheat': (245, 222, 179),  # 小麦色
                           'violet': (238, 130, 238),  # 紫罗兰色
                           'silver': (192, 192, 192),  # 银白色
                           'brown': (165, 42, 42),  # 棕色
                           'gray': (128, 128, 128),  # 灰色
                           'olive': (128, 128, 0),  # 橄榄色
                           'purple': (128, 0, 128),  # 紫色
                           'turquoise': (64, 224, 208),  # 绿宝石色
                           'seagreen': (46, 139, 87),  # 海洋绿色
                           'cyan': (0, 255, 255),  # 青色
                           'green': (0, 128, 0),  # 纯绿色
                           'blue': (0, 0, 255),  # 纯蓝色
                           'darkblue': (0, 0, 139),  # 深蓝色
                           'navy': (0, 0, 128),  # 海军蓝色
                           'black': (0, 0, 0),  # 纯黑色
                           }

        # 元素的数字颜色
        self.NUM_COLOR_DICT = {'2': self.COLOR_DICT['gray'], '4': self.COLOR_DICT['brown'],
                               '8': self.COLOR_DICT['violet'], '16': self.COLOR_DICT['wheat'],
                               '32': self.COLOR_DICT['coral'], '64': self.COLOR_DICT['turquoise'],
                               '128': self.COLOR_DICT['navy'], '256': self.COLOR_DICT['olive'],
                               '512': self.COLOR_DICT['orange'], '1024': self.COLOR_DICT['seagreen'],
                               '2048': self.COLOR_DICT['purple']}

        self.TILE_SIZE = 80
        self.WINDOW_BLOCK_NUM = 4

    def init_game(self):
        """初始化游戏的数组，于开始新游戏或者重置游戏时调用"""
        gameArray = [[0 for i in range(self.WINDOW_BLOCK_NUM)] for j in
                     range(self.WINDOW_BLOCK_NUM)]  # 初始化的游戏数组
        # 初始化两个开始元素在任意位置。
        random_elem = 0
        while random_elem < 2:
            self.add_elem(gameArray)
            random_elem += 1

        return gameArray

    def add_elem(self, gameArray):
        """添加元素功能"""
        while self.can_add_elem(gameArray):
            # 生产随机位置元素，完成即跳出运行
            x = random.randint(0, self.WINDOW_BLOCK_NUM - 1)
            y = random.randint(0, self.WINDOW_BLOCK_NUM - 1)
            if gameArray[x][y] == 0:
                gameArray[x][y] = 2
                break

    def can_add_elem(self, gameArray):
        """初始化元素为零的元素数量为16个。每查找到一个非零的元素，计数减1. 如果没有是零的元素，不必添加新元素"""
        num_zero = 16
        # 添加一个判断，如果数组全部非0，不添加元素
        for i in range(self.WINDOW_BLOCK_NUM):
            for j in range(self.WINDOW_BLOCK_NUM):
                if gameArray[i][j] != 0:
                    num_zero -= 1
        if num_zero == 0:
            return False
        return True

