class ABC:
    cat = 'Persion'

    def __init__(self):
        print('ABC contructor')
    
    def testing(sefl, param1, param2):
        print(param1 + param2)

    def showCat(self):
        print(self.cat)

xyz = ABC()
efg = ABC()

# Attribute shadowing is when an instance variable overrides a class variable with the same name, so the instance uses 
# its own value instead of the shared class value. It lets you override a shared default (class attribute) for specific 
# objects, so each instance can have its own customized value without affecting others or the class itself.
xyz.cat = 'Siamese'
efg.cat = 'Rag Doll'

print(ABC.cat)
print(xyz.cat)
print(efg.cat)

xyz.testing(20, 30)