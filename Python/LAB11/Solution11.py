username=input("username:")
password=input("password:")
character=False
digit=False
uppercase=False
if len(password)>=8:
   character=True
for ch in password:
    if ch.isupper():
     uppercase=True 
    if ch.isdigit():
      digit=True
print(f" Enter your username:{username}")
print(f" Enter your password:{password}")
print("=============================================")
print("      PASSWORD VALIDATION REPORT")
print("=============================================")
print(f"Username:{username}")
print(f"Password:{password}")
print("\n")
print("----Validation Rules----")
print("[PASS] Minimum 8 characters ")
print("[PASS] Atleast one digit ")
print("[PASS] Atleast one uppercase letter ")
print("\n")
print("---Result---")
if character and digit and uppercase:
    print("Password is VALID!")
    print(f"Account created successfully for {username}")
else:
   print("Password is INVALID!")
print("=============================================")
    