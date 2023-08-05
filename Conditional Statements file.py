def triangle():
    x = int(input("base length:"))
    y = int(input("height:"))

    area = (x * y) / 2

    print("area:", area)

    if area >= 10:
        print("bigger than 10")
    elif area < 10 and area > 0:
        print("smaller than 10")
    else:
        print("invalid inputs")

triangle()


def rectangle():
    z = int(input("length:"))
    a = int(input("width"))
    area = z * a

    print("area:", area)

    if area >= 10:
        print("bigger than 10")
    elif area < 10 and area > 0:
        print("smaller than 10")
    else:
        print("invalid inputs")

rectangle()


def circle():
    r = int(input("radius"))
    area = 3.14 * (r**2)
    print("area", area)

    if area >= 10:
        print("bigger than 10")
    elif area < 10 and area > 0 :
        print("smaller than 10")
    elif area <= 0:
        print("invalid inputs")
    else:
        print("non")


circle()