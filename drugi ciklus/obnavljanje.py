#OSNOVNI TIPOVI PODATAKA
#int-cele brojeve
#float-decimalne borijeve
#str-niz karaktera pod navodnicama
#bool-tacno i netacno
#----------------------------------------------
#NAREDBE
#print
#input
#USLOVI
# if 3>6:
# elif
# else:
#PETLJE
# 1.FOR PETLJA-ponavlja odredjeni deo koda 
#2.ponavlja deo koda dok se uslov ne ispuni
#--------------------------------------
# mojaLista = [1, 2, 3, 4]
# print('Lista', mojaLista, 'je dužine', len(mojaLista))



# lista=[1,2,3,4,-20,-8,-77]
# for i in lista:
#     if i < 0:
#         print("negativni brojevi su",i)
lista=[1,2,3,4,-20,-8,-77,15]
for i in lista:
    if i%3==0 and i%5==0:
        print("fizz buz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print('buzz')