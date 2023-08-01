import datetime
from random import shuffle

class python():
    def __init__(self):
        self.add()
        self.tuple()
        self.strslice()
        self.listslice()
        self.pattern()
        self.isdigit()
        self.upper()
        self.pasitive()
        self.merge()
        self.file()
        self.dictionary()
        self.duplicate()
        self.elseif()
        self.currentdate()
        self.time()
        self.today()
        self.read()
        self.list()
        self.length()
        self.sum()
        self.reverse()
        self.listmethod()
        self.shuffle()
        self.maximum()
        self.enumerate()
        self.remove()
        self.tuple()
        self.enumerate02
        self.method()
        self.set()
        self.differen()
        self.logic()
        self.calculate()

    def add(self):    
        ## 1. list into a string using list comprehensition
        list1=['hii','welcome','20','hello']
        list2=['I','and','fine']
        list3=list1+list2
        print(list3)

    def tuple(self): 
        ## 2. how to convert a list in to tuple 
        list=[1,2,3,4,5,6]
        list2=(tuple(list))
        print(list2)

    def strslice(self):
        ## 4.string Slice a="hello how are you"? ans w a
        a="hello how are you"
        b=list(a)
        new=slice(8,11)
        vo=b[new]
        vi="".join(vo)
        print(vi)

    def listslice (self): 
        ## 5.list slice a=[1,2,3,4,5,6,7,8] ans: [5,6]
        lists=[1,2,3,4,5,6,7,8]
        listsl=slice(4,6)
        voda=lists[listsl]
        print(voda)

    def pattern(self):
        ## 6.pattern program
        for i in range(1,5):
            for j in range(1,i+1):
                print(i,end=" ")  
            print()    
        

    def isdigit(self):
        ## 7. python program to check digit or not?
        e1="15,a"
        e2=e1.isdigit()
        print(e2)

    def upper(self):
        ## 8. python program to check lowercase or upper case?
        ei=(input("enter=" ))
        if ei.lower() and ei.upper() and ei!=ei.isdigit() and ei!=ei.capitalize():
            print("correct")
        else:
            print("wrong") 


    def pasitive(self):
        ##  9. Python program to find Positive or Negative number negative number?
        p1=int(input("numbers="))
        if p1>0:
            print("pasitive numbers")
        else:
            print("negative numbers") 
        
    def merge (self): 
        #11. Python Program to Merge Two Dictionaries 2 ways?
        m1={"jerry":5,"jack":2}
        m2={"block":5,"queen":2}
        m1.update(m2)
        print(m1)

    def file(self):
        ## 12. file write & read concept? 
        a5=(input("enter the name="))
        a6=(input("password"))
        if "jerry" in a5 and "567" in a6:
            open("read.html","w").write("login success ful")

        else:
            open("read.html","w").write("log in failed")

            v=open("read.html","r").read() 
            print(v) 
    

    def dictionary(self):
        ##14. Python Program to Convert Two Lists Into a Dictionary?
        a7=[2,3,4,5,6,7]
        a8=[46,76,8]
        a9=a7+a8
        a10=set(a9)
        print(a10)

    def duplicate(self):
        ## 15. Python Program to Remove Duplicate Element From a List?
        b7=[1,2,3,4,5,6]
        b8=[1,2,4,5,7,9,11,13,54]
        b9=b7+b8
        ben=set(b9)
        ben1=tuple(ben)
        print(ben1) 

    def elseif(self):
        ##16. Some of the examples of simple if else and elif?
        el=int(input("enter the values="))
        if el<10:
            print("0<10")
        elif el==10>100:
            print("10>100 ")
        else:
            print("others") 


                                                        ##datetime program

    def currentdate(self):
        #1. Python program to get current date
        current=datetime.datetime.today() 
        c=current.strftime("%D")
        print(c)
        

    def time(self):
       ## 2. Python program to get current time 
        time=datetime.datetime.today() 

        ti=time.strftime("%T")
        print(ti)  

    def today(self):
       ## 3. Python program to print today's year, month and day  
        today=datetime.datetime.today()
        print(today)
        

    def read(self):
        ##4. python datetime and using strftime also and write file?     
        read=datetime.datetime.today()
        w=read.strftime("%d,%m,%y")
        open("read.html","w").write(str(w))

    def list(self):
        ##  1: Program to Find List Difference:
        list1 = [1, 2, 4, 6, 8, 9]
        list2 = [1, 3, 5, 7, 11, 9]
        a=(list(set(list1)-(set(list2)))) 
        b=(list(set(list2)-(set(list1))))
        c=a+b
        print(c) 

    def length(self):
       ## 2: Python List length check?    
        length=[1,2,3,4,5,6,7]
        print(len(length))

    def sum(self):
        ##3: Python Program to find Sum of Elements in a List? 
        s=[3,6,5,8,9]
        u=sum(s)
        print(u) 

    def reverse (self):
        ##4. Python Program to Print List Items in Reverse Order?      
        re=[1,2,3,4,5,6,7,8,9,0]
        ve=((re)[::-1])
        print(ve)
        

    def listmethod(self):
       ## 5. list method using all and example programs? 
        a=[1,2,3,4,5,6]
        a.append(7)        ##append method
        print(a)

        b=a.copy()
        print(b)           ##copy method

        c=b.count(5)
        print(c)          ##count method


        d=[2,4,6,8,9]
        e=[1,3,5]
        d.extend(e)
        print(d)          ##extend method


        f=((d)[::-1])
        print(f)          ##reverse method


        f.remove(1)
        print(f)          ##remove method

        h=f.index(6)
        print(h)         ##index method

        
        i=["apple","orange","mango"]
        i.insert(1,"banana")          ##insert method
        print(i)

        i.sort()
        print(i)                     ##sort method


        i.pop(2)
        print(i)                     ##pop method


        i.clear()
        print(i)                    ##clear method

    
    def shuffle(self):
       ## 7. using Shuffle and print a specified list? random?  
        a=["red","orange","yellow","white","black","green"]  
        shuffle(a)
        print(a)

    def maximum(self):
       ## 8. Write a Python program to get the smallest number and longest from a list? 
        a=[1,2,3,4,5,6,7,8,9]
        print(min(a))
        print(max(a))


    def enumerate(self):
        a=[1,2,3,4,5,6,7,8]
        for i,j in enumerate(a):
            print(i,j)    

    def remove(self):
        ##1. Python Program to Remove an Item from Tuple?
        a=(1,2,3,4,5,6,8,9)
        b=[]
        for c in a:
            b.append(c)
        b.remove(4)
        c=tuple(b)
        print(c)

    def tuple(self):
        ##2. Python Program to Reverse Tuple?
        a=(11,12,13,21,22,23,24)
        b=[]
        for i in a:
            b.append(i)
        c=(b[::-1])
        print(c)


    def enumerate02(self):
       ### 9. list using enumerate in python?
        a=[1,2,3,4,5,6,7,8]
        for i,j in enumerate(a):
            print(i,j)     

    def method(self):
        a={1,2,3,4,5,6,7,8,9}
        a.clear()              ### 1. clear
        print(a)

        a={1,3}
        a.copy()              ### 2.copy
        print(a)

        b={"key","kock","heart","jerry"}
        c=3
        d=dict.fromkeys(b,c)        ### 3.fromkeys
        print(d)

        a={"jerry":1 ,"jack":2,"heat":3}
        b=a.get("jack")              ### 4.get method
        print(b)

        a={"jerry":1 ,"jack":2,"heat":3}                       
        b=a.items()                   ### 5.items
        print(b)
                              ###set
    def set(self):
        a={"a","b","c","d","e","f"}
        a.add("g")                 ## add method
        print(a) 

        a.copy()
        print(a)                  ## copy method 

        h={1,2,3,4,5,6,7}
        h.pop()
        print(a)                 ##pop method

        a.remove("f")
        print(a)                 ##remove method

        a.discard("a")
        print(a)                 ##discard method

        b={"hii","hello","jery","jack"}
        b.update(a)                   ##update method
        print(b)
  
        c={"hii","mango","django"}
        f= b.intersection(c)
        print(f)                    ##intersection method

        g=c.difference(b)
        print(g)                    ##difference method
        

        u=g.union("start")
        print(u)                  ## union method

        u.clear()
        print(u)
                          ## clear method

    def differen(self):  
    ##13. Python Program to Concatenate Two Lists? use 2 differend ways. 
        a=[1,2,3,4,5,6]
        b=[2,4,7,0,34]
        c=a+b
        print(c)
        a.extend(b)
        print(a)

    def logic(self):
        ## 17. python if else program using (and,or,in,==,!=,>,<) using all single program?    
        a=(input("enter the name="))
        b=int(input("values="))
        if ("jerry" in a or a==a.lower()) and a!=a.upper() and a!=a.isdigit()  and b>10 and b<100 :
            print("sucess")

        else:
            print("failed")
      

    def calculate (self):
        a=35
        b=4
        c=a+b
        print("addiction=",c)
        c=a-b 
        print("substration=",c)
        c=a*b
        print("multiplucation=",c)
        c=a/b
        print("divided=",c)          



        
if __name__=='__main__':
    python()        