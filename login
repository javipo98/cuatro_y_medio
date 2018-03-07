def paubot()
  matricula = (input("Ingrese su matricula"))
  if len(matricula)==8 and matricula.isnumeric():
    return True 
  else:
    print ("matricula", matricula, "no es correcta")

paubot()
