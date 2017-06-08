__author__ = 'shahab'

class State:
    def __init__(self,name,cities):
        self.name = name
        self.citis = cities
lorestan = State("lorestan","noorabad,dorood,alashtar,broojerd")

print(lorestan.citis)

khoozestan = State("khoozestan","shooshtar,ahvaz,dezfull")
print(khoozestan.citis)

iran = [lorestan,khoozestan]
print(iran)

for s in iran:
    print(s.name)
    print(s.citis)