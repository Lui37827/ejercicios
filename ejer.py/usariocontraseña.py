def validar_usuario():
    usuario_db = "mia khalifa"
    clave_db = "emilio123"
    usuario_ingresado = input("Ingrese su usuario: ")
    clave_ingresada = input("Ingrese su contraseña: ")
    if usuario_ingresado == usuario_db and clave_ingresada == clave_db:
        print("¡Acceso concedido! Bienvenido.")
    else:
        print("Acceso denegado. Usuario o contraseña incorrectos.")
validar_usuario()