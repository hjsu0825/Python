# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed) :
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage) :
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]")

    def damaged(self, damage):
        print(f'{self.name} : {damage} 대미지를 입었습니다.')
        self.hp -= damage
        print(f'{self.name} : 현재 체력은 {self.hp}입니다.')
        if self.hp <=0:
            print(f"{self.name} : 파괴되었습니다.")

# 드랍쉽
class Flyable:
    def __init__(self, name, flyingspeed):
        self.name = name
        self.flyingspeed = flyingspeed
    
    def fly(self, location):
        print(f"{self.name} : {location} 방향으로 날아갑니다. [속도 {self.flyingspeed}]")

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flyingspeed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드 0
        Flyable.__init__(self, name, flyingspeed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(location)

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        self.name = name
        self.hp = hp
        self.location = location

# 밥집