
# array syntax--> array("type_code",[])

#import array
#import array as ar    (as means alias)
#from array import *

# import array
# a=array.array("i",[1,2,3,4,5])
# print(a)

import array as arr
a=arr.array("i",[-1,-2,3,4])
print(a)

from array import *
a=array("i",[1,2,3,4,5,6])
a.insert(0,15)
print(a)
a.pop(0)
print(a)

import array

a=array.array("i",[1,2,3,4,5,6])
for i in a:
    if i==2:
        print("multiple")
        continue
    print(i)    



