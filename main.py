

def calculate(num1, num2,op):

        global result

        result=0

        if op =="1":
             
                result= num1 + num2

        elif op =="3":
               
                result= num1/num2
        

op = input("Choose the opertion that you desire (^u^)/ :\n 1- Addition\n 2- Subtraction\n 3- Division\n 4- Multiplication\n")

num1 = float(input("Please enter your first number (OwO):"))

num2 = float(input("Please enter your second number ('u'):"))

calculate(num1, num2,op)

print("This is your result \(>w<)/:",result)

