year=int(input("year:"))
print("==============================================================================")
print("    CALENDER YEAR VERIFICATION    ")
print("==============================================================================")
print(f"Enter Year:{year}")
print("-------------------------------------------------------------")
if year>0:
    if (year%400)!=0:
        if (year%100)!=0:
            if (year%4)!=0:
                print(F"Year:{year}")
                print(F"Status:Common Year")
                print(F"Days in Year:365 days")
                print(F"Days in Februry:28 days")
                print(f"Reason:Not divisble by 4 and 100")

            else:
                print(F"Year:{year}")
                print(F"Status:Leap Year ")
                print(F"Days in Year:366 days")
                print(F"Days in Februry:29 days")
                print(f"Reason:divisble by 4 but not by 100")
                
        else:
            print(F"Year:{year}")
            print(F"Status:Century Year ")
            print(F"Days in Year:365 days")
            print(F"Days in Februry:28 days")
            print(f"Reason:divisble by 100")
            
    else:
        print(F"Year:{year}")
        print(F"Status: Leap Year and Century Year ")
        print(F"Days in Year:366 days")
        print(F"Days in Februry:29 days")
        print(f"Reason:divisble by 400")
                    
        
else:
    print(year,"INVALID YEAR",end=":")