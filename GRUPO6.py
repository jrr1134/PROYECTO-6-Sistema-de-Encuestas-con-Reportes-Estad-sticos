#RICARDO
print ("=====INICIAR ENCUESTA=====") #usamos un print escrito como "encuesta" para que sirva de titulo del proyecto
print ("\n*Escriba SALIR para terminar la encuesta*\n")

encuestados = [] #nombre de la lista donde se van a guardar todas las personas que respondan la encuesta.
continuar = "si" #variable usada para controlar la continuacion del ciclo que se usara luego.

#se usa un while para que las preguntas sigan una atras de la otra Hasta llegar a la ultima del bloque de codigo.
while continuar.lower() == "si": #mientras la variable continuar contenga la palabra "si",el bloque de codigo que está dentro del while se va a repetir.
    #.lower() funcion que se usa en este caso para que "si" sea valido en maysuculas o minusculas

    respuestas = {} #crea un diccionario vacío llamado persona para guardar todas las respuestas de un ususario

    # Pregunta 1
    while True:
        p1 = input("1 - Apoyas al Licey o las Aguilas? (Escriba solo uno:) ").lower() #p1 variable que guarda la respuesta y .lower() metodo que lo pone en minuscula
        if p1 == "salir":
            continuar = "no"
            break
        if p1 in ["licey","aguilas"]:
            break
        print("Valor no válido, intenta otra vez.")
    if continuar == "no":
        break
    respuestas["equipo"] = p1 #Pide al usuario el equipo y lo guarda en el diccionario.


    # Pregunta 2
    while True:
        p2 = input("2 - ¿Cuál es tu edad? (solo números): ")
        if p2.lower() == "salir":
            continuar = "no"
            break
        try:
            p2 = int(p2)
            break
        except:
            print("Valor no válido, intenta otra vez.")
    if continuar == "no":
        break
    respuestas["edad"] = p2 #p2 variable que guarda la edad como número entero y la guarda en el diccionario.


    # Pregunta 3
    while True:
        p3 = input("3 - Género (M/F): ").upper()
        if p3.lower() == "salir":
            continuar = "no"
            break
        if p3 in ["M","F"]:
            break
        print("Valor no válido, intenta otra vez.")
    if continuar == "no":
        break
    respuestas["genero"] = p3 #p3 variable que guarda el género, .strip() quita espacios, .upper() lo pone en mayúscula y lo guarda en el diccionario.


    # Pregunta 4
    while True:
        p4 = input("4 - ¿Usas internet todos los días? (si/no): ").lower()
        if p4 == "salir":
            continuar = "no"
            break
        if p4 in ["si","no"]:
            break
        print("Valor no válido, intenta otra vez.")
    if continuar == "no":
        break
    respuestas["internet"] = p4 #p4 variable que guarda la respuesta sobre uso de internet y .lower() lo pone en minúscula antes de guardarlo en el diccionario.


    # Pregunta 5
    while True:
        p5 = input("5 - ¿Del 1 al 5 qué tan satisfecho estás con tu conexión a internet?: ")
        if p5.lower() == "salir":
            continuar = "no"
            break
        try:
            p5 = int(p5)
            if 1 <= p5 <= 5:
                break
        except:
            pass
        print("Valor no válido, intenta otra vez.")
    if continuar == "no":
        break
    respuestas["satisfaccion"] = p5 #p5 variable que guarda la calificación como número entero y la guarda en el diccionario.

    encuestados.append(respuestas) #Guarda todo el diccionario de respuestas en la lista de encuestados.

    continuar = input("¿Deseas agregar otro encuestado? (si/no/salir): ") #Variable que guarda si se repite la encuesta o no.
    if continuar.lower() == "salir":
        continuar = "no"


print("\nFIN DE LA PREGUNTAS") #print que muestra en pantalla indicando que no hay mas preguntas
print()
print() #esos print fue para dejar espacio y se vea mas organizado














#JEREMY
print("\n***REPORTES ESTADISTICOS***") #print para mostrar que comenzarán los reportes estadísticos.
total = len(encuestados) #cuenta cuántas personas respondieron la encuesta y lo guarda en total con la funcion len y la lista guardada de los diccionarios
print("Total de encuestados:", total) #función print() que muestra en pantalla el total de encuestados

#contador de hombre y mujer
hombres = 0 #una variable entera con contador de hombres inicia en 0
mujeres = 0 #una variable entera con contador de mujeres inicia en 0

#lista de encuestado de genero (hombre y mujer)
for p in encuestados: #bucle 'for p in encuestados' recorre cada elemento de la lista encuestados y lo guarda en la variable p
    if p["genero"] == "M": #condicional if, revisa si el valor asociado a la clave "genero" en el diccionario p es "M"
        hombres += 1 #operación de incremento; suma 1 al contador de hombres si la condición anterior se cumple
    elif p["genero"] == "F": #condicional elif, si la condición anterior no se cumple, revisa si el género es "F"
        mujeres += 1 #operación de incremento, suma 1 al contador de mujeres si el género es "F"


#calcula el procentaje en numero entero
if total > 0: #condicional if; revisa si total es mayor que 0 para evitar dividir entre cero
    porc_hombres = int((hombres / total) * 100) #operación matemática; calcula el porcentaje de hombres en entero
    porc_mujeres = int((mujeres / total) * 100) #operación matemática; calcula el porcentaje de mujeres en entero
