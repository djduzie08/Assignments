def check_tri(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else:
        return False

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if check_tri(a, b, c):
    print("The triangle is a right-angled triangle.")
else:
    print("The triangle is not a right-angled triangle.")