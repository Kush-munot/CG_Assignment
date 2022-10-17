import package as p

if __name__=="__main__":
    # image_to_sketch()
    # image_to_oilPaint()
    # image_to_colorSketch()
    # image_to_darkSketch()
    # image_to_waterColor()
    # image_addition()
    # image_subtraction()
    # bgr_hsv()
    # smooth_image()
    # image_translation()
    # bilateral_filter()
    print("Computer Graphics TA 1 ---- Group 1")
    

    while(1):
        print("Choices Available are : ")
        print("1.   Image to Sketch")
        print("2.   Image to Oil Paint")
        print("3.   Image to Color Sketch")
        print("4.   Image to Dark Sketch")
        print("5.   Image to Water Color")
        print("6.   Image Addition")
        print("7.   Image Subtraction")
        print("8.   Get Hue Saturation Value")
        print("9.   Smooth Image")
        print("10.  Image Translation")
        print("11.  Bilateral Image Filter")
        print("0.   Exit")
        
        print("\n\n\n")
        
        opt = int(input("Enter Your Choice"))
        
        match opt:
            case 0:
                break
            case 1:
                p.image_to_sketch()
                print("1")

            case 2:
                p.image_to_oilPaint()
                print("2")
            
            case 3:
                p.image_to_colorSketch()
                print("3")

            case 4:
                p.image_to_darkSketch()
                print("4")

            case 5:
                p.image_to_waterColor()
                print("5")

            case 6:
                p.image_addition()
                print("6")
            
            case 7:
                p.image_subtraction()
                print("7")
            
            case 8:
                p.bgr_hsv()
                print("8")
            
            case 9:
                p.smooth_image()
                print("9")
            
            case 10:
                p.image_translation()
                print("10")
            
            case 11:
                p.bilateral_filter()
                print("11")
                
            case _:
                print("default")