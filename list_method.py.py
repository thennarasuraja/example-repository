              #list methodes
class find():
     def __init__(self):
          fruits=["apple","orange","grapes","orange","orange"]
          print(fruits)
          print("*"*20+'list compited'+"*"*20)
          self.Append(fruits)


     def Append(self,fruits):
                         ###  append method
         fruits.append("watermelon")
         print(fruits)
         print("*"*20+'append complete'+"*"*20)
         self.copy(fruits)

     def copy(self,fruits):
                         ### copy method
         Copy=fruits.copy() 
         print(Copy)
         print("*"*20+'copy complited'+"*"*20)
         self.count(fruits) 

     def count(self,fruits):
                         ### count method
         Count=fruits.count("orange")
         print(Count)
         print("*"*20+'count complited'+"*"*20)  
         self.extend(fruits)

     def  extend(self,fruits):
                           ### extend method
         car=['volvo','bmw','skoda']
         Extend=fruits.extend(car)
         print(fruits)
         print("*"*20+"extend completed"+"*"*20)
         self.index(fruits)

     def  index(self,fruits):
                            ### index method
         Index=fruits.index('watermelon')
         print(Index)
         print("*"*20+'Index completed'+"*"*20) 
         self.insert(fruits)

     def insert(self,fruits):
                             ### insert method
        fruits.insert(2,'pomegranate')
        print(fruits)
        print("*"*20+'Insert completed'+"*"*20)
        self.pop(fruits)

     def pop(self,fruits):
                          ### pop method
         fruits.pop(1)
         print(fruits)
         print("*"*20+'pop copmleted'+"*"*20)
         self.remove(fruits)

     def remove(self,fruits):
                         ### remove method
         Remove=fruits.remove("apple")
         print(fruits)
         print("*"*20+'remove completed'+"*"*20)
         self. reverse(fruits)

     def reverse(self,fruits):
                       ### reverse method
         fruits.reverse()
         print(fruits)
         print("*"*20+'reverse complited'+"*"*20)
         self.sort(fruits)
     
     def sort(self,fruits):
                         ### sort method
          fruits.sort()
          print(fruits)
          print("*"*20+'sort completed'+"*"*20)

              
      

        







if __name__=="__main__":
     find()              





    