# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")
# def my_function(country = ""):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# def cube(x):
#    r=x**3
#    return r
# print(cube(3))

# def fizz_buz(broj):
#     if broj %3==0 and broj %5==0:
#         return "fizz buzz"
#     elif broj %5==0:
#         return "buz"
#     elif broj%3==0:
#         return "fizz"
#     else:
#         return 'puko program'

# broj=int(input("Unesi neki broj"))

# print(fizz_buz(broj))
# def shut_down(rec):
#     if rec=="yes" or rec=="YES":
#         return "shutting down"
#     elif rec=="no" or rec=="NO":
#         return "shut down aborted"
#     else:
#         return "PUKO SISTEM BGM"
# rec=input("unesite da li zelite da ugasite vas racunar")
# print(shut_down(rec))


# speed_drivers
# ako je vrednost manja od 70km/h vrati OK
# ako je vrednost veca od 70km/h vrati trebalo bi da usporite
# ako je vrednost veca od 100km/h a manja 150 km/h policija je iza coska uspor!


# mydict={
#     "ime":"sara",
#     "prezime":"saracevic",
#     "godine":16,
#     "visina":178
# }
# for i in mydict.keys():
#     print(i)


# mydict={
#     "ime":"sara",
#     "prezime":"saracevic",
#     "godine":16,
#     "visina":178
# }

# for i in mydict.values():
#     print(i)

osnove_sifre={  
    "sifra1":456,
    "sifra2":789,
    "sifra3":349,
    "sifra4":961
}
korisnik=str(input("unesite jednu od 4 sifre"))
if korisnik=="sifra1":
    korisnikova_sifra=int(input("unesite vasu sifru"))
    print(str(osnove_sifre["sifra1"])+str(korisnikova_sifra))
elif korisnik=="sifra2":
    korisnikova_sifra=int(input("unesite vasu sifru"))
    print(str(osnove_sifre["sifra2"])+str(korisnikova_sifra))
elif korisnik=="sifra3":
    korisnikova_sifra=int(input("unesite vasu sifru"))
    print(str(osnove_sifre["sifra3"])+str(korisnikova_sifra))
elif korisnik=="sifra4":
    korisnikova_sifra=int(input("unesite vasu sifru"))
    print(str(osnove_sifre["sifra4"])+str(korisnikova_sifra))



