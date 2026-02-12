#powershell line to run script:
#python SCRIPTNAMEHERE.py

num1 = None
while num1 is None:     
    try:
         num1 = float(input("Enter the first number: "))
    except ValueError:
       print("That's not a valid number.")

num2 = None
while num2 is None:     
    try:
         num2 = float(input("Enter the second number: "))
    except ValueError:
       print("That's not a valid number.")

def option_one():
    print(num1 + num2)
def option_two():
    print(num1 - num2)
def option_three():
    print(num1 * num2)
def option_four():
    if num2 == 0:
        print("Error: Division by Zero") #might not be needed, due to pythons built in div/zero error messaging
    else:
        print(num1 / num2)

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