#Library Book Collection
book=("Python Crash Course by Eric Matthes(2019)|Genre:Programming","Automate the Boring Stuff by Al Sweigart(2020)|Genre:Programming","Artificial Intelligence:A Modern Approach by Stuart Russell(2021)|Genre:AI","Clean Code by Robert C. Martin(2008)|Genre:Software Engineering")
x=5
while x<10:
    s=int(input("Select An Operation    1)View Cataloged Books  2)Add New Book Record  3)View Unique Library Categories  4)Add Category To Student Wishlist  5)Run Category Gap Analysis  6)Exit  :"))
    if s==1:
        for i in book:
            print(i)
    if s==2:
        y=input("add book details(name,author,year,genre in prescribed format):")
        r=list(book)
        r.append(y)
        z=tuple(r)
        print(z)
    if s==3:
        l=set(book)
        print(l)
    if s==4:
        m=input("Student wishlist(enter book in prscribed format):")
        n=[]
        n.append(m)
        print(n)
        t=set(n)
    if s==5:
        c=t-l
        q=[]
        q.append(c)
        print(q)
    if s==6:
        print(f"Thankyou for using the library manager.Goodbye!")
        break