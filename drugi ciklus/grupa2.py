# mylist = ["apple", "banana", "cherry"]
#             # 0         1           2
# raznovrsna_lista=["ajlana",12,7.7,True]

# print(raznovrsna_lista[0])
# print(mylist[0])
# 0="apple"
# 1="banana"
# 2="cherry"
# mylist=["sara",16,9.6]
# print(mylist[2])
# lista_stringova=["adem","amar","ali","kadir","ali"]
# print(lista_stringova)
# lista_brojeva=[10,11,11,13,9,14,10,11,11,12]
# print(lista_brojeva[3])
#----------------------------------------------------------------
# mylist=["sara","saracevic",16,9.6,2006]
        #   0        1        2  3    4
# print(mylist[1])
# 0="sara"
# 1="saracevic"
# 2=16
# 3=9.6
# 4=2006
# broj=17
# broj2=76 
# mylist=["sara","saracevic",16,9.6,2006]
# print(mylist[-1])
# print(mylist[4])
# mylist=["sara","saracevic",16,9.6,2006]
# mylist[-1]=15
# print(mylist)
# mylist=["sara","saracevic",16,9.6,2006]
# mylist.append("python")
# print(mylist)
# # .append()
# mylist=["sara","saracevic",16,9.6,2006]
# mylist.insert(1,"python")
# print(mylist)
# mylist=["sara","saracevic",16,9.6,2006]
# mylist.remove(16)
# print(mylist)

# mylist=["davud","dolicanin",10.27,2011]
# # mylist.append(9)
# # mylist.insert(2,"sara")
# mylist.remove(2011)
# print(mylist)
# mylist=["sara","saracevic",16,9.6,2006]
# mylist.pop(1)
# print(mylist)
# 0="sara"
# 1="saracevic"
# 2=16
# mylist=["davud","dolicanin",10.27,2011]
# # del mylist[1]
# # mylist.pop(1)
# print(mylist)
# mylist=["davud","dolicanin",10.27,2011]
# mylist.clear()
# print(mylist)
# listica=[1,6,7,8,18,-34,89,-998754]
# for i in listica:
#         print(i)


# listica=[1,6,7,8,18,-34,89,-998754]
# for i in listica:
#         if i<0:
#                 print("negativan broj je:",i)



# /3 fizz
# /5 buzz
# /3 i /5 fizzbuzz
# %==0
#------------------------------------------------
# lista=[3,5,15,9,8,7,90,4567]
# for i in lista:
#         if i%3==0 and i%5==0:
#                 print("fizzbuzz")
#         elif i%3==0:
#                 print("fizz")
#         elif i%5==0:
#                 print("buzz")
#         else:
#                 print("nije ni fiz ni buzz ni fizzbuzz")
#--------------------------------------------------
# [3,5,6,7,332,5]
# for
# if
# prin

# list=[1,2,34,123,24,53,5,6,3,53,2,23]
# for i in list:
#         if i%5==0:
#                 print(i)




# list=[1,2,34,123,24,53,5,6,3,53,2,23]
# broj=int(input("unesite neki"))
# list.insert(2,broj)
# print(list)



# list=[1,2,34,123,24,53,5,6,3,53,2,23]
# broj=int(input("unesite neki broj"))
# list.append(broj)
# print(list)
# [9,5,699,6,4]
# 699
# []
# list=[1,2,34,123,24,53,5,6,3,53,2,23]
# for i in list:
#         broj=int(input("unesute neki broj"))
#         if i==broj:
#                 print(list.clear())
#         else:
#                 print(list.append(broj))

# mylist=[23,24,28,56,98,54,13,18,27,24,98753,2,76543,234567] 
# for i in mylist:
#         if i %2==0:
#             print("parni brojevi su:",i)
        
        #     [5,7,8,9,9]
        #     ako je poslednji element liste 5 
        #     vrati "DA"
        #     ako nije vrati "NE"


# lista=[3,6,89,5,790,8,21,0,5]
# if lista[-1]==5:
#         print("DA")
# else:
#         print("NE")


# inputa 10-na kraju liste
# print("kraj casa")
# else:
#         print("vezbamo jos")

# lista=[1,66,7,8,8,3,22,44]
# broj=int(input("unesite neki broj"))
# lista.append(broj)
# if lista[-1]==10:
#         print("kraj casa")
# else:
#         print("vezbamo jos")



# lista=[7,55,43,2,99]
# broj=int(input("unesite neki broj"))
# lista.append(broj)
# if broj==10:
#         print("kraj casa")
# else:
#         print("vezbamo jos")


# lista=[123,5,7,8,[45,89,4,["sara",7]],90605,"iiwuhfw",0.9,True,["jcibcwu","SLihwch"]]
# lista[4][3].append(90)
# print(lista)

# lista=[123,5,7,8,[45,89,4,["sara",7]],90605,"iiwuhfw",0.9,True,["jcibcwu","SLihwch"]]
# print(len(lista))
# lista[9].insert(0,"sara")
# print(lista)


# myset = {"apple", "banana", "cherry"}
# print(myset)
# myset = {"apple", "banana", "cherry"}
# myset.add("pear")
# print(myset)

# myset = {"apple", "banana", "cherry"}
# myset2={"pear","watermellon","kiwi"}
# myset.update(myset2)
# print(myset)
# myset = {"apple", "banana", "cherry"}
# myset.discard("apple")
# print(myset)

# myset = {"apple", "banana", "cherry"}
# print(len(myset))
# list=[1,2,34,123,24,53,5,6,3,53,2,23]
# for i in list:
#         broj=int(input("unesute neki broj"))
#         if i==broj:
#                 list.clear()
#                 print(list)
#         elif  i!=broj:
#                 list.append(broj)
#                 print(list)
# thisset = {"apple", "banana", "cherry"}
# thisset.clear()
# print(thisset)
# tuple=("adem","kadir",10,True,5.7,945748)
# if "adem"in tuple:
#         print(tuple)

