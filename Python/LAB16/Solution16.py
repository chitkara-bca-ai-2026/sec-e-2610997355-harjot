#input function
def ask():
    a=int(input("num1:"))
    b=int(input("num2:"))
    return a,b
#addition function
def addition():
    a,b=ask()
    z=a+b
    return z
#subtraction function
def subtraction():
    a,b=ask()
    y=a-b
    return y
#multiplication function
def multiplication():
    a,b=ask()
    x=a*b
    return x
#division function
def division():
    a,b=ask()
    w=a/b
    return w
#modulus function 
def modulus():
    a,b=ask()
    v=a%b
    return v
#power function 
def power():
    a,b=ask()
    v=a**b
    return v


print("=======================================================")
print("  ENTERPRISE MODULAR UTILITY CALCULATOR  ")
print("=======================================================")
x=5
while x<10:
    u=int(input("Select an operation:\n1.Addition\n2.Subtration\n3.Multiplication\n4.Division\n5.Modulus\n6.Power\n7.View Calculation History\n8.Exit :"))
    if u==1:
        print(f"Addition:{addition()}")
    if u==2:
        print(f"Subtraction:{subtraction()}")
    if u==3:
        print(f"Multiplication:{multiplication()}")
    if u==4:
        print(f"Division:{division()}")
    if u==5:
        print(f"Modulus:{modulus()}")
    if u==6:
        print(f"Power:{power()}")
    if u==8:
        print("Thank you for using Modular Utility Calculator,Goodbye! ")
        break