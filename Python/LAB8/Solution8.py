sn=input("student name:")
rn=int(input("roll number:"))
for i in range(1,6):
    marks=int(input("marks:"))
    if marks>0 and marks<=100:
        if i==1:
            english=marks
        elif i==2:
             hindi=marks
        elif i==3:
            maths=marks
        elif i==4:
            ssc=marks
        elif i==5:
            science=marks
    else:
        print("Marks Invalid")   
tot=english+hindi+maths+ssc+science
per=(tot/500)*100
print("========================================================")
print("    SCHOOL RESULT PROCESSING   ")
print("========================================================")
print(f"Enter Student Name:{sn}")
print(f"Enter Roll Number:{rn}")
print(f"--------Enter Marks for 5 subjects (0-100)-----------")
print(f"Enter marks English:{english}")
print(f"Enter marks Hindi:{hindi}")
print(f"Enter marks Maths:{maths}")
print(f"Enter marks Social Science:{ssc}")
print(f"Enter marks Science:{science}")
print("========================================================")
print("     STUDENT REPORT CARD")
print("========================================================")
print(f"Student Name:{sn}")
print(f"Roll Number:{rn}")
print("---------------------------------------")
print(f"Total Marks:{tot}")
print(f"Percentage:{per}")
if per>=40:
    r="PASS"
else:
    r="FAIL"
print(f"Result:{r}")
if per>=90 and per<=100:
    g="A+"
    remarks="Outstanding"
elif per>=80 and per<=89:
    g="A"
    remarks="Excellent"
elif per>=70 and per<=79:
    g="B" 
    remarks="Very Good"
elif per>=60 and per<=69:
    g="C"
    remarks="Good"
elif per>=50 and per<=59:
    g="D"
    remarks="Satisfactory"
elif per>=40 and per<=49:
    g="PASS"
    remarks="Pass"
else:
    g="FAIL"
    remarks="Fail"
print(f"Grade:{g}")
print(f"Remarks:{remarks}")