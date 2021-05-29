#REALIZAR PROGRAMA EN PYTHON QUE AL MOMENTO DE DIGITAR UN DATO, 
#(PUEDE SER NUMERO O LETRA), MUESTRE EN PANTALLA QUE OPERACIONES LOGICAS
#CUMPLEN O NO CUMPLEN LAS CONDICIONES

#CONJUNCION
print("CONJUNCION (AND)")
num_uno = int (input("escribir un numero mayor a 2 y menor a 5: "))
if num_uno > 2 and num_uno < 5:
    print ("El numero ", num_uno,"CUMPLE LA CONDICION.\n")

else:
    print("el numero ",num_uno,"NO CUMPLE LA CONDICION. \n")


#DISYUNCION
print("DISYUNCION (OR)")
palabra = input("escribir 'SI' O 'NO':  ")
if palabra =='SI' or palabra =='YES':
    print ("CUMPLE LA CONDICION.\n")

else:
    print("NO CUMPLE LA CONDICION. \n")

    

#NEGACION
print("CONJUNCION (AND)")
num_uno = int (input("escribir el numero 5: "))
if not num_uno == 5:
    print ("EL NUMERO ES DIFERENTE DE CUANTRO Y SI CUMPLE LA CONDICION.\n")

else:
    print("EL NUMERO ES IGUAL A CINCO Y NO CUMPLE LA CONDICION. \n")