else: #condicional else; si total no es mayor que 0
    porc_hombres = porc_mujeres = 0 #asignación múltiple; asigna 0 a ambos porcentajes

 #imprime el resultado de la lista
print("\n1. Porcentaje por género:") #función print() que muestra un título del reporte
print("Hombres:", porc_hombres, "%") #función print() que muestra el porcentaje de hombres
print("Mujeres:", porc_mujeres, "%") #función print() que muestra el porcentaje de mujeres











#CARLOS
#estadistica de edad
if total > 0: # condicional if revisa si total es mayor que 0 para evitar dividir entre cero
    suma_edades = sum(p["edad"] for p in encuestados) # función y expresión generadora sum() suma todas las edades de los diccionarios en la lista
    promedio_edad = suma_edades / total # operación matemática divide la suma de edades entre total para obtener el promedio
else: # condicional else si total no es mayor que 0
    promedio_edad = 0 # asignación que asigna 0 al promedio de edad

print("\n2. Promedio de edad:", promedio_edad) # función; print() muestra el promedio de edad

#estadistica de equipos
conteo_licey = 0 # variable entera contador para Licey inicia en 0
conteo_aguilas = 0 # variable entera contador para Aguilas inicia en 0

for p in encuestados: # bucle for recorre cada diccionario en la lista encuestados
    if p["equipo"] == "licey": # condicional if revisa si el valor de "equipo" es "licey"
        conteo_licey += 1 # operación de incremento; suma 1 al contador de Licey
    elif p["equipo"] == "aguilas": # condicional elif revisa si el valor de "equipo" es "aguilliceyas"
        conteo_aguilas += 1 # operación de incremento; suma 1 al contador de Aguilas

print("\n3. Conteo de apoyo a equipos:") # función print() muestra el título del reporte de equipos
print("Licey:", conteo_licey) # función print() muestra el total de personas que apoyan Licey
print("Aguilas:", conteo_aguilas) # función print() muestra el total de personas que apoyan Aguilas









#OLIVER
#estadistica del uso de internet
si_internet = 0 #variable contador para respuestas "si"
no_internet = 0 #variable contador para respuestas "no"

for p in encuestados: #p se usa para recorrer las respuestas en el bucle for
    if p["internet"] == "si": #condicional if revisa si la respuesta es "si"
        si_internet += 1 #incrementa contador si es "si"
    elif p["internet"] == "no": #condicional elif revisa si la respuesta es "no" si no fue "si"
        no_internet += 1 #incrementa contador si es "no"

if total > 0: #condicional if evita division entre cero
    porc_si_internet = (si_internet / total) * 100 #calculo porcentaje de "si"
    porc_no_internet = (no_internet / total) * 100 #calculo porcentaje de "no"
else: #condicional else si no hay encuestados
    porc_si_internet = porc_no_internet = 0 #asigna 0 a ambos porcentajes

print("\n4. Porcentaje de uso de internet diario:") #funcion print() muestra titulo del reporte
print("Si:", porc_si_internet, "%") #funcion print() muestra porcentaje de "si"
print("No:", porc_no_internet, "%") #funcion print() muestra porcentaje de "no"

#estadistica de satisfaccion del usuario
if total > 0: #condicional if verifica que haya encuestados
    lista_satisfaccion = [p["satisfaccion"] for p in encuestados] #lista por comprension con todas las calificaciones
    prom_satis = sum(lista_satisfaccion) / total #funcion sum() suma todos los valores y se divide por total para el promedio de las respuestas
    max_satis = max(lista_satisfaccion) #funcion max() obtiene el valor mayor
    min_satis = min(lista_satisfaccion) #funcion min() obtiene el valor menor
else: #Si no hay ningun encuestado
    prom_satis = max_satis = min_satis = 0 #asigna 0 a todas las variables

print("\n5. Satisfaccion del internet:") #funcion print() muestra titulo del reporte
print("Promedio:", prom_satis) #funcion print() muestra promedio de satisfaccion
print("Maxima:", max_satis) #funcion print() muestra cantidad maxima
print("Minima:", min_satis) #funcion print() muestra cantidad minima



#sistema de guardado
with open("resultados_encuesta.txt", "w", encoding="utf-8") as f:
    f.write("*** RESULTADOS DE LA ENCUESTA ***\n\n")
    f.write(f"Total encuestados: {total}\n")
    f.write(f"Hombres: {porc_hombres}%\n")
    f.write(f"Mujeres: {porc_mujeres}%\n\n")

    f.write(f"Promedio de edad: {promedio_edad}\n\n")

    f.write("Apoyo a equipos:\n")
    f.write(f"Licey: {conteo_licey}\n")
    f.write(f"Aguilas: {conteo_aguilas}\n\n")

    f.write("Uso de Internet:\n")
    f.write(f"Si: {porc_si_internet}%\n")
    f.write(f"No: {porc_no_internet}%\n\n")

    f.write("Satisfacción con Internet:\n")
    f.write(f"Promedio: {prom_satis}\n")
    f.write(f"Máxima: {max_satis}\n")
    f.write(f"Mínima: {min_satis}\n")

print("\nArchivo 'resultados_encuesta.txt' creado exitosamente.")

print("\n-----FIN DEL REPORTE----- \nPASE FELIZ RESTO DEL DIA\n")