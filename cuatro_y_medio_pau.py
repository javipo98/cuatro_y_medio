import datetime
import os.path #libreria que permite verificar la existencia de los archivos

# with open("Excersises.csv") as Excersises:
#     excersises_list = []

# with open("codewars.csv") as codewars:
#     codewars_list = []
#     if "Grasshopper" in codewars:
#         for lines in codewars:
#             print(lines)

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
<<<<<<< HEAD
                due_date_day = int(exercise_line[due_date][3:5])
                due_date_month = int(exercise_line[due_date][0:2])
                due_date_year = int("20"+exercise_line[due_date][6:9])
                due_date_exsercises = datetime.date(due_date_year,due_date_month,due_date_day)
                print(due_date_exsercises)
                print(slug_pulled)
=======
                #print(slug_pulled)

>>>>>>> c41cca485743282b53028fa129b5f9918f055dfd
                with open(codewars_db) as codewars:
                    
                    for check in codewars:
<<<<<<< HEAD
                        
=======
                        #print(check)
>>>>>>> c41cca485743282b53028fa129b5f9918f055dfd
                        if check == "id,name,slug,completedLanguages/0,completedAt\n":
                            continue 
                        elif slug_pulled == check.split(",")[slug]:
                            codewars_line = check.split(",")
                            completed_at_month = int(codewars_line[completed_at][5:7])
                            completed_at_day = int(codewars_line[completed_at][8:10])
                            completed_at_year = int(codewars_line[completed_at][0:4])
                            completed_at_date = datetime.date(completed_at_year,completed_at_month,completed_at_day)
                            to_be_written += (",True" + "," + check.split(",")[completed_at])
                            print(to_be_written)
<<<<<<< HEAD
                            break
                            




=======
                            break 
                    else:
                        to_be_written += (",False,None,False")
                        print(to_be_written)
            
>>>>>>> c41cca485743282b53028fa129b5f9918f055dfd
        





#####################Testing##############################################################################################
    # print(exercises_splitted,batch,due_date,name,url,codewars_splitted,slug,completed_at)



    # print(exercises.closed,codewars.closed,processed.closed)
    # exercises.close()
    # codewars.close()
    # processed.close()
    # print(exercises.closed,codewars.closed,processed.closed)


codewars_command()
