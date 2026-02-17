import csv
from datetime import datetime
from modulos.validaciones import validar_correo, validar_rut
from modulos.modelos import Cliente  # Asegúrate de tener esta clase en modelos.py

def registrar_log(mensaje):
    """Guarda la actividad en log_actividad.txt con timestamp."""
    try:
        with open("log_actividad.txt", "a", encoding="utf-8") as archivo:
            ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            archivo.write(f"[{ahora}] {mensaje}\n")
    except Exception as e:
        print(f"Error crítico al escribir log: {e}")

def ingresar_cliente_csv(cliente_obj):
    """
    Recibe un objeto Cliente (o sus subclases), lo valida 
    y lo guarda en el archivo CSV.
    """
    # 1. Validaciones previas (Integridad de datos)
    if not validar_correo(cliente_obj.correo):
        registrar_log(f"ERROR: Intento de ingreso con correo inválido: {cliente_obj.correo}")
        return False, "Correo electrónico no válido."

    try:
        # 2. Guardar en CSV (Persistencia)
        with open("clientes.csv", "a", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([
                cliente_obj.rut, 
                cliente_obj.nombre, 
                cliente_obj.correo, 
                cliente_obj.tipo
            ])
        
        # 3. Registrar en Log (Seguridad)
        registrar_log(f"INGRESO: Cliente {cliente_obj.nombre} (RUT: {cliente_obj.rut}) guardado con éxito.")
        return True, "Cliente ingresado correctamente."

    except PermissionError:
        return False, "Error: El archivo clientes.csv está abierto en otro programa."
    except Exception as e:
        return False, f"Error inesperado: {e}"
    
def obtener_todos_los_clientes():
    clientes = []
    try:
        with open("clientes.csv", "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                clientes.append(fila)
    except FileNotFoundError:
        pass
    return clientes

def existe_rut(rut_buscar):
    clientes = obtener_todos_los_clientes()
    for c in clientes:
        if c['rut'] == rut_buscar:
            return True
    return False