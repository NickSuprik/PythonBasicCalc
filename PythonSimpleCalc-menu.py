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

# ------ Menu ------
menuItems = ['1. Addition', 
             '2. Subtraction', 
             '3. Multiplication', 
             '4. Division'] #remembember divison by zero logic print("That's not a valid number.")
print('Choose an operation: \n')   # print menu title and top border
 
for menuItem in menuItems:      # cycle through menu items
    print(menuItem)             # show menu item
 
choice = input('Please enter your choice: ')    # get user selection


#print(f"Do you want a {fav2} {fav1} with {fav3} legs?")