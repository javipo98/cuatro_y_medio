def paubot()#Creamos una funcion, en la cual se creara los algoritmos para que dicha funcion pueda ejecutarse.
  matricula = (input("Ingrese su matricula")) #Creamos una variable en la cual introducimos un input el cual mostrara que debemos ingresar para completar dicho paso.
  if len(matricula)==8 and matricula.isnumeric():#Aqui decimos que la variable debe tener una longitud de 8 digitos y debe ser numerica.
    return True #Asi retornamos que es verdadero cuando cumple cada paso correctamente.
  else:
    print ("matricula", matricula, "no es correcta")

paubot()
