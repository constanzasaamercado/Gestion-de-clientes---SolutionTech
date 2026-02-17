class Usuario:
    def __init__(self, username, password, rol):
        self.__username = username
        self.__password = password
        self.rol = rol

    def verificar_password(self, intento):
        return self.__password == intento
    
    def es_admin(self):
        """Verifica si el usuario es administrador"""
        return self.rol == "admin"
    
    def __str__(self):
        return f"Usuario: {self.__username} | Rol: {self.rol}"

class Cliente:
    def __init__(self, rut, nombre, correo, tipo):
        self.rut = rut
        self.nombre = nombre
        self.correo = correo
        self.tipo = tipo

    def __str__(self):
        return f"RUT: {self.rut} | Nombre: {self.nombre} | Correo: {self.correo} | Tipo: {self.tipo}"

class ClienteRegular(Cliente):
    def __init__(self, rut, nombre, correo, plan_basico=True):
        super().__init__(rut, nombre, correo, "Regular")
        self.plan_basico = plan_basico

    def mejorar_plan(self):
        """Mejora el plan a premium"""
        if self.plan_basico:
            self.plan_basico = False
            return "✅ Plan mejorado a Premium"
        return "ℹ️ Ya tiene el mejor plan"

    def __str__(self):
        base = super().__str__()
        return f"{base} | Plan: {'Básico' if self.plan_basico else 'Premium'}"

class ClientePremium(Cliente):
    def __init__(self, rut, nombre, correo, membresia):
        super().__init__(rut, nombre, correo, "Premium")
        self.membresia = membresia
        self.soporte_247 = True

    def cambiar_gestor(self, nuevo_gestor):
        """Cambia el gestor de cuenta asignado"""
        self.gestor_cuenta_asignado = nuevo_gestor
        return f"✅ Gestor cambiado a: {nuevo_gestor}"

    def __str__(self):
        return f"{super().__str__()} | Membresía: {self.membresia} | Soporte 24/7: {'Sí' if self.soporte_247 else 'No'}"

class ClienteCorporativo(Cliente):
    def __init__(self, rut, nombre, correo, empresa):
        super().__init__(rut, nombre, correo, "Corporativo")
        self.razon_social = empresa

    def __str__(self):
        return f"{super().__str__()} | Empresa: {self.razon_social}"