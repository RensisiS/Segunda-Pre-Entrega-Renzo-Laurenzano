DC = {}
def registro(DC):
  print("Ingrese sus datos")
  print("Usuario")
  user = input()
  print("Contraseña")
  pwd = input()

  DC.update({user: pwd})

def login(DC):
  print("Ingrese sus datos")
  print("Usuario")
  user = input()
  print("Contraseña")
  pwd = input()
  if user in DC and DC[user] == pwd:
    print("Bienvenido, acceso correcto")
  else:
    print("¡usuario o contraseña inválidos!")

def visualizar(DC):
  print(DC)

registro(DC)
login(DC)
visualizar(DC)