num = input("Enter a number: ")

if int(num) > 0:
    print("You entered a number more than zero")
elif int(num) < 0:
    print("You entered a number less than zero")
    if int(num) > -10:
        print("You entered a number more than -10")
    else:
        print("You entered a number less than -10")
else:
    print("You entered a zero")

name = input()
A = 'Yes' if name != "Test" else 'No'
print(A)
