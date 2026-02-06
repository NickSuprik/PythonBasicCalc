#powershell line to run script:
#python SCRIPTNAMEHERE.py

#name = input("Enter your name:")
#print(f"Hello {name}")
first_number = None
while first_number is None:     
    try:
         first_number = int(input("Enter the first number: "))
    except ValueError:
       print("That's not a valid number.")

second_number = None
while second_number is None:     
    try:
         second_number = int(input("Enter the second number: "))
    except ValueError:
       print("That's not a valid number.")
       
        #if second_number == 0
            #print("That's not a valid number.")

#print(f"Do you want a {fav2} {fav1} with {fav3} legs?")