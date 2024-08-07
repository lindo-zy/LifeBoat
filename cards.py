import random


class Card:
    def __init__(self, name, type, value=None):
        self.name = name  # 卡牌名称
        self.type = type  # 卡牌类型
        self.value = value  # 卡牌的值，某些卡牌可能没有值

    def __str__(self):
        return f"{self.name} ({self.type})"


# 定义补给卡
provision_cards = [
    ("水", "补给", None) * 16,
    ("现金包", "现金", 1) * 6,
    ("珠宝", "珠宝", None) * 3,
    ("画作", "画作", 3) * 2,
    ("画作", "画作", 2),
    ("医疗包", "医疗包", None) * 3,
    ("武器", "武器", "桨") * 2,
    ("武器", "武器", "黑杰克") * 1,
    ("武器", "武器", "匕首") * 1,
    ("武器", "武器", "鱼叉") * 1,
    ("武器", "武器", "信号枪") * 1,
    ("鱼饵桶", "鱼饵桶", None) * 2,
    ("救生圈", "救生圈", None) * 1,
    ("指南针", "指南针", None) * 1,
    ("遮阳伞", "遮阳伞", None) * 1,
]

# 定义航行卡
navigation_cards = [("航行", "航行")] * 24

# 定义角色卡
character_cards = [
    ("劳伦女士", "角色"),
    ("斯蒂芬爵士", "角色"),
    ("船长", "角色"),
    ("大副", "角色"),
    ("弗兰奇", "角色"),
    ("小鬼", "角色")
]

# 定义位置卡
placeholder_cards = [
    ("占位符", "占位符") for _ in range(6)
]

# 定义憎恨卡
hate_cards = character_cards.copy()

# 定义爱恋卡
love_cards = character_cards.copy()


# 创建卡牌实例
def create_cards(card_data):
    cards = []
    for card_info in card_data:
        if isinstance(card_info[0], tuple):  # 处理重复卡牌的情况
            for _ in range(len(card_info)):
                cards.append(Card(*card_info[0]))
        else:
            cards.append(Card(*card_info[0]))
    return cards


# 创建所有卡牌
provision_deck = create_cards(provision_cards)
navigation_deck = create_cards(navigation_cards)
character_deck = create_cards(character_cards)
placeholder_deck = create_cards(placeholder_cards)
hate_deck = create_cards(hate_cards)
love_deck = create_cards(love_cards)

# 打乱卡牌
random.shuffle(provision_deck)
random.shuffle(navigation_deck)
random.shuffle(character_deck)
random.shuffle(placeholder_deck)
random.shuffle(hate_deck)
random.shuffle(love_deck)

# 输出卡牌信息
for card in provision_deck:
    print(card)
