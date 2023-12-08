#Simple Calculator using concepts like Functions,If-elif-else conditions,try-except-finally.
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
if __name__=="__main__":
    print("Simple Calc:")
    print("Type appropriate symbols to get calculations")
    print("1.For Addition:+" )
    print("2.For Subtraction:-")
    print("3.For Multiplication:*")
    print("4.For Division:/")
    try:
        option = input("Enter your calculation type(eg:+):")
        if(option=='+'):
            a=int(input("A:"))
            b=int(input("B:"))
            c=add(a,b)
            print(f"{a}+{b} is {c}")
        elif(option=='-'):
            a=int(input("A:"))
            b=int(input("B:"))
            c=sub(a,b)
            print(f"{a}-{b} is {c}")
        elif(option=='*'):
            a=int(input("A:"))
            b=int(input("B:"))
            c=mul(a,b)
            print(f"{a}*{b} is {c}")
        elif(option=='/'):
            a=int(input("A:"))
            b=int(input("B:"))
            c=div(a,b)
            print(f"{a}/{b} is {c}")
        else:
            print("You have entered invalid input!")
            print("Try typing (+ - * /)")
    except TypeError as e:
        print(f"Error:{e}")
    except ValueError as e:
        print(f"Error:{e}")
    finally:
        print("Thank you")    
