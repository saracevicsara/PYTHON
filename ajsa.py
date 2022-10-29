# ime="sara"
# print(ime)

# ime=str(input("unesite svoje ime"))
# print(ime)


# while True:
#     broj =int(input('unesite broj u rasponu od 10 do 20'))
#     if broj >=10 and broj <=20:
#         print("cestitamo uneli ste broj u rasponu")
#         break
#     elif broj ==False:
#         print("izlaz iz progama")
#     else:
#         print("niste uneli broj u rasponu pokusajte ponovo")


#----------------------------------------------------------------------------------------------------
# broj=7
# if broj >10:
#     print("broj je veci od 10")
# else:
#     print("broj je manji od 10")


# broj=int(input("unesite neki broj"))
# if broj>0:
#     print("pozitivan")
# else:
#     print("negativan")


# broj=int(input("unesite neki broj"))
# if broj %2==0:
#     print("broj je deljiv sa 2")
# else:
#     print("broj nije deljiv sa 2")


from platform import freedesktop_os_release


# operacija=str(input("unesite zeljenu operaciju(*,/,+,-)"))
# if operacija =="*":
#     a=int(input("unesite prvi broj"))
#     b=int(input("unesite drugi broj"))
#     print(a*b)
# elif operacija=="/":
#     a=int(input("unesite prvi broj"))
#     b=int(input("unesite drugi broj"))
#     print(a/b)
# elif operacija=="+":
#     a=int(input("unesite prvi broj"))
#     b=int(input("unesite drugi broj"))
#     print(a+b)
# elif operacija =="-":
#     a=int(input("unesite prvi broj"))
#     b=int(input("unesite drugi broj"))
#     print(a-b)


# <8 free

# >=8 <=18  200

# >65 100

# else 500

god=int(input("unesite svoje godine"))
if god<8:
    print("vozite se free")
elif god>=8 and god<=18:
    print("cena karte je 200")
elif god >65:
    print('cena karte je 100')
else:
    print("cena karte je 500")