# tuple=("adem","kadir",10,True,5.7,945748)
# if 10==tuple[2]:
#         print("jes")
# moj_tuple=("adem","kadir",10,True,5.7,945748)
# tuple_list=list(moj_tuple)
# tuple_list.append("novi element")
# moj_tuple=tuple(tuple_list)
# print(moj_tuple)



# tt=("mehmed","zaimovic",5.9,2005)
# tuple_tate=list(tt)
# tuple_tate.pop(3)
# tt=tuple(tuple_tate)
# print(tt)


# ajlana=("ajlana","sacirovic",12,7.7)
# sacirovic=list(ajlana)
# sacirovic.insert(2,"lana")
# ajlana=tuple(sacirovic)
# print(ajlana)


# amar=("amar","dervisevic",9,9.12)
# dervisevic=list(amar)
# dervisevic.append(2)
# amar=tuple(dervisevic)
# print(amar)

# hamza=('hamza','curic',1,11,2010)
# for i in hamza:
#         print(i)


# mojtuple=(232,4321,6545,3567,2465,434)

# broj=int(input("unesite neki broj"))
# kadirovalista=list(mojtuple)
# kadirovalista.append(broj)
# mojtuple=tuple(kadirovalista)
# print(mojtuple)

# oo=("adem","tiganj","deka",2012,2.4)
# broj=int(input("unesite neki broj"))
# tuple_list=list(oo)
# tuple_list.insert(3,broj)
# oo=tuple(tuple_list)
# print(oo)
# obj={
#        " car":"audi",
#         "animal":'cat',
#          " car":"audi",
#         "animal":'cat',
#          " car":"audi",
#         "animal":'cat',
#          " car":"audi",
#         "animal":'cat'
# }

# https://www.w3schools.com/python/
# lista=["amar","dervisevic",9,9.12]
# lista.append(-1)
# print(lista

# davud={"davud","dolicanin",10.27,2011}
# davud.discard("davud")
# print(davud)
#-------------------------------------------------------------------
#                           Dictionary

#car={
#         "brand":"bmw",
#         "model":"M3",     
#         "godina":"2019",
#         }

# informacije={
#         "ime":"sara",
#         "prezime":"saracevic",
#         "godina-rodjenja":"2006"
# }

# print(len(informacije))
# informacije={
#         "ime":"sara",
#         #key    value
#         "prezime":"saracevic",
#         "godina-rodjenja":[9,6,2006],
#         "broj":4,
#         'float':9.7,
#         "bool":True
        
#         }
# print(informacije)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["year"]

# print(x+5)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.get("year")

# print(x+5)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.keys()

# print(x)

# car = {
# "brand": "Ford"
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()

# print(x) #before the change

# car["color"] = "white"

# print(x) #after the change


# dictionary = {
#         "Brand":"audi",
#         "model":"L8",
#         "godina":2017
# }
# print(dictionary)


# car={
#      "brand":"bmw",
#      "model":"m3",
#      "godina":2000,
# }
# x=car.keys()
# print(x)

# thisdict = {
#         "brand":"bmw",
#         "model":"Mustang",
#         "year":2013
# }
# thisdict["year"] = 2018
# print(thisdict)



# thisdict = {
#         "brand":"bmw",
#         "model":"Mustang",
#         "year":2013
# }
# thisdict.update({"year":2022})
# print(thisdict)       


# thisdict = {
#         "brand":"bmw",
#         "model":"Mustang",
#         "year":2013
# }
# thisdict.update({"fjgugwehuw":2022})
# print(thisdict)   
# dict={
#         "ime":"sara",
#         "prezime":"saracevic",
#         "godine":16
# }
# dict["godine"]=17

# print(dict)


# dict={
#         "ime":"sara",
#         "prezime":"saracevic",
#         "godine":16
# }
# dict.update({"godine":17})
# print(dict)



# thisdict={
#         'ime':'hamza',
#         'prezime':'curic',
#         'godine':'2010'
# }
# thisdict['godina'] = 12
# print(thisdict)



# dict={ 'ime':'hamza',
#         'prezime':'curic',
#         'godine':'2010' 
# }
# dict.update({"godina":10})
# print(dict)

# thisdict={
#         'ime':'davud',
#         'prezime':'dolicanin',
#         'godine':11,
# }
# thisdict.pop('ime')
# print(thisdict)
# thisdict={
#         'ime':'davud',
#         'prezime':'dolicanin',
#         'godine':11,
# }
# thisdict.popitem()
# print(thisdict)

# thisdict={          
#         "ime":"ajlana",
#         "prezime":"sacirovic",
#         "godine":12
# }
# thisdict.clear()
# print(thisdict)

# thisdict={
#         "ime":"amar",
#         "prezime":"dervisevic",
#         "godina":9

# }
# del thisdict['ime']
# print(thisdict)
# thisdict={
#         "ime":"amar",
#         "prezime":"dervisevic",
#         "godina":9

# }
# for i in thisdict:
#         print(thisdict[i])

# thisdict={
#         "ime":"sara",
#         "prezime":"saracevic",
#         "godine":16
# } 

# for i in thisdict:
#         print(i)
# thisdict={
#         "ime":"sara",
#         "prezime":"saracevic",
#         "godine":16
# }

# for i in thisdict:
#         print(thisdict[i])



# thisdict={         
#           "ime":"ajlana",
#           "prezime":"sacirovic",
#           "godine":12,

# }
# for i in thisdict.keys():
#         print(i)
 
# for i in thisdict.values():
#         print(i)