import random 
alfabeto = "a b c d e f g  h i j k l m n ñ o p q r s t u v w x y z"
#1 funcion para escoger una palabra ramdon

def seleccionarPalabra():
  lineas=open("frutas_verduras.txt").readlines()
  palabra = random.choice(lineas).rstrip()
  return palabra  
#palabra=seleccionarPalabra()
#print(palabra)

#2funcion entrada del teclado

def entradaUsuario():
  letra= input("Introduzca una letra: ")
  return letra.lower()


#print(letra)

#3funciona actualizar jugada

def actualizarJugada(palabra,letra,jugada):
  n_letra = len(palabra)
  for i in range (0, n_letra):
    if palabra[i]== letra:
      jugada[i]=letra 
  return jugada
  
#palabra = seleccionarPalabra()
#letra = entradaUsuario()
#jugada =["_"]*len(palabra)
#jugada = actualizarJugada(palabra,letra,jugada)
#print(jugada)

#4 FUNCION ACTUALIZAR ALFABETO 
def actualizarAlfabeto (letra,alfabeto):
  alfabeto = alfabeto.replace(letra," ")
  return alfabeto

#alfabeto = actualizarAlfabeto(letra,alfabeto)
##print (alfabeto) 
#5imprimir resultados de la jugada en pantalla
def imprimirActualizacion(alfabeto,jugada):
  print(f"jugada:{jugada}")
  print(f"letra disponibles:{alfabeto}")

#imprimirActualizacion(alfabeto,jugada)

#6verificar jugada 
def verificarJugada( suposicion,palabra):
  success = False
  if suposicion == palabra:
    success = True
  return success
#success = verificarJugada ("timate",palabra)
#print(success)