f=open("Solution20.txt","w")
f.write("9:00AM:System server startup verified.\n")
f.write("10:30AM:Morning attendance synchronized.\n")
f.write("02:15PM:Network security patch applied.\n")
f.close()
while True:
    N=int(input("Select Number\n1)Add\n2)Read\n3)Exit"))
    if N==1:
        f=open("Solution20.txt","a")
        x=input("Information to add:")
        f.write(x)
        f.close()
    elif N==2:
        f=open("Solution20.txt","r")
        print(f.read())
        f.close()
    elif N==3:
        print("Thank you,Goodbye!")
        break
        
