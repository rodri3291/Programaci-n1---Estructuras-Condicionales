# Estructuras condicionales
# Ejercicio 1
edad = int(input("Ingrese su edad:"))
if edad > 18:
    print("Eres mayor de edad") 
    
    
# Ejercicio 2 
nombre = input("Ingrese su nombre:")
nota = int(input("Ingrese su nota:"))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

    
# Ejercicio 3
numero = int(input("Ingrese un número:"))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
    
    
# Ejercicio 4
edad = int(input("Ingrese su edad:"))
if edad < 12:
    print("Niño")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto joven")
elif edad >= 30:
    print("Adulto")
    
    
# Ejercicio 5
len("8 y 14")
contraseña = input("Ingrese una contraseña:")
if contraseña == len("8 y 14"):
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# Ejercicio 6
import statistics
numeros_aleatorios = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8]
mean = statistics.mean(numeros_aleatorios)
median = statistics.median(numeros_aleatorios)
mode = statistics.mode(numeros_aleatorios)
print("Media:", mean)
print("Mediana:", median)
print("Moda:", mode)
print("-"*20)
if mean > median and median > mode:
    print("La distribución presenta una sesgo positivo")
elif mean < median and median < mode:
    print("La distribución presenta un sesgo negativo")
else:
    print("La distribución no presenta un sesgo")
    
        
# Ejercicio 7
vocales = "aeiouAEIOU"
palabra = input("Ingrese una palabra o frase:")
if palabra[-1] in vocales:
    print(palabra + "!")
else:
    print(palabra)
    
    
# Ejercicio 8
nombre = input("Ingrese su nombre: ")
numero1 = input("Ingrese numero 1: ")
numero2 = input("Ingrese numero 2: ")
numero3 = input("Ingrese numero 3: ")
nombre_mayusculas = nombre.upper()
nombre_minusculas = nombre.lower()
nombre_titulo = nombre.title()
print(numero1 + nombre_mayusculas)
print(numero2 + nombre_minusculas)
print(numero3 + nombre_titulo)  


# Ejercicio 9
magnitud = float(input("Ingrese la magnitud del sismo: "))
if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
elif magnitud >= 7:
    print("Extremo")

    
# Ejercicio 10  
hemisferio = input("Ingrese el hemisferio (Norte/Sur): ").strip().lower()
mes = input("Ingrese el mes: ").strip().lower()
dia = int(input("Ingrese el día: "))
if hemisferio == "norte":
    if (mes == "diciembre" and dia >= 21) or (mes in ["enero", "febrero"]) or (mes == "marzo" and dia < 20):
        print("Invierno")
    elif (mes == "marzo" and dia >= 20) or (mes in ["abril", "mayo"]) or (mes == "junio" and dia < 21):
        print("Primavera")
    elif (mes == "junio" and dia >= 21) or (mes in ["julio", "agosto"]) or (mes == "septiembre" and dia < 22):
        print("Verrano")
    elif (mes == "septiembre" and dia >= 22) or (mes in ["octubre", "noviembre"]) or (mes == "diciembre" and dia < 21):
        print("Otoño")
    elif hemisferio == "sur":
        if (mes == "junio" and dia >= 21) or (mes in ["julio", "agosto"]) or (mes == "septiembre" and dia < 22):
            print("Invierno")
        elif (mes == "septiembre" and dia >= 22) or (mes in ["octubre", "noviembre"]) or (mes == "diciembre" and dia < 21):
            print("Primavera")
        elif (mes == "diciembre" and dia >= 21) or (mes in ["enero", "febrero"]) or (mes == "marzo" and dia < 20):
            print("Verano")
        elif (mes == "marzo" and dia >= 20) or (mes in ["abril", "mayo"]) or (mes == "junio" and dia < 21):
            print("Otoño")  