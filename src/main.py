from device_manager import agregar_dispositivo, listar_dispositivos, activar_modo_ahorro

def mostrar_menu():
    while True:
        print("\n=== Menú SmartHome ===")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Cambiar contraseña")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            cambiar_contrasena()
        elif opcion == "4":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    mostrar_menu()
