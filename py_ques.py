# a=(7/10)*100
# print(a)
print("\tPython (one mark) questions!")
a=0
start=input("Are you interest! solve this Questions? (yes or no)\n\t\t=======>")
if start=="yes":
    print("lets go!")
else:
    quit()
print("------------------------------------------------\n")
first_question=input("1)who developed python programing language?\na)wick van rossum \nb)rasmus lerdorf\nc)Guido van rossum\n=====>")
if first_question=="Guido van rossum" or first_question=="c":
    print("Answer : Correct")
    a+=1
else:
    print("Answer : incorrect!") 
print("-------------------------------------------------\n")
second_question=input("2. Which type of Programming does Python support?\na) object-oriented programming\nb) structured programming\nc) functional programming\nd) all of the mentioned\n=====>")

if second_question=="object oriented programing" or second_question=="a":
    print("Answer : Correct")
    a+=1  
else:
    print("Answer : incorrect!")
print("--------------------------------------------------------\n")
Third_question=input("3. Which of the following is the correct extension of the Python file?\na) .python\nb) .pl\nc) .py\nd) .p\n=====>") 
if Third_question==".py" or Third_question=="c":
    print("Answer : Correct!")
    a+=1
else:
    print("Answer : incorrect")
print("----------------------------------------------------------\n")
fourth_question=input("4. Is Python code compiled or interpreted?\na) Python code is both compiled and interpreted\nb) Python code is neither compiled nor interpreted\nc) Python code is only compiled\nd) Python code is only interpreted\n=====>")
if fourth_question=="python code is both compiled and interpreted" or fourth_question=="a":
    print("Answer : Corrrect")
    a+=1
else:
    print("Answer : incorrect")
print("------------------------------------------------------------\n")
five=input("5. What will be the value of the following Python expression?\n\t4 + 3 % 5\na) 7\nb) 2\nc) 4\nd) 1\n=====>")
if five =="7" or five =="a":
    print("Answer : Correct")
    a+=1
else:
    print("Answer : incorrect")
print("--------------------------------------------------------------\n")
six=input("6. Which of the following is used to define a block of code in Python language?\na) Indentation\nb) Key\nc) Brackets\nd) All of the mentioned\n=====>")
if six=="indentation" or six=="a":
    print("Answer : Correct")
    a+=1
else:
    print("Answer : incorrect")
print("----------------------------------------------------------------\n")
seven=input("7. Which keyword is used for function in Python language?\na) Function\nb) def\nc) Fun\nd) Define\n=====>")
if seven=="def" or seven=="b":
    print("Answer : Correct")
    a+=1
else:
    print("Answer : incorrect")
print("-----------------------------------------------------------------\n")
eight=input("8. Which of the following character is used to give single-line comments in Python?\na) //\nb) #\nc) !\nd) /*\n=====>")
if eight=="#" or eight=="b":
    print("Answer : Correct")
    a+=1
else:
    print("Answer : incorrect")
print("-------------------------------------------------------------------\n")
nine=input("9. Which of the following functions can help us to find the version of python that we are currently working on?\na) sys.version(1)\nb) sys.version(0)\nc) sys.version()\nd) sys.version\n=====>")
if nine =="sys.version" or nine =="d":
    print("Answer : Correct")
    a+=1
else:
    print("Answer : incorrect")
print("---------------------------------------------------------------------\n")    
ten=input("19. Which of the following is the truncation division operator in Python?\na) |\nb) //\nc) /\nd) %\n=====>")
if ten=="//" or ten=="b":
    print("Answer : Correct")
    a+=1
else:
    print("Answer : incorrrect")

print("||----------------------------------------||")
print("Total Right Answer:",str((a/10)*100),"Marks")
print("||-----------------------------------------||")

                 

