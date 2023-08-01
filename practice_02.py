from itertools import product
class jack():
    def __init__(self):
        # self.program01()
        # self.program02()
        # self.program03()
        #self.program04()
        self.program05()
        # self.program06()
        # self.program07()
        # self.program08()
        # self.program09()
        # self.program10()

    def program01(self):
        for q in range(1,5):
            print(q)
        for i in range(1,10):     #"  " to additction values
            print(i+100) 
        for j in range(1,10,2):     #for use to jumb values
            print(j)  
        for k in range(10,1-1,-1):    #for use to reverse values 
            print(k)   
        for l in range(1,11):
            print(l,"X",10,"=",l*10)     #*Table
        a="sample"
        b=0
        for i in a:
            print(b,"=",i)     #positon check
            b+=1 
    def program02(self):
        a=1
        while a<=10:         #while loop
            print(a)
            a+=1

        b=input("values").upper()
        while  b=="B":
            print("Bathma priya")
            break

    def program03(self):  
        result=0
        number=1
        while result<=5:
            result +=number
            print(result)

    def program04(self):
                            ### find a leap years
        year=int(input("enter the year: "))
        if year%400==0:
            print(f"{year} is leap year")
        elif year%100==0:
            print(f"{year} is not leap year")
        elif year%4==0:
            print(f"{year} is leap year")
        else:
            print(f"{year} is not leap year")                        

    def program05(self):
                           ### fibanocci concept
        first,second=0,1
        n = int(input("enter the numbers"))
        for i in range(1,n):
            if i<=1:
                result=i
                print("if", result)
            else:
                result = first+second
                # print("result-->", result)
                first = second
                # print("first ",first)
                second = result
                # print("second ",second)
            print("result- last",result)    
                                    
    def program06(self):
                        ### armstrong number
        number=input("enter the value: ")
        armstrong=0
        for i in number:
            armstrong+=(int(i))**3
            # print(armstrong)
        if armstrong==int(number):
            print("this is armstrong number")
        else:
            print("this is not armstrong number") 

    def program07(self):
                          ###  iter toools 
       d={"1":["a","b"],"2":["c","d"]}
       for x,y in product (*d.values()):
           print(x+y)

    def program08(self):
                      ### zip   
        a=("hererert")
        b=(1,2,3,4,5,6,7,8,9)
        print(list(zip(a,b)))

    def program09(self):
                         ### lambda
        a=(1,2,3,4)
        b=(5,6,7,8)
        c=map(lambda x,y:x+y,a,b)
        print(list(c))


    def program10(self):
                        ###   replace
        a="restart"
        b=a[0]
        print(b)
        c=a.replace(b,"$")
        d=c+b[1:]
        print(d)
      
            
      






     





if __name__=="__main__":
    jack()