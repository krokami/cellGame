# -*- coding: utf-8 -*-

import profile
from game import Game


def profile_main():
    """main函数性能测试.

    @return: None
    """
    game = Game(1300, 800)
    game.start(1)


if __name__ == "__main__":
    profile.run("profile_main()")
