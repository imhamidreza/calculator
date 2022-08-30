num1 = float(input("inter num1:"))
num2 = float(input("inter num2:"))
operation = input("""please choose a operator:
+ for addition
- for subtaction
* for multiplication
/ for division
:""")
if operation == "+":
    output = num1+num2
    print("{}+{}={}" .format(num1, num2, output))
elif operation == "-":
    output = num1-num2
    print("{}-{}={}" .format(num1, num2, output))
elif operation == "*":
    output = num1*num2
    print("{}*{}={}" .format(num1, num2, output))
elif operation == "/":
    output = num1/num2
    print("{}/{}={}" .format(num1, num2, output))
else:
    print("again choose a operator!")
