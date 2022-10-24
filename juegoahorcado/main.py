from funciones import*
def main ():
  palabra = seleccionarPalabra()
  alfabeto= "a b c d e f g  h i j k l m n ñ o p q r s t u v w x y z"
  jugada =["_"]*len(palabra)
  for turno in range(5):
    print (f"\nTurno:{turno+1}")
    print("-"*20)
    #imprimir alfabeto y juaga
    imprimirActualizacion (alfabeto,jugada)
    #entrada usuario
    letra = entradaUsuario()
    #actualizar jugada y alfabeto
    jugada = actualizarJugada(palabra,letra,jugada)
    alfabeto = actualizarAlfabeto(letra,alfabeto)
    #imprimir actulizacion
    imprimirActualizacion(alfabeto,jugada)
    #preguntar al esuario si desea adivinar una la palabra
    check = input("desea adivinar la palabra?(s/n):")
    if check.lower()== "s":
      suposicion =input("introduzaca su respuesta: ").lower()
      success = verificarJugada(suposicion,palabra)
      if success:
        print("+"*20)
        print("siuuuu gano ")
        print("+"*20)
        break
      else:
        print("+"*20)
        print("la suposicion es incorrecta ")
        print("+"*20)
    if turno ==4:
      print("-"*20)
      print ("ahorcado pana")
      print ("-"*20)
  
if __name__=="__main__":
  main()






