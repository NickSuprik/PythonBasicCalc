#powershell line to run script:
#python SCRIPTNAMEHERE.py

first_number = None
while first_number is None:     
    try:
         first_number = float(input("Enter the first number: "))
    except ValueError:
       print("That's not a valid number.")

second_number = None
while second_number is None:     
    try:
         second_number = float(input("Enter the second number: "))
    except ValueError:
       print("That's not a valid number.")

def option_one():
    print(first_number + second_number)
def option_two():
    print(first_number - second_number)
def option_three():
    print(first_number * second_number)
def option_four():
    if second_number == 0:
        print("Error: Division by Zero") #might not be needed, due to pythons built in div/zero error messaging
    else:
        print(first_number / second_number)

# ------ Menu ------
menuItems = ['1. Addition', 
             '2. Subtraction', 
             '3. Multiplication', 
             '4. Division'] #remembember divison by zero logic print("That's not a valid number.")
print('Choose an operation: \n')   # print menu title and top border
 
for menuItem in menuItems:      # cycle through menu items
    print(menuItem)             # show menu item
 
choice = input('Please enter your choice: ')    # get user selection
if choice == '1':
    option_one()
elif choice == '2':
    option_two()
elif choice == '3':
    option_three()
elif choice == '4':
    option_four()