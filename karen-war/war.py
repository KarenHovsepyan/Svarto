class Weapon:
    def __init__(self, name, bullet, damage):
        self.name = name
        self.bullet = bullet
        self.damage = damage


class Warrior:
    def __init__(self, name, nationality, weapon, live):
        self.name = name
        self.nationality = nationality
        self.weapon = weapon
        self.live = live

    def shot(self, warrior):
        warrior.live -= 1
        self.weapon.bullet -= 1


class War:
    def shoting(target, shooter):
        quentity = 0
        for i in range(500):
            target.shot(shooter)
            quentity += 1
            if shooter.live == 0:
                print("Death")
                break
            elif target.weapon.bullet == 0:
                print("recharge")
                target.weapon.bullet = quentity
                quentity = 0


akaem = Weapon("Akaem", 30, 19)
sniper = Weapon("Sniper", 4, 80)
winchester = Weapon("Winchester", 8, 52)
machine_gun = Weapon("Machine Gun", 50, 23)
ronin = Warrior("Ronin", "USA", akaem, 400)
fantom = Warrior("Fantom", "Franch", sniper, 300)
saint = Warrior("Saint", "England", winchester, 500)
trench = Warrior("Trench", "Canada", machine_gun, 500)
War.shoting(ronin, fantom)

