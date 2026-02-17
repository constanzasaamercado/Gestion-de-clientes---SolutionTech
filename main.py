import modulos.menu as menu
from modulos.funciones_utiles import registrar_log
from modulos.modelos import Usuario
from modulos.gestion_clientes import GestionClientes

def login():
    usuarios_db = [Usuario("admin", "1234", "admin"), Usuario("venta1", "5678", "vendedor")]
    
    intentos = 3
    while intentos > 0:
        u = input("Usuario: ")
        p = input("Contraseña: ")
        for user in usuarios_db:
            if user._Usuario__username == u and user.verificar_password(p):
                return user
        intentos -= 1
        print(f"❌ Error. Intentos restantes: {intentos}")
    return None

def ejecutar_sistema():
    menu.mostrar_bienvenida()
    
    # Autenticación
    sesion_activa = login()
    if not sesion_activa:
        print("❌ Acceso denegado.")
        registrar_log("SESIÓN: Intento de acceso fallido")
        return
    
    registrar_log(f"SESIÓN: Usuario '{sesion_activa}' ha ingresado al sistema.")
    
    # Crear instancia de GestionClientes
    gestor = GestionClientes()

    while True:
        opcion = menu.menu_principal()

        if opcion == "1":
            gestor.ingresar_cliente()
            
        elif opcion == "2":
            gestor.modificar_cliente()
            
        elif opcion == "3":
            if sesion_activa.es_admin():
                gestor.eliminar_cliente()
            else:
                print("❌ ERROR: Solo el administrador puede eliminar registros.")
                registrar_log(f"ADVERTENCIA: Usuario '{sesion_activa}' intentó eliminar sin permisos.")

        elif opcion == "4":
            gestor.visualizar_clientes()

        elif opcion == "5":
            registrar_log(f"SESIÓN: Usuario '{sesion_activa}' cerró el sistema.")
            print("👋 Saliendo del sistema... ¡Hasta pronto!")
            break
        else:
            print("❌ Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    ejecutar_sistema()