import itertools 

# name="jerry"
# password=12345
# mail="jerry@gmail.com"
# result=iter{"name":name,"password":password,"mail":mail}
# print(next(result))

# a=(15,16,17)
# b=iter(a)
# print(next(b))

a="raja kumari"
b="raja"
for i in a:
    if i not in b:
        print(i)
    