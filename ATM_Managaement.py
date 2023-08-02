management="Wellcome To My Bank ATM".center(50)
print(management,"\n\n\n")
chance=3
Balance=1000
while chance>0:
    pin=int(input("please enter your pin:\n"))
    
    if pin ==2348:
        print("your enter your pin correctly")
        print("press==>1 for your balance enquiry")
        print("press==>2  to make a withdrawal")
        print("press==>3 to pay in")
        print("press==>4 to remove your card")
        option=int(input("what you like to choose :\n==>"))
        while option !={1,2,3,4}:
            if option==1:
                print("====================================\n")
                print(f"your Balance is: ${Balance}\n")
                print("=====================================\n")
                pass
                option=int(input("what you like to choose :\n==>"))
                # break
            elif option ==2:
                withdraw=int(input("Enter your withdrawal amount:\n $"))
                print("========================================\n")
                Balance=Balance-withdraw
                break
            elif option ==3:
                payment=int(input("Enter the amount you want to pay in:\n $"))
                print("=========================================\n")
                Balance=Balance+payment
                break
            elif option ==4:
                print("your card is removing\n")
                print("Thank you\n")
                print("==========================================\n\n")
                break
            else:
                print("you have entered a wrong input:")  
                break
    else:
        chance=chance-1
        print("you have entered a wrong pin,please Try again")
        print(f"you have {chance} chance")