import random

con = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z',]
voc = ['a', 'e', 'i', 'o', 'u']


cantidad = int(input("Introduzca la cantidad de pares de caracteres de su palabra: "))

def generar():
    word = ""
    for i in range(cantidad):
        
        randcon = random.randrange(0,20)
        randvoc = random.randrange(0,4)
        car_a = con[randcon]
        car_b = voc[randvoc]
        preword = car_a + car_b
        word += preword
    print(word)
        

generar()

    