# ime="sara"
# print(ime)

# ime=str(input("unesite svoje ime"))
# print(ime)


while True:
    broj =int(input('unesite broj u rasponu od 10 do 20'))
    if broj >=10 and broj <=20:
        print("cestitamo uneli ste broj u rasponu")
        break
    elif broj ==False:
        print("izlaz iz progama")
    else:
        print("niste uneli broj u rasponu pokusajte ponovo")


