🚀 Sistema de Gestión de Clientes - SolutionTech

📋 Descripción del Proyecto
Sistema de gestión de clientes desarrollado en Python para SolutionTech, una startup de tecnología en crecimiento. El sistema permite administrar de manera eficiente tres tipos de clientes (Regular, Premium y Corporativo), implementando principios de Programación Orientada a Objetos (POO) y control de acceso basado en roles.

✨ Funcionalidades Principales
🔐 Sistema de Autenticación
✅ Login con usuario y contraseña
✅ Control de acceso basado en roles (Admin/Vendedor)
✅ Límite de intentos de login (3 intentos)
✅ Registro de actividad en log
👥 Gestión de Clientes
✅ Registro de clientes con tres categorías:
Cliente Regular: Plan básico o mejorado
Cliente Premium: Membresía especial con soporte 24/7
Cliente Corporativo: Empresas con descuentos exclusivos
✅ Modificación de datos de clientes existentes
✅ Eliminación de clientes (solo administradores)
✅ Visualización de clientes:
Ver listado completo
Búsqueda por RUT (exacta)
Búsqueda por nombre (parcial)
🛡️ Validaciones Implementadas
✅ Validación de formato de RUT chileno (XX.XXX.XXX-X)
✅ Validación de formato de correo electrónico
✅ Verificación de duplicados (RUT único)
✅ Control de permisos por rol de usuario
📊 Registro de Actividad
✅ Log automático de todas las operaciones
✅ Registro con timestamp de cada acción
✅ Trazabilidad de usuarios y operaciones
🛠️ Tecnologías Utilizadas
Lenguaje: Python 3.8+
Paradigma: Programación Orientada a Objetos (POO)
Persistencia de Datos: Archivos CSV
Registro de Actividad: Archivos TXT
Interfaz: Línea de comandos (CLI)
📁 Estructura del Proyecto

Gestion de clientes - SolutionTech/
│
├── main.py                          # Punto de entrada de la aplicación
│
├── modulos/                         # Paquete de módulos
│   ├── __init__.py                 # Inicializador del paquete
│   ├── menu.py                     # Interfaz de menús
│   ├── modelos.py                  # Clases de dominio (Usuario, Cliente)
│   ├── gestion_clientes.py         # Lógica de negocio
│   ├── funciones_utiles.py         # Funciones auxiliares
│   └── validaciones.py             # Validaciones de datos
│
├── clientes.csv                     # Base de datos de clientes
├── log_actividad.txt               # Registro de actividades
│
└── README.md                        # Este archivo


🚀 Instalación y Configuración
Requisitos Previos
Python 3.8 o superior instalado
Sistema operativo: Windows, Linux o macOS
Pasos de Instalación
Clonar o descargar el repositorio:

git clone <url-del-repositorio>cd "Gestion de clientes - SolutionTech"
Verificar la estructura de archivos:

# Asegurarse de que existe la carpeta modulos/# y todos los archivos .py necesarios
Ejecutar la aplicación:

python main.py
💻 Uso del Sistema
Credenciales de Acceso
Administrador
Usuario: admin
Contraseña: 1234
Permisos: Acceso completo (crear, modificar, eliminar, visualizar)
Vendedores
Usuario: venta1 | Contraseña: 5678
Usuario: vendedor | Contraseña: 1111
Permisos: Crear, modificar y visualizar (sin eliminación)
Menú Principal

==================================================
           MENÚ PRINCIPAL
==================================================
1. Ingresar Cliente
2. Modificar Cliente
3. Eliminar Cliente
4. Visualizar Clientes
5. Salir
==================================================

Flujo de Trabajo
1. Registrar un Cliente Regular

Opción: 1RUT (formato XX.XXX.XXX-X): 12.345.678-9Nombre completo: María GonzálezCorreo electrónico: maria@empresa.clTipo de cliente:1. Regular2. Premium3. CorporativoSeleccione (1-3): 1¿Plan básico? (s/n): s✅ Cliente María González registrado exitosamente

2. Buscar un Cliente Específico

Opción: 4--- VISUALIZACIÓN DE CLIENTES ---1. Ver todos los clientes2. Buscar cliente específicoSeleccione una opción: 2Buscar por:1. RUT2. NombreSeleccione criterio de búsqueda: 2Ingrese el nombre (o parte del nombre): juan

3. Modificar Datos de Cliente

Opción: 2Ingrese RUT del cliente a modificar: 12.345.678-9Cliente encontrado: RUT: 12.345.678-9 | Nombre: Juan Perez | ...Nuevo nombre (Enter para mantener): Juan Carlos PerezNuevo correo (Enter para mantener): juan.perez@mail.com✅ Cliente modificado exitosamente
📊 Formato de Archivos de Datos
clientes.csv

rut,nombre,correo,tipo_cliente,dato_especifico,beneficios12.345.678-9,Juan Perez,juan@mail.com,Regular,True,Plan Estándar98.765.432-1,Marta Gomez,marta@tech.com,Premium,Gestor VIP,Gestor VIP11.223.344-5,Empresa Alfa,contacto@alfa.cl,Corporativo,Alpha S.A.,Descuentos exclusivos
log_actividad.txt

[2026-02-17 15:26:11] SESIÓN: Usuario 'admin' ha ingresado al sistema.[2026-02-17 15:27:12] INGRESO: Cliente Juan (RUT: 12.345.678-9) agregado[2026-02-17 15:28:30] BÚSQUEDA: Cliente RUT 12.345.678-9 consultado[2026-02-17 15:30:45] SESIÓN: Usuario 'admin' cerró el sistema.

🏗️ Arquitectura del Sistema

