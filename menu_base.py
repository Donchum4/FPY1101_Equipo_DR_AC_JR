def datos_DiegoRivera():
  print("Mi nombre es Diego Rivera y tengo 19 años.")
def datos_joaco():
    print("Mi nombre es joaquin y tengo 18 años.")
def datos_andres():
 print("Mi nombre es Andres Cereño y tengo 20 años")
# Menú base del programa
while True:
 print("\n--- MENÚ PRINCIPAL ---")
 print("1. Función de integrante 1")
 print("2. Función de integrante 2")
 print("3. Función de integrante 3")
 print("0. Salir")
 op = input("Seleccione opción: ")
 if op == "0":
    print("Programa finalizado.")
    break
 elif op == "1":
     datos_DiegoRivera()
 elif op == "2":
    datos_joaco()
 elif op == "3":
    datos_andres()
 else:
    print(" Opción inválida.")
