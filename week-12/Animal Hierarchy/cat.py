from animal import Animal

class Cat(Animal): #inherit everything from animal class
    def __init__(self):
        #super().__init__(4)
        Animal.__init__(4) #using constructor from animal
        self.type = 'cat'
    def sleep(self, hours = None) -> None: #when calling sleep cat this executes and not the one from the parent class

        if hours == None:
            print('Cats sleep in confortable places')
        else:
            print(f'Cats sleep {hours} hours.')
    def __repr__(self):
        return f'Animal: {self.type} \n Legs: {self.legs}'
if __name__ == '__main__':    
    cat = Cat()
    print(cat)

    print()
    cat.walk() #cat animal
    cat.sleep() #cat class
    cat.sleep(4) #cat class