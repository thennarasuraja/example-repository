word=input("enter the word ti find palindrome or not = ")
reverse=(word[::-1])
if word==reverse:
    print("The word is palindrome")
else:                                                      #find the palindrome word
    print("The word is not palindrome")    



number=int(input("enter the values= "))
copy=number
reverse=0
while number>0:
    reminder=number%10                 #palindrome program
    reverse=reverse*10+reminder
    number=number//10
if copy==reverse:
    print("\nThis is palindome number") 
else:
    print("\nthis is not palindrome number")    







# number=int(input("enter the values= "))
# print(number)
# b=[]
# for i in str(number):
#     b.append(i)
# c=b[::-1]                                           #this is concept not palindrome i am just try
# d="".join(c)
# print(d)
# if number==d:
#     print("palindrome number")
# else:
#     print("not palindrome number")    


