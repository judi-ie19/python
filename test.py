#1. ADD
#2. SUBTRACT
#3. MULTIPLY
#4. DIVIDE
# print("select an operation to perform:")
from select import EPOLLEXCLUSIVE


print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")
 
Love= input("Enter your choice:")
num1=float(input("Enter number 1: "))
num2=float(input("Enter number 2: "))

if Love=="1":
    print(num1,"+",num2,"=",(num1+num2))
elif Love=="2":
    print(num1,"-",num2,"=", (num1-num2))
elif Love=="3":
    print( num1,"*",num2,"=", (num1*num2))
elif Love=="4":
    if num2==0.0:
        print("Divide by 0 error")
    else:
        print( num1,"/",num2,"=", (num1/num2))
else:
     print("invalid choice")

            



 





