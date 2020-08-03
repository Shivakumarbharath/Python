try:
    num = int(input("Enter even  a number"))
    assert num % 2 == 0, "You Hav  Enterd a odd number"


except AssertionError:
    print("You Hav  Enterd a odd number")
