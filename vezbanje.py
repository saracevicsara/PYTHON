h=str(input("odaberite operaciju:"))
if h=="zbir":
    a=int(input("unesite neki broj"))
    b=int(input("unesite drugi broj"))
    print("zbir je;", a+b)
elif h=="razlika":
    a=int(input("unesite neki broj"))
    b=int(input("unesite drugi broj"))
    if a>b:
        print("razlika je:", a-b)
    elif b>a:
        print("razlika je",b-a)
elif h=="proizvod":
    a=int(input("unesite neki broj"))
    b=int(input("unesite drugi broj"))
    print("proizvod je:" , a*b)
elif h=="kolicnik":
    a=int(input("unesite neki broj"))
    b=int(input("unesite drugi broj"))
    print("kolicnik je:", a/b)
else:
    print("kraj")
