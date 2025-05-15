usuarios = []

def registrar_usuario():
    print("\n--- Registrar nuevo Usuario ---")
    correo = input("Correo electrónico: ")
    for usuario in usuarios:
        if usuario['correo'] == correo:
            print("Error: el correo ya está registrado.")
            return
    nombre = input("Nombre de usuario: ")
    contrasena = input("Contraseña: ")
    usuarios.append({
        "correo": correo,
        "nombre": nombre,
        "contrasena": contrasena
    })
    print("✅ Registro exitoso.")

def iniciar_sesion():
    print("\n--- Inicio de Sesión ---")
    correo = input("Correo electrónico: ")
    contrasena = input("Contraseña: ")
    for usuario in usuarios:
        if usuario['correo'] == correo and usuario['contrasena'] == contrasena:
            print(f"✅ Bienvenido/a, {usuario['nombre']}.")
            return True
    print("❌ Correo o contraseña incorrectos.")
    return False

def cambiar_contrasena():
    print("\n--- Cambiar Contraseña ---")
    correo = input("Correo electrónico: ")
    for usuario in usuarios:
        if usuario['correo'] == correo:
            actual = input("Contraseña actual: ")
            if usuario['contrasena'] == actual:
                nueva = input("Nueva contraseña: ")
                usuario['contrasena'] = nueva
                print("🔐 Contraseña actualizada correctamente.")
                return
            else:
                print("❌ Contraseña actual incorrecta.")
                return
    print("❌ Usuario no encontrado.")
