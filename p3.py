OPER_LIST = "+ - * / "
z = 0
while True:
    while True:
        x = input ("Введите число x: ")
        if x.replace(".", "").isnumeric() or x == "":
            break
        else:
            print("это не число")
    if x == "":
        x = z
    else:
        x = float (x)
    print ("x = ", x )
    while True:
        y = input ("Введите число y: ")
        if y.replace(".", "").isnumeric() or y == "":
            break
        else:
            print("это не число")
    if y == "":
        y = z
    else:
        y = float (y)
    print ("y = ", y )
    while True:
        oper = input ("Введите операцию (+, -, *, /): ")
        if OPER_LIST.find(oper) > -1:
            break
        else:
           print("эта операция не поддерживается в данной версии") 
    if oper == "+":
        z = x + y
    elif oper == "-":
        z = x - y
    elif oper == "*":
        z = x * y
    elif oper == "/":
        z = x / y
    z = round(z, 4)
    print ("x " + oper + " y =", z)

