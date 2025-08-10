from gift import GiftAble
from typing import override


class BasketBall(GiftAble):
    @override
    def give_gift(self):
        return "You get to ride with your friends :)"