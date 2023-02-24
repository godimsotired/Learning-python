
print("This is a calculator.\nWhat would you like to do?")

dictionary = {"1": "addition", "2": "subtraction", "3": "multiplication", "4": "division", "5": "finding the exponent"}
selected_function = int(input("Enter your math function:\n- 1 for addition\n- 2 for subtraction\n- 3 for multiplication\n- 4 for division\n- 5 for finding the exponent "))

func = dictionary.get(str(selected_function))
if func == None:
    print("Not a function")
    exit(1)
number1 = float(input("Enter your first number "))
number2 = float(input("Enter your second number "))
print("You selected " + dictionary[str(selected_function)])
# print("you selected " + str(selected_function))

if selected_function == 1:
    print(float(number1) + float(number2))

elif selected_function == 2:
    print(float(number1) - float(number2))

elif selected_function == 3:
    print(float(number1) * float(number2))

elif selected_function == 4:
    print(float(number1) / float(number2))

elif selected_function == 5:
    print(pow(float(number1), float(number2))),

