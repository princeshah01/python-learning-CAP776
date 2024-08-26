x = int(input("Enter a number to know its word version: "))

match x:
    case 1:
        print("one")
    case 2:
        print("two")
    case _:
        print("don't know")