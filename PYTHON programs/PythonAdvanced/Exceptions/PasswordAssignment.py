class PasswordExceptionError(Exception):
    pass
class PasswordMatchingError(Exception):
    pass

pw=input("Enter Your Password : ")
try:
    if len(pw) < 8:
        raise PasswordExceptionError


except PasswordExceptionError:
    print("The Password should be atleast 8 charecters")

else:
    print("Password Created")

    pw1=input("Renter Your password : ")
    try:
        if pw1 != pw:
            raise PasswordMatchingError
    except PasswordMatchingError:
        print("The Password Renterd is not Matching")
        pw2 = input("Renter Your password : ")
        try:
            if pw2 is not pw:
                raise PasswordMatchingError
        except PasswordMatchingError:
            print("The Password Renterd is not Matching")
            print("Exceeded the number of attempts")
            exit()
    else:
        print("Password created")