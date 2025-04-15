from __future__ import annotations

class Animal:
    def __init__(self,legs=0):
        self.legs = legs
    def walk(self)-> None:
        print(f'This animal walks with {self.legs} legs.')
    def sleep(self)-> None:
        print(f'Different animals have different sleep habits')
    def __repr__(self):
        return f'Animal: no idea \nLegs: {self.legs}'

if __name__ == '__main__':
    anim = Animal(6)
    print(anim)

    print()
    anim.walk()
    anim.sleep()

