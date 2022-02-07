"""
通过改造__new__ 方式实现单例
"""


class MusicPlayer:
    # 记录第一次创建的类的地址
    instance = None
    # 是否被初始化过
    init_flag = False

    def __init__(self):
        if MusicPlayer.init_flag is False:
            print("播放音乐...")
            # 标记为以初始化
            MusicPlayer.init_flag = True

    def __new__(cls, *args, **kwargs):
        print("分批内存地址")
        # 判断是否已存在
        if cls.instance is None:
            # 1. 为对象分配地址
            cls.instance = super().__new__(cls)
        # 2. 返回对象的地址
        return cls.instance


player = MusicPlayer()
print(player)

player2 = MusicPlayer()
print(player2)
