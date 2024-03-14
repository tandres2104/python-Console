import random

Nombre = "Ingresa Tu nombre:  "
snomb = input(Nombre)


def ingresar_numero():
  while True:
    Edad = input("Ingrese Su Edad: ")
    try:
      numero = float(Edad)
      return numero
    except ValueError:
      print("Por favor, ingrese Numeros Enteros.")


numero_ingresado = ingresar_numero()


def jugar_adivina_numero():
  numero_secreto = random.randint(1, 10)
  intentos = 0

  print("Bienvenido al juego de adivinar el número.")
  print("He elegido un número entre 1 y 10. ¡Adivina cuál es!")
  while True:
    if intentos <= 2:
      intento = int(input("Introduce tu Numero: "))
      intentos += 1

      if intento < numero_secreto:
        print("El número secreto es mayor. ¡Inténtalo de nuevo!")
      elif intento > numero_secreto:
        print("El número secreto es menor. ¡Inténtalo de nuevo!")
      else:
        print(
            f"Felicidades, has adivinado el número secreto {numero_secreto} en {intentos} intentos.  ¡ Tu nombre Es! {snomb}"
        )
        break

    else:
      print("Vuelve. ¡A intentar!")
      # Aca llamamos la funcion mensj_jue()
      mensj_jue()
      break


def mensj_jue():
  mens = input("Quieres Jugar un juego de nueros? (yes/no)")

  mensYs = "yes"
  menNt = "no"

  if mens == mensYs:
    print("Ok, Comenzemos")
    # Aca llamamos la funcion jugar_adivina_numero
    jugar_adivina_numero()

  else:
    print("Ok, Adios")


if numero_ingresado >= 18:
  print("Su Nombre Es: " + snomb + " " + " Y Tienes" + " " +
        str(numero_ingresado) + " Años")
  # Aca llamamos la funcion mmensj_jue()
  mensj_jue()

else:
  print("Eres Menos de Edad " + " " + "Adios" + " " + Nombre)