Diagrama de Clases

Usuario
├── username: str (privado)
├── password: str (privado)
├── rol: str
├── verificar_password(intento: str): bool
├── es_admin(): bool
└── __str__(): str

Cliente (Clase Base)
├── rut: str
├── nombre: str
├── correo: str
├── tipo: str
└── __str__(): str

ClienteRegular (hereda de Cliente)
├── plan_basico: bool
├── mejorar_plan(): str
└── __str__(): str

ClientePremium (hereda de Cliente)
├── membresia: str
├── soporte_247: bool
├── gestor_cuenta_asignado: str
├── cambiar_gestor(nuevo_gestor: str): str
└── __str__(): str

ClienteCorporativo (hereda de Cliente)
├── razon_social: str
└── __str__(): str

GestionClientes
├── lista_clientes: list
├── cargar_clientes_desde_csv()
├── guardar_datos_csv()
├── existe_cliente(rut: str): bool
├── ingresar_cliente()
├── modificar_cliente()
├── eliminar_cliente()
└── visualizar_clientes()


🔍 Características Técnicas

Principios POO Implementados
Encapsulamiento

Atributos privados en clase Usuario (__username, __password)
Métodos de acceso controlado
Herencia

Clase base Cliente
Clases derivadas: ClienteRegular, ClientePremium, ClienteCorporativo
Polimorfismo

Método __str__() sobrescrito en cada clase
Comportamiento específico por tipo de cliente
Abstracción

Separación de responsabilidades en módulos
Interfaces claras entre componentes
Validaciones de Datos
Validación de RUT Chileno:


# Formato aceptado: XX.XXX.XXX-X# Ejemplo: 12.345.678-9# Incluye validación de dígito verificador
Validación de Correo Electrónico:


# Patrón: usuario@dominio.extension# Ejemplo: contacto@solutiontech.cl
Seguridad
✅ Contraseñas encapsuladas (atributos privados)
✅ Control de acceso por roles
✅ Límite de intentos de login
✅ Registro de intentos de acceso no autorizado
📈 Casos de Uso
Caso 1: Onboarding de Cliente Corporativo

1. Admin/Vendedor ingresa al sistema2. Selecciona "Ingresar Cliente"3. Completa datos (RUT, nombre, correo)4. Selecciona tipo "Corporativo"5. Ingresa razón social de la empresa6. Sistema valida y guarda el cliente7. Se genera registro en log
Caso 2: Búsqueda de Cliente para Soporte

1. Usuario ingresa al sistema2. Selecciona "Visualizar Clientes"3. Elige "Buscar cliente específico"4. Busca por RUT o nombre5. Sistema muestra información completa6. Se registra la consulta en log
Caso 3: Actualización de Datos

1. Admin/Vendedor busca cliente por RUT2. Selecciona "Modificar Cliente"3. Actualiza campos necesarios4. Sistema valida nuevos datos5. Guarda cambios en CSV6. Registra modificación en log
⚠️ Limitaciones Conocidas
❌ No incluye interfaz gráfica (GUI) en Tkinter o Flask
❌ No implementa integración con APIs externas
❌ No utiliza base de datos SQLite o archivos JSON
❌ No incluye pruebas unitarias automatizadas
❌ No implementa sistema de notificaciones automáticas
❌ Búsqueda sensible a mayúsculas/minúsculas en algunos casos
🔮 Mejoras Futuras Propuestas
Corto Plazo
 Agregar exportación de reportes a PDF
 Implementar historial de cambios por cliente
 Mejorar búsqueda con filtros avanzados
 Agregar validación de teléfonos
Mediano Plazo
 Migrar a base de datos SQLite
 Implementar sistema de backup automático
 Agregar dashboard de métricas
 Sistema de recordatorios/seguimiento
Largo Plazo
 Desarrollar API REST
 Integración con CRM externo
 Implementar machine learning para segmentación
 Aplicación web con Flask
🧪 Testing Manual
Checklist de Pruebas
Autenticación:

 Login exitoso con credenciales válidas
 Rechazo con credenciales inválidas
 Bloqueo después de 3 intentos fallidos
 Distinción entre roles Admin/Vendedor
Gestión de Clientes:

 Registro de cliente Regular
 Registro de cliente Premium
 Registro de cliente Corporativo
 Validación de RUT duplicado
 Validación de formato de RUT
 Validación de formato de correo
 Modificación de datos existentes
 Eliminación (solo Admin)
 Rechazo de eliminación (Vendedor)
Visualización:

 Listado completo de clientes
 Búsqueda por RUT exacto
 Búsqueda por nombre parcial
 Manejo de búsquedas sin resultados
Persistencia:

 Guardado correcto en CSV
 Carga correcta desde CSV
 Registro en log de actividades
 Formato correcto de timestamps
 
👥 Información del Desarrollador
Proyecto: Sistema de Gestión de Clientes - SolutionTech
Módulo: #4 - Aprendizaje Basado en Proyectos
Curso: Programación Avanzada en Python
Fecha: Febrero 2026


📄 Licencia
Este proyecto es de uso académico.
Todos los derechos reservados © 2026

Última actualización: 17 de Febrero, 2026
Versión: 1.0.0
Estado: ✅ Operativo

🎯 Objetivos de Aprendizaje Cumplidos
✅ Implementación de POO con herencia y polimorfismo
✅ Manejo de archivos CSV y TXT
✅ Validaciones de datos con expresiones regulares
✅ Control de acceso basado en roles
✅ Registro y trazabilidad de operaciones
✅ Arquitectura modular y escalable
✅ Manejo de excepciones y errores

¡Sistema listo para producción en SolutionTech! 🚀