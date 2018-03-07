import datetime
import os.path #libreria que permite verificar la existencia de los archivos

def login(matricula):#Creamos una funcion, en la cual se creara los algoritmos para que dicha funcion pueda ejecutarse.
  #matricula = (input("Ingrese su matricula")) #Creamos una variable en la cual introducimos un input el cual mostrara que debemos ingresar para completar dicho paso.
  if len(matricula)==8 and matricula.isnumeric():#Aqui decimos que la variable debe tener una longitud de 8 digitos y debe ser numerica.
    logged = matricula      #Guardamos la matricula introducida en una variable (si es valida)
    return True #Asi retornamos que es verdadero cuando cumple cada paso correctamente.
  else: 
    print ("matricula", matricula, "no es valida") #Y un else, que de lo contrario a lo planteado anterior, imprima que la matricula es incorrecta


def codewars_command(exercises_db = "exercises.csv" , codewars_db = "codewars.csv" , processed_info = "processed.csv"):
    
    if  os.path.isfile(exercises_db):               #Se abren los archivos
        with open(exercises_db) as exercises:
            exercises_splitted = exercises.readline().replace("\n","").split(",")       #Se obtiene el indice de cada renglon
            batch = exercises_splitted.index("batch")                                   #Esto es para evitar fallos si los documentos no estan organizados
            due_date = exercises_splitted.index("due_date")
            name = exercises_splitted.index("name")
            url = exercises_splitted.index("url")        
                                                    #Si el archivo "nuevo" ya esta creado, lo limpia
    else:                                           #   y escribe una primera linea con los renglones
        return "El archivo " + exercises_db + " no existe" 
    
    if  os.path.isfile(codewars_db):                
        with open(codewars_db) as codewars:
            codewars_splitted = codewars.readline().replace("\n","").split(",")
            slug = codewars_splitted.index("slug")
            completed_at = codewars_splitted.index("completedAt")
    else:
        return "El archivo " + codewars_db + " no existe"
    
    if  os.path.isfile(processed_info):
        with open(processed_info , "w") as processed:
            processed.write("")
        processed = open(processed_info , "a")
        processed.write("Batch,Exercise,Completed,DateCompleted,CompletedLate")
    else:
        processed = open(processed_info , "a")
        processed.write("Batch,Exercise,Completed,DateCompleted,CompletedLate")


    
    with open(exercises_db) as exercises:   
        for line in exercises:                                                      #Este for recorre el documento exercises
            if line == "batch,due_date,name,url,strict,extra\n":
                continue
            else:
                exercise_line = line.split(",")
                to_be_written = exercise_line[batch] + "," + exercise_line[name]        #En esta variable se va creando el string a escribir en processed
                slug_pulled = exercise_line[url][(exercise_line[url].index("kata")+5):] #Aqui se obtiene el slug del url de exercises
                
                due_date_day = int(exercise_line[due_date][3:5])
                due_date_month = int(exercise_line[due_date][0:2])
                due_date_year = int("20"+exercise_line[due_date][6:9])
                due_date_exercises = datetime.date(due_date_year,due_date_month,due_date_day)
                #print(due_date_exercises)
                #print(slug_pulled)
                with open(codewars_db) as codewars:
                    
                    for check in codewars:
                        
                        if check == "id,name,slug,completedLanguages/0,completedAt\n":
                            continue 
                        elif slug_pulled == check.split(",")[slug]:
                            codewars_line = check.split(",")

                            completed_at_month = int(codewars_line[completed_at][5:7])
                            completed_at_day = int(codewars_line[completed_at][8:10])
                            completed_at_year = int(codewars_line[completed_at][0:4])
                            completed_at_date = datetime.date(completed_at_year,completed_at_month,completed_at_day)
                             
                            to_be_written += (",True" + "," + check.split(",")[completed_at] + "," + str((due_date_exercises - completed_at_date).days <= 0))
                            to_be_written = to_be_written.replace("\n","")
                            print(to_be_written)
                            with open(processed_info,"a") as processed:
                                processed.write(to_be_written + "\n")
                            break
                    else:
                        to_be_written += (",False,None,False")
                        to_be_written = to_be_written.replace("\n","")
                        print(to_be_written)
                        with open(processed_info,"a") as processed:
                                processed.write(to_be_written + "\n")

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
          
          print(total_exercises, total_completed, total_late, total_missing)

  else:
    print("No se ha encontrado ningun archivo con informacion suficiente para crear un summary")
                            




        





#####################Testing##############################################################################################
codewars_command()
summary()
login()
