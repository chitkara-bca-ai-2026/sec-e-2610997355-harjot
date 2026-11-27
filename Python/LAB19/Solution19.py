while True:
    N=int(input("Select number\n1)Write\n2)Read\n3)Exit\n Enter:"))
    if N==1:
        f=open("Solution19.txt","w")
        x=input("What to write:")
        f.write(x+"\n")
        f.close()
        print("Text has been successfully written and save in the file named (Solution19.txt),to check enter 2")
    elif N==2:
        f=open("Solution19.txt","r")
        print(f.read())
        f.close()
    elif N==3:
        print("Thank you for using NOTES MANAGEMENT SYSTEM,Goodbye!")
        break
