print("Computer Graphics TA 1 ---- Group 1")

while(1):
    print("Choices Available are : ")
    print("1.   Image to Sketch")
    print("2.   Image to Cartoon")
    print("3.   Image to Water Color")
    print("4.   Image to Color Sketch")
    print("5.   Image to Dark Sketch")
    print("0.   Exit")
    
    print("\n\n\n")
    
    opt = int(input("Enter Your Choice "))
    
    match opt:
        case 0:
            break

        case 1:
            print("1")

        case 2:
            print("2")
        
        case 3:
            print("3")

        case 4:
            print("4")

        case 5:
            print("5")

        case 6:
            print("6")
        case _:
            print("default")