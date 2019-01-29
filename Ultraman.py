"""
奥特曼打小怪兽

"""

from abc import ABCMeta, abstractmethod
from random import randint, randrange


class Fighter(object, metaclass=ABCMeta):
    # 限定对象可以绑定的成员变量
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        """
        攻击
        :param other: 被攻击目标
        """
        pass


class Ultraman(Fighter):

    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)

    def ult(self, other):
        """
        大招(打掉对方至少50点或四分之三的血)
        :param other: 被攻击目标
        :return: 使用成功返回True 否则False
        """
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        """
        魔法攻击
        :param others: 被攻击的群体
        :return: 使用魔法成功返回True否则返回False
        """
        if self._mp >= 20:
            self._mp -= 20
            for target in others:
                if target.alive:
                    target.hp -= randint(10, 15)
            return True
        else:
            return False

    def restore(self):
        """恢复魔法值"""
        re_mana = randint(1, 10)
        self._mp += re_mana
        return re_mana

    def __str__(self):
        return '~~~%s奥特曼~~~\n' % self._name + \
               '生命值: %d\n' % self._hp + \
               '魔法值: %d\n' % self._mp


class Monster(Fighter):

    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + \
               '生命值: %d\n' % self._hp


def is_any_alive(monsters):
    """判断小怪兽是否还有活着的"""
    for monster in monsters:
        if monster.alive:
            return True
    return False


def select_alive_one(monsters):
    """选中一只活着的小怪兽"""
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive:
            return monster


def display_info(ultraman, monsters):
    """显示奥特曼和小怪兽的信息"""
    print(ultraman)
    for monster in monsters:
        print(monster, end='')


def main():
    u = Ultraman('迪迦', 1000, 120)
    m1 = Monster('贝蒙斯坦', 250)
    m2 = Monster('达达', 500)
    m3 = Monster('史莱姆', 750)
    ms = [m1,m2,m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('==========第%02d回合==========' % fight_round)
        m = select_alive_one(ms) # 选择一只小怪兽
        skill_choice = randint(1, 10) # 通过随机数来选择技能
        if skill_choice <= 6: # 60%概率选择普通攻击
            print('%s使用普通攻击打了%s' % (u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢复了%d点.' % (u.name, u.restore()))
        elif skill_choice <= 9: # 30%概率选择魔法攻击（也可能因为魔法不足而失败）
            if u.magic_attack(ms):
                print('%s使用了魔法AOE' % u.name)
            else:
                print('%s使用魔法攻击失败' % u.name)
                print('%s的魔法值恢复了%d点.' % (u.name, u.restore()))
        else:  # 10%的概率使用究极必杀技(如果魔法值不足则使用普通攻击)
            if u.ult(m):
                print('%s使用究极必杀技虐了%s.' % (u.name, m.name))
            else:
                print('%s使用普通攻击打了%s.' % (u.name, m.name))
                u.attack(m)
                print('%s的魔法值恢复了%d点' % (u.name, u.restore()))
        if m.alive > 0:  # 如果选中的小怪兽没有死就回击奥特曼
            print('%s回击了%s.' % (m.name, u.name))
            m.attack(u)
        display_info(u, ms)  # 每个回合结束后显示奥特曼和小怪兽的信息
        fight_round += 1
    print('\n========战斗结束!========\n')
    if u.alive > 0:
        print('%s奥特曼胜利!' % u.name)
    else:
        print('小怪兽胜利!')


if __name__ == '__main__':
    main()


