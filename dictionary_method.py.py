class jack():
         ###     Dictionary  list()
    def __init__(self):

                         ### add method()
        fruit={"a","b","c"}
        fruit.add("d")
        print(fruit)
        self.copy(fruit)


    def copy(self,fruit):
                        ### copy method()
        fruit.copy()
        print(fruit)
        self.pop(fruit)

    def pop(self,fruit):
                         ###  pop method()
        # fruit.pop()
        # print(fruit)
        self.remove(fruit)

    def remove(self,fruit):
                        ###   remove method()

        fruit.remove("b")
        print(fruit)
        self.discard(fruit)

    def discard(self,fruit):
                          ###  discard method()
        fruit.discard("a")
        print(fruit)
        self.update(fruit)

    def update(self,fruit):
                          ###  update method()
        fruit.update("a","b","c","d")
        print(fruit)
        self.intersection()

    def intersection(self):
                         ###  intersection method
        a={"apple","banana","newyork"}
        b={"microsoftware","newyork"}
        c=b.intersection(a)
        print(c)
        self.difference()


    def difference(self):
                        ### difference method
        ab={"normal","medium","high","5"}
        cd={"normal","low","high"}
        ed=ab.difference(cd)
        print(ed)


    








    






if __name__=='__main__':
    jack()        