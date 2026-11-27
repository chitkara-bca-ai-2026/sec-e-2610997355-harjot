while True:
    N=int(input("Select number\n1)Factorial\n2)Fibonacci\n3)Exit\n Enter:"))
    if N==1:
        def fact(n):
            if n==1:
                return 1
            return n*fact(n-1)
        x=int(input("Enter Number:"))
        print(f"Factorial of {x} is {fact(x)}")
    elif N==2:
        def fib(n):
            if n==1:
                return 1
            if n==0:
                return 0
            return fib(n-1)+fib(n-2)
        x=int(input("Enter Number:"))
        print(f"Fibonacci of {x} is {fib(x)}")
    elif N==3:
        print(f"Thank you for using the mathematics learning tool.Goodbye!")
        break