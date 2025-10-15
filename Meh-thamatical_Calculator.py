def addition(a, b):
    sum = a + b
    return sum
def subtraction(a, b):
    sum = a - b 
    return sum
def multiply(a, b):
    sum = a * b
    return sum
def divide(a, b):
    if b == 0:
        return "Did you fail highschool math? Dividing by zero is impossible, you moron!"
    sum = a / b
    return sum
def exponent(a, b):
    sum = a ** b
    return sum

print("Welcome to the basic Meh-thematical Calculator")
blue=int(input("Your first number: "))
green=int(input("Your second number: "))
print("What basic mathmatical operation would you like to execute today?\n"
      "1. Addition\n"
      "2. Subtraction\n"
      "3. Multiplication\n"
      "4. Division\n"
      "5. Exponentialize")
grass=int(input("Your answer: "))
if grass == 1:
     pink = addition(blue, green)
     print(f"Amazing choice (Too easy). Your answer is {pink}")
elif grass == 2:
     red = subtraction(blue, green)
     print(f"Your so lame. Can you PLEASE pick something harder? Your answer is {red}")
elif grass == 3:
     yellow = multiply(blue, green)
     print(f"This is peanuts compared to addition. Your answer is {yellow}")
elif grass == 4:
    purple = divide(blue, green)
    if isinstance(purple, str): 
        print(purple)
    else:
        print(f"LAME. LAME. LAME. Dear god please pick something harder. Your answer is {purple}")
elif grass == 5:
    gray = exponent(blue, green)
    print(f"Congratulaions you managed to bore me even more. Your answer is {gray}")