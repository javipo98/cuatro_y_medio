import os.path
# with open("Excersises.csv") as Excersises:
#     excersises_list = []

# with open("codewars.csv") as codewars:
#     codewars_list = []
#     if "Grasshopper" in codewars:
#         for lines in codewars:
#             print(lines)

def codewars_command(exercises_db = "exercises.csv" , codewars_db = "codewars.csv" , processed_info = "processed.csv"):
    if  os.path.isfile(exercises_db):
        exercises = open(exercises_db , "r")
    if  os.path.isfile(codewars_db):
        codewars = open(codewars_db , "r")
    if  os.path.isfile(processed_info):
        with open(processed_info , "w") as processed:
            processed.write("")
        processed = open(processed_info , "a")
    else:
        processed = open(processed_info , "a")
    print(exercises.closed,codewars.closed,processed.closed)
codewars_command()
