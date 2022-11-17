def addition ():
    print("addition")
    n = float(input("Enter the number:"))
    t = 0
    ans = 0
    while n != 0:
        ans = ans + n
        t+=1
        n = float(input("Enter another number(0 to calculate):"))
    return[ans,t]
while True:
    list = []
    print("Calculator Project")
    print("Enter a for addition")
    c = input("")
    if c!= 'q':
        if c == 'a':
            list = addition()
            print("Ans = ", list[0], "total inputs", list[1])
    else:
        print("Sorry, the character is invalid")