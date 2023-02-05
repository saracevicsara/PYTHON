
# dict = {
#     "ime" : "Petar",
#     "godine" : 17,
#     "skola" : True,
# }

# print(dict)
# print(dict["ime"])
# print(dict["skola"])

# for i in dict:
#     print(dict[i])


# for i in dict.values():
#     print(i)

# print(100 * "=")

# for i in dict.keys():
#     print(i)

# print(100 * "=")

# for i,j in dict.items():
#     print(i,j)


# ----------------------------------

# recnik = {
#     "ime" : "Petar",
#     "godine" : 17,
#     "skola" : True,
#     "zanrovi" : ["rock", "pop", "hip-hop"],
# }

# # recnik["grad"] = "Novi Pazar"


# # recnik["ime"] = "Petar Petrovic"

# # print(recnik)

# recnik.update({"vreme" : "nocno"})

# print(recnik)

# ---------------------------------

# recnik = dict()

# n = int(input("Unesite broj: "))

# for i in range(1, n+1):
#     recnik[i] = i**2

# print(recnik)

# -----------------------------

# sampleDict = {
#     "class" : {
#         "students" : {
#             "name" : "Petar",
#             "marks" : {
#                 "math" : 70,
#                 "history" : 80,
#             }
#         }
#     }
# }


# print(sampleDict["class"]["students"]["marks"]["history"])


# ----------------


# dict = {
#     "emp1" : {
#         "name" : "Petar", "salary" : 500
#     },
#     "emp2" : {
#         "name" : "Marija", "salary" : 600
#     },
#     "emp3" : {
#         "name" : "Ana", "salary" : 700
#     }
# }

# for i in dict.values():
#     if i["name"] == "Marija":
#         i["salary"] = 1000
#         break
# print(dict)

# broj=int(input("unesite zeljeni broj"))
# if broj%3==0 and broj%5==0:
#     print("fizzbuzz")
# elif broj%5==0:
#     print("buzz")
# elif broj%3==0:
#     print("fizz")



# x=int(input("unesite prvi broj"))
# y=int(input("unesite drugi broj"))
# z=x+y
# if z>20:
#     print("suma je veca od 20")
# else:
#     print("suma je manja od 20")









# print("unosimo policu broj 1")
# print("unosimo policu broj 2")
# print("unosimo policu broj 3")
# print("unosimo policu broj 4")
# print("unosimo policu broj 5")
# print("unosimo policu broj 6")
# print("unosimo policu broj 7")
# for brojac in range(1,11):
#     print("unosimo poolicu broj",brojac)



# for i in range(1,21):
#     print(i)


# for i in range(2,11,2):
#     print(i)

# for i in range(10,0,-1):
#     print(i)



# broj=int(input("unesite neki broj"))
# for i in range(broj,0,-1):
#     print(i)

# broj=int(input("unesite neki broj"))
# for i in range(0,broj+1,2):
#      print(i)


# broj_ucenika=int(input("unesite koliko ima ucenika u odeljenju"))
# broj=int(input("unesite promenu brojaca"))
# for i in range(0,broj_ucenika+1,broj):
#     print(i)



# for i in range(1,11):
#     if i !=7:
#         print(i)

# lozinka="sara123"
# while True:
#     korisnik=str(input('unesite lozinku'))
#     if korisnik ==lozinka:
#         print("pogodili ste lozinku")
#         break
#     else:
#         print("pokusajte ponovo")


brojic=788

while True:
    korisnik=float(input("unesite neki broj"))
    if brojic==int(korisnik):
        print("uneli ste tacan broj")
    elif int(korisnik)==0:
        print("prekid")
        break
    elif int(korisnik)>brojic:
        print("vas broj je prevelik")
    elif int(korisnik)<brojic:
        print("vas je premali")







