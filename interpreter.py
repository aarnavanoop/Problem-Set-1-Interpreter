def calculate(saying):
    x,y,z = saying.split(" ")
    x = float(x)
    z = float(z)
    
    if y == "+":
        print(x + z)   
    elif y == "-":
        print(x - z)
    elif y == "*":
        print(x*z)
    elif y == "/":
        print(x/z)

def main():
    user_calc = input("What's the equation you would like to solve?: ")
    calculate(user_calc)



main()