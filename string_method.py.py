                  ###     string methodes
class string():
    def __init__(self):
                        ### capitalize method
        g=("jerry jack")
        print(g.capitalize())
        self.ned()
        

    def ned(self):
                       ### upper method
        h=("string")
        print(h.upper())
        self.new()

    def new(self):    
                       ### lower method
        a=("METHOD")
        print(a.lower())
        self.sir()

    def sir(self):
                       ### casefold method
        w="karThi"    
        print(w.casefold())
        self.m()

    def m(self):
                     ### isdigit method
        e="1234"
        print(e.isdigit())
        self.mom()  

    def mom(self):
                     ### isalpha method
        r=("1234")
        print(r.isalpha() )
        self.park()

    def park(self):
                     ### split method
        t=("hard work")
        f=t.split()
        print(f)
        self.jk()

    def jk(self):
                       ### left strip method
         s=("        hii")   
         print(s.lstrip())
         self.kong()

    def kong(self):
                       ### right strip method
        j=("  oiihii ")
        print(j.rstrip())
        self.king()


    def king(self):
                      ### strip method
        k=("                 new")
        print(k.strip())
        self.jack()

    def jack(self):
                     ### title method
        m=("fd gtr wer ") 
        print(m.title())


if __name__=="__main__":
    string()