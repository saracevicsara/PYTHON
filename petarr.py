
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







































