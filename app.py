# Simple Calculator 


def  Addition(a,b):
    return a+b;

def Subraction (a,b):
    return a- b;

def Multiply(a,b):
    return a* b;


def Divide(a,b):
 if b== 0 :
    return "Division by zero"
    return a/b;
print("Select operation")
print("Addition")
print("Subraction")
print("Multiply")
print("Divide")


choice = input ("Enter choice(Enter choice (1-2-3-4))")
if choice in ["1","2","3","4"]:
    num1=float(input("Enter first number  :"))
    num2=float(input("Enter second number :"))



if choice =="1":
        print(f"The result is equal to {Addition(num1,num2)}")


elif choice =="2":
    print(f"The result is equal to {Subraction(num1,num2)}")

elif choice =="3":
    print (f"The result is equal to {Multiply(num1,num2)}")

elif choice =="4":
    print(f"The result is equal to {Divide (num1,num2)}")