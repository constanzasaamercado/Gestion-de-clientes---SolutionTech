import csv
from .modelos import Cliente, ClienteRegular, ClientePremium, ClienteCorporativo
from .funciones_utiles import registrar_log
from .validaciones import validar_correo, validar_rut

class GestionClientes:
    def __init__(self):
        self.lista_clientes = []
        self.cargar_clientes_desde_csv()
    
    # ...existing code...

    def cargar_clientes_desde_csv(self):
        """Carga los clientes desde el archivo CSV al iniciar"""
        try:
            with open("clientes.csv", "r", encoding="utf-8") as archivo:
                lector = csv.DictReader(archivo)
                for fila in lector:
                    # Crear el objeto según el tipo
                    if fila['tipo_cliente'] == 'Regular':
                        cliente = ClienteRegular(
                            fila['rut'], 
                            fila['nombre'], 
                            fila['correo'],
                            fila['dato_especifico'] == 'True'
                        )
                    elif fila['tipo_cliente'] == 'Premium':
                        cliente = ClientePremium(
                            fila['rut'],
                            fila['nombre'],
                            fila['correo'],
                            fila['beneficios']  # Cambiado de dato_especifico a beneficios
                        )
                    elif fila['tipo_cliente'] == 'Corporativo':
                        cliente = ClienteCorporativo(
                            fila['rut'],
                            fila['nombre'],
                            fila['correo'],
                            fila['dato_especifico']  # Esto toma "Alpha S.A."
                        )
                    self.lista_clientes.append(cliente)
            registrar_log(f"Clientes cargados: {len(self.lista_clientes)}")
        except FileNotFoundError:
            registrar_log("Archivo clientes.csv no encontrado. Se creará uno nuevo.")
        except Exception as e:
            registrar_log(f"ERROR al cargar CSV: {e}")

    # ...existing code...


    def guardar_datos_csv(self):
        """Guarda todos los clientes en el CSV"""
        try:
            with open("clientes.csv", "w", newline="", encoding="utf-8") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(['rut', 'nombre', 'correo', 'tipo_cliente', 'dato_especifico', 'beneficios'])
                
                for cliente in self.lista_clientes:
                    if isinstance(cliente, ClienteRegular):
                        escritor.writerow([
                            cliente.rut, 
                            cliente.nombre, 
                            cliente.correo, 
                            'Regular', 
                            cliente.plan_basico, 
                            'Plan Estándar'
                        ])
                    elif isinstance(cliente, ClientePremium):
                        escritor.writerow([
                            cliente.rut, 
                            cliente.nombre, 
                            cliente.correo,
                            'Premium', 
                            cliente.membresia,  # dato_especifico
                            'Gestor VIP'        # beneficios
                        ])
                    elif isinstance(cliente, ClienteCorporativo):
                        escritor.writerow([
                            cliente.rut, 
                            cliente.nombre, 
                            cliente.correo,
                            'Corporativo', 
                            cliente.razon_social,    # dato_especifico (empresa)
                            'Descuentos exclusivos'  # beneficios
                        ])
            registrar_log("Datos guardados en CSV exitosamente")
        except Exception as e:
            registrar_log(f"ERROR al guardar CSV: {e}")


    
    def existe_cliente(self, rut):
        """Verifica si un RUT ya existe en la lista"""
        for cliente in self.lista_clientes:
            if cliente.rut == rut:
                return True
        return False
    
    def ingresar_cliente(self):
        """Solicita datos y agrega un nuevo cliente"""
        print("\n--- REGISTRO DE NUEVO CLIENTE ---")
        rut = input("RUT (formato XX.XXX.XXX-X): ")
        
        if not validar_rut(rut):
            print("❌ RUT inválido")
            registrar_log(f"ERROR: RUT inválido ingresado: {rut}")
            return
        
        if self.existe_cliente(rut):
            print("❌ Este RUT ya está registrado")
            return
        
        nombre = input("Nombre completo: ")
        correo = input("Correo electrónico: ")
        
        if not validar_correo(correo):
            print("❌ Correo inválido")
            return
        
        print("\nTipo de cliente:")
        print("1. Regular")
        print("2. Premium")
        print("3. Corporativo")
        tipo = input("Seleccione (1-3): ")
        
        if tipo == "1":
            plan = input("¿Plan básico? (s/n): ").lower() == 's'
            cliente = ClienteRegular(rut, nombre, correo, plan)
        elif tipo == "2":
            membresia = input("Nivel de membresía: ")
            cliente = ClientePremium(rut, nombre, correo, membresia)
        elif tipo == "3":
            empresa = input("Nombre de la empresa: ")
            cliente = ClienteCorporativo(rut, nombre, correo, empresa)
        else:
            print("❌ Opción inválida")
            return
        
        self.lista_clientes.append(cliente)
        self.guardar_datos_csv()
        print(f"✅ Cliente {nombre} registrado exitosamente")
        registrar_log(f"INGRESO: Cliente {nombre} (RUT: {rut}) agregado")
    
    def modificar_cliente(self):
        """Modifica los datos de un cliente existente"""
        rut = input("Ingrese RUT del cliente a modificar: ")
        
        for cliente in self.lista_clientes:
            if cliente.rut == rut:
                print(f"\nCliente encontrado: {cliente}")
                cliente.nombre = input("Nuevo nombre (Enter para mantener): ") or cliente.nombre
                cliente.correo = input("Nuevo correo (Enter para mantener): ") or cliente.correo
                
                self.guardar_datos_csv()
                print("✅ Cliente modificado exitosamente")
                registrar_log(f"MODIFICACIÓN: Cliente RUT {rut} actualizado")
                return
        
        print("❌ Cliente no encontrado")
    
    def eliminar_cliente(self):
        """Elimina un cliente de la lista"""
        rut = input("Ingrese RUT del cliente a eliminar: ")
        
        for i, cliente in enumerate(self.lista_clientes):
            if cliente.rut == rut:
                confirmacion = input(f"¿Eliminar a {cliente.nombre}? (s/n): ")
                if confirmacion.lower() == 's':
                    self.lista_clientes.pop(i)
                    self.guardar_datos_csv()
                    print("✅ Cliente eliminado")
                    registrar_log(f"ELIMINACIÓN: Cliente RUT {rut} borrado")
                return
        
        print("❌ Cliente no encontrado")
    

    def visualizar_clientes(self):
        """Muestra todos los clientes o busca uno específico"""
        if not self.lista_clientes:
            print("\n📋 No hay clientes registrados")
            return
        
        print("\n--- VISUALIZACIÓN DE CLIENTES ---")
        print("1. Ver todos los clientes")
        print("2. Buscar cliente específico")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            self._mostrar_todos_clientes()
        elif opcion == "2":
            self._buscar_cliente_especifico()
        else:
            print("❌ Opción no válida")
    
    def _mostrar_todos_clientes(self):
        """Muestra la lista completa de clientes"""
        print("\n" + "="*80)
        print("LISTA COMPLETA DE CLIENTES")
        print("="*80)
        for i, cliente in enumerate(self.lista_clientes, 1):
            print(f"{i}. {cliente}")
        print("="*80)
        print(f"Total de clientes: {len(self.lista_clientes)}")
    
    def _buscar_cliente_especifico(self):
        """Busca un cliente por RUT o nombre"""
        print("\nBuscar por:")
        print("1. RUT")
        print("2. Nombre")
        criterio = input("Seleccione criterio de búsqueda: ")
        
        if criterio == "1":
            rut_buscar = input("Ingrese el RUT: ")
            encontrado = False
            for cliente in self.lista_clientes:
                if cliente.rut == rut_buscar:
                    print("\n" + "="*80)
                    print("CLIENTE ENCONTRADO")
                    print("="*80)
                    print(cliente)
                    print("="*80)
                    encontrado = True
                    registrar_log(f"BÚSQUEDA: Cliente RUT {rut_buscar} consultado")
                    break
            if not encontrado:
                print(f"❌ No se encontró cliente con RUT: {rut_buscar}")
        
        elif criterio == "2":
            nombre_buscar = input("Ingrese el nombre (o parte del nombre): ").lower()
            resultados = []
            for cliente in self.lista_clientes:
                if nombre_buscar in cliente.nombre.lower():
                    resultados.append(cliente)
            
            if resultados:
                print("\n" + "="*80)
                print(f"RESULTADOS DE BÚSQUEDA ({len(resultados)} encontrado(s))")
                print("="*80)
                for i, cliente in enumerate(resultados, 1):
                    print(f"{i}. {cliente}")
                print("="*80)
                registrar_log(f"BÚSQUEDA: Se encontraron {len(resultados)} clientes con '{nombre_buscar}'")
            else:
                print(f"❌ No se encontraron clientes con el nombre: {nombre_buscar}")
        else:
            print("❌ Criterio no válido")

