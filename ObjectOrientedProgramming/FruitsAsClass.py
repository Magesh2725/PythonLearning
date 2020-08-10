class fruits():
    #classobject
    fruitvariety='Berries'
    cost=20
    def __init__(self, name, seedless):
            self.name=name
            self.seedless = seedless
    def getPrice(self,kgs):
        self.kgs=kgs
        return f'the cost of {self.name}  is {fruits.cost*self.kgs}'
fruitobject=fruits('Grapes',False)

print(fruitobject.name)
print(fruitobject.seedless)
print(fruitobject.fruitvariety)
print(fruitobject.getPrice(5))


