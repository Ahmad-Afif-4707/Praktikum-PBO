# class Hero:
#     def __init__(self, name, health):
#         # hanya pertarungan
#         self.name = name
#         self.health = health
        
#     def serang(self, target):
#         target.health -= 10

# class TampilanHero:
#     def tampilkan(self, hero):
#         # hanya tampilan
#         print(f"{hero.name} | HP {hero.health}")

# class PenyimpanHero:
#     def simpan(self, hero, nama_file):
#         # hanya penyimpanan
#         with open(nama_file, "a") as f:
#             f.write(f"{hero.name}, {hero.health}\n")

# layla = Hero("Layla", 70)
# Hero("Balmond", 120).serang(layla)
# TampilanHero().tampilkan(layla)
# PenyimpanHero().simpan(layla, "data_hero.txt")

# class Hero:
#     def __init__(self, attack):
#         self.attack = attack
        
#     def hitung_damage(self):
#         return self.attack

# class Fighter(Hero):
#     def hitung_damage(self):
#         return self.attack + 5

# class Mage(Hero):
#     def hitung_damage(self):
#         return self.attack * 2

# class Assassin(Hero):
#     def hitung_damage(self):
#         return self.attack * 3

# print(Fighter(10).hitung_damage())
# print(Mage(10).hitung_damage())
# print(Assassin(10).hitung_damage())

class Unit:
    pass  # hanya yang dimiliki semua unit

class UnitBergerak(Unit):
    def bergerak(self):
        print("Unit bergerak")

class Minion(UnitBergerak):
    pass

class Turret(Unit):
    def tembak(self):
        # tidak berjanji bisa bergerak
        print("Turret menembak")

def maju(unit: UnitBergerak):
    unit.bergerak()

maju(Minion())
Turret().tembak()