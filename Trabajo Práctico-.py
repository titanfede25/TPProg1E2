"""
-----------------------------------------------------------------------------------------------

Título: Entrega 1 del TP grupal
Fecha: Hecho para el 22/10/2025
Autor: Equipo 1. Federico Sznajderhaus, Benjamín Moyano, Samuel Franco Salazar, Galo Barus.

Descripción: Un club deportivo con actividades aranceladas necesita el desarrollo de una aplicación para informatizar la gestión de los pagos de los socios por cada deporte.

Pendientes: Respecto a los inputs que esperan enteros, tenemos pensado utilizar try y except en general (en el main) para que no se rompa el programa completo, en el marco de la entrega final.

******************

CARACTERISTICAS:

Es una aplicación en Python para la gestión de un club deportivo. Permite:

Administrar socios (alta, baja, modificación, listado).
Gestionar deportes (crear, modificar, eliminar, listar).
Registrar pagos y generar informes (pagos mensuales, resumen anual por deporte, ingresos, métodos de pago).
Incluye un menú interactivo para navegar entre las opciones.

Diccionarios:

socios: contiene datos de cada socio (activo, nombre, apellido, fecha, teléfonos).
deportes: contiene datos de cada deporte (activo, arancel, director, fechas de actividad).
pagos: contiene registros de pagos (idSocio, idDeporte, monto, fecha, método).
Diccionarios internos para teléfonos y fechas.

Listas:

Se usan para almacenar fechas en fechasActividad y para generar menús dinámicos.
También en informes (matrizInforme2, matrizInformes3).

Tuplas:

No hay tuplas explícitas en el código.

Conjuntos:

No hay Conjuntos explícitos en el código.

Hay más de 20 funciones, agrupadas en:

Gestión de socios: altaSocio, listarSocios, modificarSocio, bajaSocio.
Gestión de deportes: crearDeporte, listaDeDeportes, modificarDeporte, eliminarDeporte.
Gestión de pagos: registrarPago, eliminarPago.
Informes: matrizInformes1, matrizInforme2, matrizInformes3, matrizInforme4, rellenar.
main() como punto de entrada.

 Cualidades del código

Estructurado y modular: cada funcionalidad está en una función.
Uso de validaciones: controla entradas incorrectas (nombres, fechas, teléfonos).
Interfaz por consola: menús claros y submenús.
Persistencia en memoria: usa diccionarios en lugar de archivos o bases de datos.
Documentación interna: docstrings explicativos en cada función.
524 90 
**************
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import time
import json
import os


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def altaSocio(clientes, buscar):
    """
    Si el socio no existe lo agrega a la base de datos, si existe y no esta dado de alta, da la opcion de hacerlo.

    Parametros:
        clientes (dict)
        buscar (str)
    Devuelve:
        clientes (dict)
    """
    
    nombre = str(input("Nombre: "))
    while nombre.isalpha() == False:
        nombre = str(input("Error! Seleccione nuevo nombre: "))
    apellido = str(input("Apellido: "))
    while apellido.isalpha() == False:
        apellido = str(input("Error! Seleccione nuevo nombre: "))

    diaNacimiento = int(input("Dia de nacimiento: "))    
    if diaNacimiento < 1 or diaNacimiento > 31:
        print("Error, fecha invalida")
        return clientes

    mesNacimiento = int(input("Mes de nacimiento: "))
    if mesNacimiento < 1 or mesNacimiento > 12 or ((mesNacimiento == 4 or mesNacimiento == 6 or mesNacimiento == 9 or  mesNacimiento == 11) and diaNacimiento == 31):
        print("Error, fecha invalida")
        return clientes
    
    anioNacimiento = int(input("año de nacimiento: "))
    if (anioNacimiento < 1900 or anioNacimiento > 2025):
        print("Error, fecha invalida")
        return clientes
    
    anioBiciesto = (anioNacimiento % 4 == 0 and (anioNacimiento % 100 != 0 or anioNacimiento % 400 == 0))        
    if (not anioBiciesto and mesNacimiento == 2 and diaNacimiento > 29):
        print("Error, fecha invalida")
        return clientes
    
    if len(str(diaNacimiento)) == 1:
        diaNacimiento = "0" + str(diaNacimiento)
    if len(str(mesNacimiento)) == 1:
        mesNacimiento = "0" + str(mesNacimiento)
    fechaNacimiento = f"{str(diaNacimiento)}/{str(mesNacimiento)}/{str(anioNacimiento)}"

    clientes[buscar] = {"activo": True, "nombre": nombre, "apellido": apellido, "fechaNacimiento": fechaNacimiento, "telefonos": {} }

    numTelefonos = int(input("Cantidad de telefonos: ")) # Atributo multivaluado
    while numTelefonos < 1:
        numTelefonos = int(input("Error! Ingrese cantidad de telefonos de nuevo: "))  
    for i in range (numTelefonos):
        tel = int(input("Telefono " + str(i + 1) + ": "))
        while len(str(tel)) < 10 or len(str(tel)) > 13 or tel < 0:
            tel = int(input("Error! Ingrese Telefono " + str(i + 1) + " de nuevo: "))
        clientes[buscar]["telefonos"]["telefono" + str(i + 1)] = tel

    print("Socio agregado exitosamente")

    return clientes
    

def listarSocios(clientes):
    """
    Busca y lista todos los socios activos

    paramentros:
        clientes (dict)
        buscar (str)
    
    devuelve:
        n/a
    """
    for dni, cliente in clientes.items():
        if (clientes[dni]["activo"] == True):
            print("\nNombre:", cliente["nombre"])
            print("Apellido:", cliente["apellido"])
            print("Fecha de nacimiento:", cliente["fechaNacimiento"])
            telefonos = clientes[dni]["telefonos"]
            for k, telefono in telefonos.items():
                print(k + ":", telefono)
    
    return

def modificarSocio(clientes, buscar):
    """
    Modifica los atributos de un socio

    Parametros:
        clientes (dict)
        buscar (str)
    Devuelve:
        clientes (diccionario)
    """
   
    userInput = -1
    while (userInput != 0):
        print(buscar, ":")
        print(clientes[buscar])
        print("Que desea modificar?")
        print("---------------------------")
        print("[1] Modificar estado")
        print("[2] Modificar nombre")
        print("[3] Modificar apellido")
        print("[4] Modificar fecha de nacimiento")
        print("[5] Modificar telefonnos")
        print("---------------------------")
        print("[0] Volver al menú anterior")
        print("---------------------------")

        userInput = int(input("Seleccione una opción: "))

        print("")
        if (userInput == 0):
            break
        elif (userInput == 1):
            res = -1
            estadoSocio = clientes[buscar]["activo"]
            while (res != 1 and res != 0):
                print("Estado actual:", estadoSocio)
                if (estadoSocio == True):
                    res = int(input("Desea darlo de baja? [1 = si / 0 = No]: ")) 
                else:
                    res = int(input("Desea darlo de alta? [1 = si / 0 = No]: "))
                if (res == 1 and estadoSocio == True):
                        clientes[buscar]["activo"] = False
                        print("Socio dado de baja exitosamente.\n")
                elif (res == 1 and estadoSocio == False):
                        clientes[buscar]["activo"] = True
                        print("Socio dado de alta exitosamente.\n")
                elif (res == 0):
                    print("No se hicieron cambios\n")
                else:
                    print("Error, input invalido\n")       

        elif (userInput == 2):
            print("Nombre actual: ", clientes[buscar]["nombre"])
            cambiar = str(input("Nuevo nombre: "))
            while cambiar.isalpha() == False:
                cambiar = str(input("Error! Seleccione nuevo nombre: "))
            clientes[buscar]["nombre"] = cambiar
            print("Nombre cambiado existosamente")

        elif (userInput == 3):
            print("Apellido actual: ", clientes[buscar]["apellido"])
            cambiar = str(input("Nuevo apellido: "))
            while cambiar.isalpha() == False:
                cambiar = str(input("Error! Seleccione nuevo apellido: "))
            clientes[buscar]["apellido"] = cambiar
            print("Apellido cambiado existosamente")

        elif (userInput == 4):
            print("Fecha de nacimiento actual: ", clientes[buscar]["fechaNacimiento"])
            diaNacimiento = int(input("Dia de nacimiento: "))
            if diaNacimiento < 1 or diaNacimiento > 31:
                print("Error, fecha invalida")
                return clientes
            mesNacimiento = int(input("Mes de nacimiento: "))
            if mesNacimiento < 1 or mesNacimiento > 12 or ((mesNacimiento == 4 or mesNacimiento == 6 or mesNacimiento == 9 or  mesNacimiento == 11) and diaNacimiento == 31):
                print("Error, fecha invalida")
                return clientes
            anioNacimiento = int(input("año de nacimiento: "))
            if (anioNacimiento < 1900 or anioNacimiento > 2025):
                print("Error, fecha invalida")
                return clientes
            anioBiciesto = (anioNacimiento % 4 == 0 and (anioNacimiento % 100 != 0 or anioNacimiento % 400 == 0))        
            if (not anioBiciesto and mesNacimiento == 2 and diaNacimiento > 29):
                print("Error, fecha invalida")
                return clientes
            if len(str(diaNacimiento)) == 1:
                diaNacimiento = "0" + str(diaNacimiento)
            if len(str(mesNacimiento)) == 1:
                mesNacimiento = "0" + str(mesNacimiento)
            fechaNacimiento = f"{str(diaNacimiento)}/{str(mesNacimiento)}/{str(anioNacimiento)}"
            clientes[buscar]["fechaNacimiento"] = fechaNacimiento
            print("Fecha de nacimiento cambiada existosamente")

        elif (userInput == 5):
            print("Actual cant de telefonos: ", len(clientes[buscar]["telefonos"])) # Atributo multivaluado
            numTelefonos = int(input("Cantidad de telefonos: "))
            while numTelefonos < 1:
                numTelefonos = int(input("Error! Ingrese cantidad de telefonos de nuevo: "))  
            for i in range (numTelefonos):
                tel = int(input("Telefono " + str( i+ 1) + ": "))
                while len(str(tel)) < 10 or len(str(tel)) > 13 or tel < 0:
                    tel = int(input("Error! Ingrese Telefono " + str(i + 1) + " de nuevo: "))
                clientes[buscar]["telefonos"]["telefono"+str(i + 1)] = tel

    return clientes

def bajaSocio(clientes, pagos, buscar): 
    """
    Dar de baja logicamente a un socio

    Parametros:
        clientes (dict)
        buscar (str)
        pagos (dict)
    
    Devuelve:
        clientes (diccionario)
    """
    if (not clientes[buscar]["activo"]):
        print("Cliente ya inactivo")
        return clientes

    print(f"\nLista de pagos de {clientes[buscar]["nombre"]} {clientes[buscar]["apellido"]}:")

    for k, v in pagos.items():
        if (v["idSocio"] == buscar):
            print(k, v)

    res = -1
    while (res < 0 or res > 1):
        res = int(input("\nDesea dar de baja al socio? [1 = Si / 0 = No]: "))
        if (res == 1):
            clientes[buscar]["activo"] = False
            print("Cliente dado de baja existosamente.")
        elif (res == 0):
            print("No pasó nada.")
        else:
            print("Input invalido.")

    return clientes


#----------------------------------------------------------------------------------------------
# FUNCIONES DE DEPORTES
#----------------------------------------------------------------------------------------------
def crearDeporte(deportes, busqueda):
    """
    Se crea o reactiva un deporte (también guarda su fecha)

    Parámetros:
        deportes (dict)
        busqueda (str)
    Devuelve:
        deportes (dict)
    """
    if busqueda in deportes.keys():
        print("Advertencia, este deporte ya existe.")
        if deportes[busqueda]["activo"] == False:
            res = -1
            while res not in [0, 1]:
                res = int(input("El deporte está dado de baja. ¿Desea darlo de alta? [1 = Sí / 0 = No]: "))
                if res == 1:
                    deportes[busqueda]["activo"] = True
                    n = 1 + len(deportes[busqueda]["fechasActividad"])
                    deportes[busqueda]["fechasActividad"][f"fecha{n}"] = [time.strftime("%d/%m/%Y")] # Atributo multivaluado
                elif res == 0:
                    print("El deporte se mantiene inactivo.")
    else:
        arancel = float(input("Arancel: "))
        while arancel < 0:
            arancel = float(input("Error! Ingrese arancel de nuevo: "))
        director = str(input("Nombre del director principal: "))
        fecha_creacion = time.strftime("%d/%m/%Y")

        print("\nDatos ingresados:")
        print("Deporte:", busqueda)
        print("Arancel:", arancel)
        print("Director:", director)
        print("Fecha de creación:", fecha_creacion)

       
        res = -1
        while res not in [0, 1]:
            res = int(input("¿Los datos son correctos? [1 = Sí / 0 = No]: "))
            if res == 1:
                deportes[busqueda] = {
                    "activo": True,
                    "arancel": arancel,
                    "director principal": director,
                    "fechasActividad": {
                        "fecha1": [fecha_creacion]
                    }
                }
                print("Deporte creado exitosamente.")
            elif res == 0:
                print("Operación cancelada.")
    return deportes


def listaDeDeportes(deportes):
    """
    Muestra todos los deportes activos (sin fecha de cierre).

    Parámetros:
        deportes (dict)
    Devuelve:
        n/a
    """
    activos = False
    print("\nDeportes activos:")
    for clave, datos in deportes.items():
        if datos["activo"] == True:
            activos = True
            print("---------------------------")
            print("Deporte:", clave)
            print("Arancel:", datos["arancel"])
            print("Director principal:", datos["director principal"])
            print("Fechas de actividad: ", datos["fechasActividad"])
    if activos == False:
        print("No hay deportes activos registrados.")
    else:
        print("---------------------------")
    
    return


def modificarDeporte(deportes):
    """
    Se modifica el deporte.

    Parámetros:
        deportes (dict)

    Returns:
        deportes (dict)
    """
    keys = list(deportes.keys())
    for i in range(len(keys)): 
        print (f"[{i+1}] {keys[i]}")
    eleccion = int(input("Seleccione el número del deporte que desea modificar: "))                                                
    while eleccion < 1 or eleccion > len(keys):
        eleccion = int(input("Error seleccionar un numero apropiado: "))
    deporteSeleccionado = keys[eleccion - 1]

    userInput = -1                   
    while userInput != 0:
        print(deporteSeleccionado, ":")
        print(deportes[deporteSeleccionado]) 
        print("¿Qué desea modificar?")
        print("---------------------------")
        print("[1] Modificar arancel")
        print("[2] Modificar director principal")
        print("---------------------------")
        print("[0] Volver al menú anterior")
        print("---------------------------")

        userInput = int(input("Seleccione una opción: "))
        print("")

        if userInput == 0:
            print("Volviendo al menú anterior...\n")

        elif userInput == 1:
            print("Arancel actual:", deportes[deporteSeleccionado]["arancel"])
            cambiar = float(input("Nueva tarifa: "))
            while cambiar < 0:
                cambiar = float(input("Error! Ingrese arancel de nuevo: "))
            res = -1
            while res not in [0, 1]:
                res = int(input(f"¿Desea guardar el nuevo arancel {cambiar}? [1 = Sí / 0 = No]: "))
                if res == 1:
                    deportes[deporteSeleccionado]["arancel"] = cambiar
                    print("Tarifa modificada exitosamente\n")
                elif res == 0:
                    print("Modificación cancelada\n")

        elif userInput == 2:
            print("Profesor actual:", deportes[deporteSeleccionado]["director principal"])
            cambiar = str(input("Nuevo director principal: "))
            res = -1
            while res not in [0, 1]:
                res = int(input(f"¿Desea guardar el nuevo director principal {cambiar}? [1 = Sí / 0 = No]: "))
                if res == 1:
                    deportes[deporteSeleccionado]["director principal"] = cambiar
                    print("Tarifa modificada exitosamente\n")
                elif res == 0:
                    print("Modificación cancelada\n")

    return deportes



def eliminarDeporte(deportes):
    """
    Da de baja un deporte activo y registra la fecha de cierre.

    Parámetros:
        deportes (dict)

    Returns:
        deportes (dict)
    """
    keys = [k for k, v in deportes.items() if v["activo"] == True]

    if not keys:
        print("No hay deportes activos para dar de baja.")
        return deportes

    print("\nDeportes activos:")
    for i in range(len(keys)): 
        print(f"[{i+1}] {keys[i]}")

    eleccion = int(input("Seleccione el número del deporte que desea dar de baja: "))
    while eleccion < 1 or eleccion > len(keys):
        eleccion = int(input("Error: seleccione un número válido: "))
    
    deporteSeleccionado = keys[eleccion - 1]

    res = -1
    while res not in [0, 1]:
        res = int(input(f"¿Desea dar de baja {deporteSeleccionado}? [1 = Sí / 0 = No]: "))
        if res == 1:
            deportes[deporteSeleccionado]["activo"] = False
            n = len(deportes[deporteSeleccionado]["fechasActividad"])
            deportes[deporteSeleccionado]["fechasActividad"][f"fechas{n}"].append(time.strftime("%d/%m/%Y")) # Append a atributo multivaluado
            print(f"Deporte '{deporteSeleccionado}' dado de baja exitosamente.\n")
        elif res == 0:
            print("Baja cancelada.\n")
    return deportes

#----------------------------------------------------------------------------------------------
# FUNCIONES DE PAGOS
#----------------------------------------------------------------------------------------------
def registrarPago(pagos, socios, deportes):
    """
    Registra un nuevo pago hecho por un socio.

    Parametros:
        pagos (dict)
        socios (dict)
        deportes (dict)

    Devuelve
        pagos (dict)
    """
    anioActual = int(time.strftime("%Y"))
    mesActual = int(time.strftime("%m"))
    dni = str(input("Ingrese DNI del socio: "))

    # Verificar si el socio existe y está activo
    if dni not in socios.keys():
        print("Error: el socio no existe.")
        return pagos
    if not socios[dni]["activo"]:
        print("Error: el socio está dado de baja.")
        return pagos

    keysDeportes = list(deportes.keys())
    for i in range(len(keysDeportes)): 
        print (f"[{i+1}] {keysDeportes[i]}")
    eleccion = int(input("Seleccione el número del deporte: "))
    while eleccion < 1 or eleccion > len(keysDeportes):
        eleccion = int(input("Error seleccionar un numero apropiado: "))
    deporteSeleccionado = keysDeportes[eleccion - 1]

    mes = 13
    anio = anioActual
    while (mes > mesActual and anio == anioActual):
        mes = -1
        while (mes < 1 or mes > 12):  
            mes = int(input("\nIngrese el mes del pago (ej: 10 para octubre): "))  
        anio = 9999
        while (anio < 1900 or anio > anioActual):
            anio = int(input("\nIngrese el año del pago: "))
        if (mes > mesActual and anio == anioActual):
            print("\nError, fecha invalida.")
    
    keysPagos = list(pagos.keys())
    for i in range(len(keysPagos)):
        if pagos[keysPagos[i]]["mes"] == mes and pagos[keysPagos[i]]["ano"] == anio and dni == pagos[keysPagos[i]]["idSocio"] and deporteSeleccionado == pagos[keysPagos[i]]["idDeporte"]:
            print("Pago invalido, pago ya efectuado.")
            return pagos
    
    activoEnFecha = False # Verificación de si el deporte estaba activo en el mes/año del pago
    for periodo in deportes[deporteSeleccionado]["fechasActividad"].values():
        diaI, mesI, anioI = periodo[0].split("/")
        anioI = int(anioI)
        mesI = int(mesI)

        if len(periodo) == 2:
            diaF, mesF, anioF = periodo[1].split("/")
            anioF = int(anioF)
            mesF = int(mesF)
        else:
            anioF = int(time.strftime("%Y"))
            mesF = int(time.strftime("%m"))
        
        if (anio > anioI or (anio == anioI and mes >= mesI)) and (anio < anioF or (anio == anioF and mes <= mesF)):
            activoEnFecha = True
    if not activoEnFecha:
        print(f"Error: el deporte seleccionado no estaba activo en esa fecha")
        return pagos


    
    opcionDePago = -1
    while (opcionDePago < 1 or opcionDePago > 3):
        print("\nSeleccione el medio de pago:")
        print("[1] Efectivo")
        print("[2] Tarjeta")
        print("[3] Transferencia")
        opcionDePago = int(input(("\nOpcion elegida:")))

    if (opcionDePago == 1):
        metodoDePago = "efectivo"
    elif (opcionDePago == 2):
        metodoDePago = "tarjeta"
    else:
        metodoDePago = "transferencia"


    monto = deportes[deporteSeleccionado]["arancel"]
    if (mesActual > mes and anioActual == anio) or (anioActual > anio):
        monto *= 1.2 # 20% de recargo en caso de que sea un pago atrasado
        print(f"Usted debe pagar {monto} que está un 20% aumentado, debido a que está atrasado. Aceptas el pago? [1 = si / 0 = No]")
    else:
        print(f"Usted debe pagar {monto}. Aceptas el pago? [1 = si / 0 = No]")
    res = -1
    while (res < 0 or res > 1):
        res = int(input(""))
        if (res == 1):
            id_pago = f"{anioActual}.{mesActual}.{time.strftime("%d")} {time.strftime("%H")}:{time.strftime("%M")}:{time.strftime("%S")}"

            pagos[id_pago] = {
                "idSocio": dni,
                "idDeporte": deporteSeleccionado,
                "estadoDePago": "pagado",
                "monto": monto,
                "ano": anio,
                "mes": mes,
                "metodoDePago": metodoDePago
            }
            

            print(f"\nPago registrado con éxito por ${monto} para {socios[dni]['nombre']} {socios[dni]['apellido']} ({deporteSeleccionado}).")
            print(pagos)

            return pagos

        elif (res == 0):
            print("No se realizo el pago.")
            return pagos
        else:
            print("Error, opcion invalida. Ingrese de nuevo.")



    return pagos

def eliminarPago(pagos, socios):
    """
    Elimina un pago

    Parámetros:
        pagos (dict)
        socios (dict)

    Devuelve:
        pagos (dict)
    """
    dni = str(input("Ingrese DNI del socio: "))
    if dni not in socios.keys():
        print("Error: el socio no existe.")
        return pagos
    
    listaKeysPagos = list(pagos.keys())
    listaDeportesPorSocio = []
    for key in listaKeysPagos:
        if pagos[key]["idSocio"] == dni and pagos[key]["idDeporte"] not in listaDeportesPorSocio:
            listaDeportesPorSocio.append(pagos[key]["idDeporte"])

    if not listaDeportesPorSocio:
        print("El socio no tiene pagos registrados.")
        return pagos

    for i, dep in enumerate(listaDeportesPorSocio):
        print(f"[{i+1}] {dep}")
    eleccion = int(input("Seleccione el número de deporte del pago: "))
    while eleccion < 1 or eleccion > len(listaDeportesPorSocio):
        eleccion = int(input("Error! Seleccionar un número apropiado: "))
    deporteSeleccionado = listaDeportesPorSocio[eleccion - 1]

    pagosFiltrados = []
    contador = 0
    for key in listaKeysPagos:
        if pagos[key]["idSocio"] == dni and pagos[key]["idDeporte"] == deporteSeleccionado:
            contador += 1
            pagosFiltrados.append(key)
            print(f"[{contador}] {pagos[key]}")

    if not pagosFiltrados:
        print("No hay pagos para este deporte.")
        return pagos

    eleccion = int(input("Seleccione el número de pago: "))
    while eleccion < 1 or eleccion > len(pagosFiltrados):
        eleccion = int(input("Error! Seleccionar un número apropiado: "))

    keySeleccionada = pagosFiltrados[eleccion - 1]
    print("\nEste es el pago seleccionado:")
    print(pagos[keySeleccionada])

    print("ALERTA: Si confirmas, se eliminará permanentemente.")
    confirmar = int(input("¿Quieres eliminar el pago? [1 = Sí / 0 = No]: "))
    if confirmar == 1:
        del pagos[keySeleccionada]
        print("Pago eliminado exitosamente.")
    else:
        print("Operación cancelada.")

    return pagos

    
#----------------------------------------------------------------------------------------------
# FUNCIONES DE INFORMES
#----------------------------------------------------------------------------------------------
def matrizInformes1(pagos, socios, mesObjetivo, anoObjetivo):
    """
    Muestra una lista detallada de todos los pagos realizados del mes actual.

    Parámetros:
        pagos (dict)
        socios (dict)
        mesObjetivo (int): El mes para el cual se desea el informe.
        anoObjetivo (int): El año para el cual se desea el informe.

    Devuelve:
        n/a
    """

    def rellenar(texto, ancho, alineacion):
        texto = str(texto)
        largo = len(texto)
        if largo >= ancho:
            return texto[:ancho]
        espacios = ancho - largo
        if alineacion == "izquierda":
            return texto + " " * espacios
        else:
            return " " * espacios + texto

    
    anchoFecha = 21
    anchoCliente = 25
    anchoDeporte = 15
    anchoMonto = 10

    
    encabezado = rellenar("Fecha/Hora", anchoFecha, "izquierda") + " | " + \
                 rellenar("Cliente", anchoCliente, "izquierda") + " | " + \
                 rellenar("Deporte", anchoDeporte, "izquierda") + " | " + \
                 rellenar("Monto", anchoMonto, "derecha")
    print(encabezado)
    print("-" * len(encabezado))

    
    for fechaHora in pagos:
        registro = pagos[fechaHora]
        if "idSocio" in registro and "mes" in registro and "ano" in registro and "monto" in registro and "idDeporte" in registro:
            if registro["mes"] == mesObjetivo and registro["ano"] == anoObjetivo:
                idSocio = registro["idSocio"]
                monto = registro["monto"]
                deporte = registro["idDeporte"]

                if idSocio in socios:
                    nombre = socios[idSocio]["nombre"]
                    apellido = socios[idSocio]["apellido"]
                    cliente = nombre + " " + apellido

                    linea = rellenar(fechaHora, anchoFecha, "izquierda") + " | " + \
                            rellenar(cliente, anchoCliente, "izquierda") + " | " + \
                            rellenar(deporte, anchoDeporte, "izquierda") + " | " + \
                            rellenar(f"${monto:.2f}", anchoMonto, "derecha")
                    print(linea)

def matrizInforme2(pagos, anoObjetivo):
    """
    Genera una matriz que resume la cantidad de pagos realizados por cada deporte durante cada mes de un año específico.

    Parámetros:
        pagos (dict)
        anoObjetivo (int)

    Devuelve:
        matriz (dict)
    """
    matriz = {}

    for fechaHora in pagos:
        registro = pagos[fechaHora]

        if "ano" in registro and "mes" in registro and "idDeporte" in registro:
            ano = registro["ano"]
            mes = registro["mes"]
            deporte = registro["idDeporte"]

            if ano == anoObjetivo:
                if deporte not in matriz:
                    matriz[deporte] = [0] * 12
                matriz[deporte][mes - 1] += 1

    return matriz


def rellenar(texto, ancho, alineacion):
    """
    Función auxiliar para formatear texto y asegurar un ancho fijo, útil para tablas. Recorta el texto si es más largo que el ancho y rellena con espacios si es más corto.

    Parámetros:
        texto (any): El valor a formatear y rellenar (se convierte a str).
        ancho (int): El ancho total deseado para la cadena de texto.
        alineacion (str): "izquierda" para alinear a la izquierda (rellena a la derecha) o cualquier otra cosa para alinear a la derecha (rellena a la izquierda).

    Devuelve:
        str: La cadena de texto formateada con el ancho y alineación especificados.
    """
    texto = str(texto)
    largo = len(texto)
    if largo >= ancho:
        return texto[:ancho]
    espacios = ancho - largo
    if alineacion == "izquierda":
        return texto + " " * espacios
    else:
        return " " * espacios + texto

def matrizInformes3(pagos, anoObjetivo):
    """
    Genera y muestra una matriz que resume la suma total de montos de pagos (ingresos) por cada deporte, distribuidos por mes para un año específico. También calcula y muestra el total general recaudado en el año.

    Parámetros:
        pagos (dict)
        anoObjetivo (int): El año para el cual se desea el informe de ingresos.

    Devuelve:
        n/a
    """
    matriz = {}
    totalGeneral = 0  

    
    for fechaHora in pagos:
        registro = pagos[fechaHora]
        if "ano" in registro and "mes" in registro and "idDeporte" in registro and "monto" in registro:
            ano = registro["ano"]
            mes = registro["mes"]
            deporte = registro["idDeporte"]
            monto = registro["monto"]

            if ano == anoObjetivo:
                if deporte not in matriz:
                    matriz[deporte] = [0] * 12
                matriz[deporte][mes - 1] += monto
                totalGeneral += monto

    anchoDeporte = 16
    anchoMes = 6
    anchoTotal = 8
    meses = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]

    encabezado = rellenar("Deporte", anchoDeporte, "izquierda") + " | " + \
                 " | ".join(rellenar(m, anchoMes, "derecha") for m in meses) + " | " + \
                 rellenar("TOTAL", anchoTotal, "derecha")
    print(encabezado)
    print("-" * len(encabezado))

    for deporte in matriz:
        fila = matriz[deporte]
        total = sum(fila)
        linea = rellenar(deporte, anchoDeporte, "izquierda") + " | " + \
                " | ".join(rellenar(int(valor), anchoMes, "derecha") for valor in fila) + " | " + \
                rellenar(int(total), anchoTotal, "derecha")
        print(linea)

    
    print("-" * len(encabezado))
    print(rellenar("TOTAL GENERAL", anchoDeporte + 13 * (anchoMes + 3) - 3, "derecha") + \
          rellenar(int(totalGeneral), anchoTotal, "derecha"))

def matrizInforme4(pagos, anioObjetivo):
    """
    Calcula un resumen de la cantidad de pagos y el porcentaje de pagos por cada método de pago ('efectivo', 'tarjeta', 'transferencia') para un año específico.

    Parámetros:
        pagos (dict)
        anioObjetivo (int): El año para el cual se desea el informe.

    Devuelve:
        list: Una lista de diccionarios, donde cada diccionario contiene:
            - "metodoDePago" (str)
            - "cantidad" (int)
            - "porcentaje" (float)
    """
    resumen = {}
    totalPagos = 0

    for registro in pagos.values():
        if registro.get("ano") == anioObjetivo and registro.get("estadoDePago") == "pagado":
            metodo = registro.get("metodoDePago", "desconocido")
            resumen[metodo] = resumen.get(metodo, 0) + 1
            totalPagos += 1

    informe = []
    for metodo, cantidad in resumen.items():
        porcentaje = (cantidad / totalPagos) * 100 if totalPagos > 0 else 0
        informe.append({
            "metodoDePago": metodo,
            "cantidad": cantidad,
            "porcentaje": round(porcentaje, 2)
        })

    return informe

#----------------------------------------------------------------------------------------------
# FUNCION DE ARCHIVOS / SOCIOS
#----------------------------------------------------------------------------------------------

def guardarSocios(socios):
    f = open("socios.json", "w", encoding="utf-8")  # Abrimos en modo escritura
    json.dump(socios, f, indent=4)  # Guardamos el diccionario en formato JSON
    f.close()  # Cerramos el archivo

def leerSocios():
    socios = {}
    try:
        f = open("socios.json", "r", encoding="utf-8")  # Abrimos en modo lectura
        socios = json.load(f)  # Cargamos el contenido como diccionario
        f.close()
    except FileNotFoundError:
        print("Archivo 'socios.json' no encontrado. Creando archivo vacío...")
        f = open("socios.json", "w", encoding="utf-8")
        json.dump({}, f)  # Guardamos un diccionario vacío
        f.close()
    return socios

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    #-------------------------------------------------
    # Inicialización de variables
    #----------------------------------------------------------------------------------------------
    socios = leerSocios()
    #-------------------------------------------------
    # Bloque de menú
    #----------------------------------------------------------------------------------------------
    while True:
        while True:
            opciones = 4
            print()
            print("---------------------------")
            print("MENÚ PRINCIPAL")
            print("---------------------------")
            print("[1] Gestión de socios")
            print("[2] Gestión de deportes")
            print("[3] Gestión de pagos")
            print("[4] Informes")
            print("---------------------------")
            print("[0] Salir del programa")
            print("---------------------------")
            print()
            
            opcionSubmenu = ""
            opcionMenuPrincipal = input("Seleccione una opción: ")
            if opcionMenuPrincipal in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcionMenuPrincipal == "0": # Opción salir del programa
            exit() # También puede ser sys.exit() para lo cual hay que importar el módulo sys

        elif opcionMenuPrincipal == "1":   # Opción 1 del menú principal
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE SOCIOS")
                    print("---------------------------")
                    print("[1] Ingresar socio")
                    print("[2] listar socios activos")
                    print("[3] Modificar socio")
                    print("[4] Eliminar socio")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior


                if (opcionSubmenu == "1" or opcionSubmenu == "3" or opcionSubmenu == "4"):
                    dniBuscar = input("Ingresar dni: ")
                    while dniBuscar.isdigit() == False:
                        dniBuscar = input("Ingresar dni válido: ")

                if opcionSubmenu == "1":   # Alta socio
                    if (dniBuscar in socios.keys()):
                        print("Error, el socio ya existe.\n")
                        print(socios[dniBuscar])
                    else:
                        socios = altaSocio(socios, dniBuscar)
                        guardarSocios(socios)  # Guardar cambios
                        print("Guardando archivo en:", os.getcwd())

                elif opcionSubmenu == "2":   # Listar socios
                    listarSocios(socios)

                elif opcionSubmenu == "3":   # Modificar socio
                    if (dniBuscar not in socios.keys()):
                        print("Error, el socio no existe.\n")
                    else:
                        socios = modificarSocio(socios, dniBuscar)
                        guardarSocios(socios)  # Guardar cambios

                elif opcionSubmenu == "4":   # Baja socio
                    socios = bajaSocio(socios, pagos, dniBuscar)
                    guardarSocios(socios)  # Guardar cambios

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")

        elif opcionMenuPrincipal == "2":   # Opción 2 del menú principal
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE DEPORTES")
                    print("---------------------------")
                    print("[1] Ingresar deporte")
                    print("[2] Listar deportes")
                    print("[3] Modificar deporte")
                    print("[4] Eliminar deporte")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()


                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    deporte = str(input("Ingresar deporte: ").lower())
                    deportes = crearDeporte(deportes, deporte)
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    listaDeDeportes(deportes)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    deportes = modificarDeporte(deportes)
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    deportes = eliminarDeporte(deportes)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")


        
        elif opcionMenuPrincipal == "3":   # Opción 3 del menú principal
            while True:
                while True:
                    opciones = 2
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE PAGOS")
                    print("---------------------------")
                    print("[1] Ingresar pago")
                    print("[2] Eliminar pago")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    pagos = registrarPago(pagos, socios, deportes)
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    pagos = eliminarPago(pagos, socios)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")


           
        elif opcionMenuPrincipal == "4":   # Opción 4 del menú principal
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE INFORMES")
                    print("---------------------------")
                    print("[1] Pagos del mes")
                    print("[2] Resumen Anual de cantidad de pagos por deporte")
                    print("[3] Resumen Anual de Pagos  (Montos cobrados, deudas, descuentos)")
                    print("[4] Resumen Anual de Métodos de Pago")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    mes = int(time.strftime("%m"))
                    ano = int(time.strftime("%Y"))
   

                    matrizInformes1(pagos, socios, mes, ano)

                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    
                    anoIngresado = int(input("Ingrese el año para el informe (ej: 2023): "))
                    while anoIngresado < 1900 or anoIngresado > int(time.strftime("%Y")):
                        anoIngresado = int(input("Año inválido. Ingrese un año válido: "))
                        
                    matriz = matrizInforme2(pagos, anoIngresado)

    
                    anchoDeporte = 20
                    anchoMes = 4
                    meses = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]

              
                    encabezado = rellenar("Deporte", anchoDeporte, "izquierda") + " | " + " | ".join(rellenar(m, anchoMes, "derecha") for m in meses)
                    print(encabezado)
                    print("-" * len(encabezado))

         
                    for deporte in matriz:
                        fila = matriz[deporte]
                        linea = rellenar(deporte, anchoDeporte, "izquierda") + " | " + " | ".join(rellenar(valor, anchoMes, "derecha") for valor in fila)
                        print(linea)

                elif opcionSubmenu == "3":   # Opción 3 del submenú
                
                    anoIngresado = int(input("Ingrese el año para el informe (ej: 2023): "))
                    while anoIngresado < 1900 or anoIngresado > int(time.strftime("%Y")):
                        anoIngresado = int(input("Año inválido. Ingrese un año válido: "))
                    matrizInformes3(pagos, anoIngresado)

                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    anoIngresado = int(input("Ingrese el año para el informe (ej: 2023): "))
                    while anoIngresado < 1900 or anoIngresado > int(time.strftime("%Y")):
                        anoIngresado = int(input("Año inválido. Ingrese un año válido: "))
                    print(f"\nResumen de métodos de pago para el año {anoIngresado}")
                    print("Método de Pago     | Cantidad | Porcentaje")
                    print("-------------------|----------|-----------")
                    grupo = matrizInforme4(pagos, anoIngresado)
                    for fila in grupo:
                        print(f"{fila['metodoDePago']:<19}| {fila['cantidad']:^8} | {fila['porcentaje']:>9.2f}%")

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")
                
        if opcionSubmenu != "0": # Pausa entre opciones. No la realiza si se vuelve de un submenú
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")


# Punto de entrada al programa
main()
