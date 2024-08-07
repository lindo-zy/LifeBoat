'''
Lady Lauren 劳伦夫人：生命分数4。生存分数8。能力：珠宝得分加倍。
Sir Stephen 斯蒂芬先生：生命分数5。生存分数7。能力：美术品得分加倍。
The Captain 船长：生命分数7。生存分数5。能力：现金得分加倍。
First Mate 大副：生命分数8。生存分数4。能力：就是个头大。
Frenchy 水手：生命分数6。生存分数6。能力：水性好，落水后避免一点伤害。
The Kid 小孩：生命分数3。生存分数9。能力：行动阶段抢劫某人手牌，对方不得拒绝。
doctor Jack 医生杰克:生命分数5。生存分数7。能力：使用【医疗箱】后可以不丢弃
lady Huang 黄女士:生命分数3。生存分数9。能力：任意角色使用【喝酒】或【水】,可以一起享受
'''


class People:
    def __init__(self):
        # 姓名
        self.name = ''
        # 描述
        self.description = ''
        self.score = 0
        # 生命
        self.life = 0
        # 位置
        self.position = 0
        # 物资
        self.substance_cards = []
        # 角色
        self.role_cards = []
        # 航海卡
        self.navigate_cards = []
        # 流血标记
        self.blood_cards = []
        # 打架标记
        self.fight = False
        # 船桨标记
        self.paddle = False
        # 落水标记
        self.fall = False

    def __str__(self):
        message = [
            f'角色:{self.name}',
            f'描述:{self.description}',
            f'当前生命:{self.life}',
            f'当前位置:{self.position}',
            f'口渴标记:{self.blood_cards}',
            f'打架标记:{self.fight}',
            f'划船标记:{self.paddle}',
            f'落水标记:{self.fall}',
        ]

        return '\r\n'.join(message)

    def cal_life(self):
        # 计算打架
        # 计算落水
        # 计算口渴
        # 计算道具
        if self.fight and self.life:
            self.life -= 1
        if self.paddle and self.life:
            self.life -= 1
        if self.blood_cards and self.life:
            self.life -= len(self.blood_cards)
        # 减去道具的体力
        if self.life < 0:
            return -1
        return self.life

    def cal_skill(self):
        pass


class LadyLauren(People):
    def __init__(self):
        super().__init__()
        self.name = '劳伦夫人'
        self.description = '生命分数4。生存分数8。能力：珠宝得分加倍'
        self.life = 4
        self.score = 8


class SirStephen(People):
    def __init__(self):
        super().__init__()
        self.name = '斯蒂芬先生'
        self.description = '生命分数5。生存分数7。能力：美术品得分加倍。'
        self.life = 5
        self.score = 7


class TheCaptain(People):
    def __init__(self):
        super().__init__()
        self.name = '船长'
        self.description = '生命分数7。生存分数5。能力：现金得分加倍。'
        self.life = 7
        self.score = 5


class FirstMate(People):
    def __init__(self):
        super().__init__()
        self.name = '船长'
        self.description = '生命分数8。生存分数4。能力：就是个头大。'
        self.life = 8
        self.score = 4


class Frenchy(People):
    def __init__(self):
        super().__init__()
        self.name = '水手'
        self.description = '生命分数6。生存分数6。能力：水性好，落水后避免一点伤害。'
        self.life = 6
        self.score = 6


class TheKid(People):
    def __init__(self):
        super().__init__()
        self.name = '小孩'
        self.description = '生命分数3。生存分数9。能力：行动阶段抢劫某人手牌，对方不得拒绝。 '
        self.life = 3
        self.score = 9


class DoctorJack(People):
    def __init__(self):
        super().__init__()
        self.name = '医生杰克'
        self.description = '生命分数5。生存分数7。能力：使用【医疗箱】后可以不丢弃'
        self.life = 5
        self.score = 7


class LadyHuang(People):
    def __init__(self):
        super().__init__()
        self.name = '黄女士'
        self.description = '生命分数3。生存分数9。能力：任意角色使用【喝酒】或【水】,可以一起享受'
        self.life = 3
        self.score = 9
