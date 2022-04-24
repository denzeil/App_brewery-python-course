import math

test_h=int(input("Enter the height: "))
test_w=int(input("Enter the width: "))
coverage=5
def paint_calc(height,width,cover):
    total=(height*width)/cover

    print("You'll need ",math.ceil(total), "cans of paint")
paint_calc(height=test_h,width=test_w,cover=coverage)