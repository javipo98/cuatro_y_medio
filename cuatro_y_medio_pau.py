with open("Excersises.csv") as Excersises:
    excersises_list = []

with open("codewars.csv") as codewars:
    codewars_list = []
    if "Grasshopper" in codewars:
        for lines in codewars:
            print(lines)