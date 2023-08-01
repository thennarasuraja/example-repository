import datetime
import random
class jerry():
    def __init__(self):
        self.program01()
        # self.program02()
        # self.program03()
        # self.program04()
        # self.program05()
        # self.program06()
        # self.program07() 
        # self.program08()
        # self.program09()
        # self.program10()
        # self.program11()
        # self.program12()
        # self.program13()
        # self.program14()
        # self.program15()
        # self.program16()
        # self.program17()
        # self.program18()
        # self.program19()
        # self.program20()
    def program01(self):
        # for j in range(1,100+1):
        #     print(j)
        a=(5,6)
        b=[]
        for i in a:
            # print(i)
            b.append(i)
            print(b)    



    def program02(self):
        variable=int(input("values="))
        new_one=[]
        for i in range(1,variable):
            new_one.append(i)
        print(new_one)   

    def program03(self):    
        a=(5,6,7,8)
        b=[]
        for i in a :
            b.append(i)
        print(b)    

    def program04(self):
        variable=("jerry","jack","chottu")
        for i in variable:
            print(i)

    def program05(self):
        user_name=(input("user name="))
        password=(input("password=")) 
        if "jerry" in user_name and "3210" in password:
            print("Log in success full") 
        else:
            print("Log in failed")

    def program06(self):
        a=datetime.datetime.today()
        b=a.strftime("%d,%m,%y")
        open("kiru.html","w").write(b)
        c=open("kiru.html","r").read()
        print(c)

    def program07(self):
        a=random.randint(1,10)
        print(a)

    def program08(self):
        #string slice a="hello how are you?
        a="hello how are you"
        b=slice(8,11)
        c=a[b]
        print(c)

    def program09(self):
        #list slice a=[1,2,3,4,5,6,7,8,9] ams:[5,6]
        a=[1,2,3,4,5,6,7,8]
        b=slice(4,6) 
        c=a[b]
        print(c)   

    def program10(self):
        #pattern programing ans like:
        for i in range(1,5):
            for j in range(1,i+1):
                print(i,end="") 
            print()  

    def program11(self):
        a=input("values=") 
        if a.isdigit():
            print("digit values")
        else:
            print("Not digit values")

    def program12(self):
        a=(input("names="))
        if a.lower() and a!=a.capitalize() and a!=a.isdigit() and a!=a.upper():
            print("the variable is lower values") 
        elif a.upper():
            print("variable is upper values")    

    def program13(self):
        a={"a":1} 
        b={"b":2}
        a.update(b)
        print(a) 
        # c={**a,**b}
        # print(c)

    def program14(self):
        #Python Program to Convert Two Lists Into a Dictionary?
        a=["jerry","jack","chottu"]
        b=[]
        b=[3,2,1]
        c=dict(zip(b,a))
        print(c)
        # for i in enumerate(a):
        #     b.append(i)
        # print(b) 
        # c=dict(zip((b[0],b[1]),(b[0],b[1])))
        # print(c)   
             

    def program15(self):
        a=[1,2,3,4,5,6,7,8,9]
        print(a[4])
        print(a[4:])
        print(a[-5])
        print(a[:-2])
        print(a[:3])
        print(a[::2]) #jump indexes
        print(a[::-3])
        print(a[1:6:2])#another jump concept
        print(a[8:1:-2])#revese jump concept
        a[1]=100
        print(a)
        # c=(10,20,30,40,50)  #tuple ah oru vatti value assign panita value ah change pana mudiyadhu
        # c[0]=13
        # print(c)

    def program16(self): 
        a={1:"jerry",2:"pradeep",3:"values"}
        b=a.keys()
        print(list(b))  
        c=a.values()
        print(list(c))   

    def program17(self):
        a=(1,2,3,4,5,6)
        b=[12,13,14,15,16]
        c={1:"jerry",2:"pradeep",3:"values"}   
        d=3 in a
        print(d)  
        e=4 in b
        print(e) 
        f=2 in c
        print(f)
        g="pradeep" in c.values()
        print(g)

    def program18(self):
        a=[1,2,3,[10,20,30]]
        b=a[-1]
        print(b)
        a[-1].append(40)
        print(a)
        print(a[-1][0])
        a.append("jerry")
        print(a)
        c=a[-1][3::]
        print(c)
        a[-2].append("pradeep")
        print(a)
        a=a[-2][-1][::-1]
        print(a)

    def program19(self):
        a={1:("sun","monday"),2:("tue","wed"),3:("thurs","fri")}
        b=a[1][1]
        print(b)
        c=a.keys()
        print(list(c)) 
        d=a.values()
        print(list(d)) 
    def program20(self):     
        ##  1: Program to Find List Difference:
        list1 = [1, 2, 4, 6, 8, 9]
        list2 = [1, 3, 5, 7, 11, 9]
        a=list(set(list1)-(set(list2))) 
        b=list(set(list2)-(set(list1)))
        c=a+b
        print(c)
        
if __name__=="__main__":
    jerry()            