class Good:
    def __init__(self):
        self.name = ""
        self.desc = ""
        self.type = ""
        self.attack = 0
        self.price = 0
        self.function = 0
        self.is_special = False

    def __str__(self):
        return f'物品名称：{self.name},类型：{self.type},特殊标记：{self.is_special}'


class Water(Good):
    def __init__(self):
        super().__init__()
        self.name = "水"
        self.desc = "使用后去除1个口渴标记"
        self.type = "消耗品"


class Medical(Good):
    def __init__(self):
        super().__init__()
        self.name = "医药箱"
        self.desc = "使用恢复1点体力"
        self.type = "消耗品"


class Treasure(Good):
    def __init__(self):
        super().__init__()
        self.name = "珠宝"
        self.desc = "1个珠宝1分，2个珠宝4分，3个珠宝8分"
        self.type = "收藏品"
        self.price = 1


class Money(Good):
    def __init__(self):
        super().__init__()
        self.name = "钞票"
        self.desc = "1个钞票1分，2个钞票4分，3个钞票8分"
        self.type = "收藏品"
        self.price = 1


class Paddle(Good):
    def __init__(self):
        super().__init__()
        self.name = "船桨"
        self.desc = "体力+1"
        self.type = "消耗品"
        self.attack = 1
