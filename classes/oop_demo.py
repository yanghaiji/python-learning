"""
设计一个游戏类
1.记录游戏的历史最高分
2.记录当前玩家的姓名
3.查看如何玩游戏

---
分析
1.记录游戏的历史最高分
    属于类信息，可定义为类属性，通过类方法进行获取
2.记录当前玩家的姓名
    属于实例方法，在创建对象时产生，实例方法
3.查看如何玩游戏
    与类和实例都无关系，定义为静态方法

"""


class Game(object):
    max_score = 0

    def __init__(self, name):
        self.name = name

    def game_start(self):
        print("%s 开始游戏了..." % self.name)

    @classmethod
    def show_max(cls):
        print("目前历史最高分数为 %s " % cls.max_score)

    @staticmethod
    def game_help():
        print(("游戏说明: \n"
               "1.点击开始 \n"
               "2.一直向前跑 \n"))


# 测试
# 查看游戏帮助信息
Game.game_help()
# 查看历史最高分
Game.show_max()
game = Game("小明")
game.game_start()
