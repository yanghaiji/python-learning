"""
__new__ 内存是指分配
"""


class MusicPlayer:

    def __init__(self):
        print("播放音乐...")

    def __new__(cls, *args, **kwargs):
        print("分批内存地址")
        # 1. 为对象分配地址
        instance = super().__new__(cls)
        # 2. 返回对象的地址
        return instance


player = MusicPlayer()
print(player)

