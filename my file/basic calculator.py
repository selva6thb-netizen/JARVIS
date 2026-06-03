class base_calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b

class advanced_calculator(base_calculator):
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
a=int(input("Enter a number for a: "))
b=int(input("Enter a number for b: "))
method = input("Enter the method (add/subtract/multiply/divide): ")
if method == "add":
    result = advanced_calculator().add(a, b)
elif method == "subtract":
    result = advanced_calculator().subtract(a, b)
elif method == "multiply":
    result = advanced_calculator().multiply(a, b)
elif method == "divide":
    result = advanced_calculator().divide(a, b)
else:
    print("Invalid method. Please choose 'add', 'subtract', 'multiply', or 'divide'.")

if method in ["add", "subtract", "multiply", "divide"]:
 c=int(input("Enter a number for c: "))
if c==a+b or c==a-b or c==a*b or (b!=0 and c==a/b)  :
    print("The value of c is correct.")
else:
    print("The value of c is incorrect. The correct value is:", c)
