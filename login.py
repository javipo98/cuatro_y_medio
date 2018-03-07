def paubot(matricula):#Creamos una funcion, en la cual se creara los algoritmos para que dicha funcion pueda ejecutarse.
  matricula = (input("Ingrese su matricula")) #Creamos una variable en la cual introducimos un input el cual mostrara que debemos ingresar para completar dicho paso.
  if len(matricula)==8 and matricula.isnumeric():#Aqui decimos que la variable debe tener una longitud de 8 digitos y debe ser numerica.
    logged = matricula      #Guardamos la matricula introducida en una variable (si es valida)
    return True #Asi retornamos que es verdadero cuando cumple cada paso correctamente.
  else: 
    print ("matricula", matricula, "no es valida") #Y un else, que de lo contrario a lo planteado anterior, imprima que la matricula es incorrecta

def summary(processed_info = "processed.csv"):
  #import os.path

  #file_db = "archivo.csv"

  if  os.path.isfile(processed_info):
      with open(processed_info) as processed:
        if len(processed.readlines()) > 1:
          processed_splitted = processed.readline().replace("\n","").split(",")
          completed = processed_splitted.index("Completed")                                   #Esto es para evitar fallos si los documentos no estan organizados
          completed_late = processed_splitted.index("completedLate")

          total_exercises, total_completed, total_late, total_missing = len(lines), 0, 0, 0

          for my_line in processed.readlines():
            exercise = my_line.replace("\n","").split(",")
  
            if exercise[completed] == "True":
              total_completed += 1
            if exercise[completed_late] == "True":
              total_late += 1
          else:
            total_missing = total_exercises - total_completed
          
          print()

  else:
    print("No se ha encontrado ningun archivo con informacion suficiente para crear un summary")
      
      #file = open(file_db , "r") 
      
  #file_splitted = file.readline().replace("\n","").split(",")

  #lines = file.readlines()


  
  #print (exercise)

  #print (x,y,z)
  #x=la cantidad de lineas 
  #y=la entrega a tiempo
  #z= la cantidad de entrega tardia 




paubot(input("Ingrese su matricula"))
paubot(input("Ingrese su matricula"))
paubot(input("Ingrese su matricula"))
