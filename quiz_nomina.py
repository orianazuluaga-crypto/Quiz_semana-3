import pandas as pd
# 1) CLASE BASE (PADRE): datos comunes + ENCAPSULAMIENTO del salario
class EmpleadoBase:
    """Clase base: encapsula el salario y define el comportamiento comun."""

    def __init__(self, nombre, salario_base, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad
        self.salario_base = salario_base
        # TODO: guarda el salario usando el SETTER -> self.salario_base = salario_base
       

    # GETTER: leer el salario de forma segura
    @property
    def salario_base(self):
        # TODO: devuelve el atributo privado self._salario_base
        return self._salario_base

    # SETTER: valida ANTES de guardar
    @salario_base.setter
    def salario_base(self, nuevo_salario):
        valor = int (nuevo_salario)
        if valor < 0:
         raise ValueError("el valor del salario no puede ser negativo")
        self._salario_base = valor
        # TODO: si int(nuevo_salario) < 0  ->  raise ValueError("El salario no puede ser negativo.")
        #       si es valido, guardalo:  self._salario_base = int(nuevo_salario)
       

    # Metodo comun que CADA HIJA sobreescribe (POLIMORFISMO)
    def calcular_pago(self):
        raise NotImplementedError("Cada tipo de empleado calcula su pago.")

    def obtener_informacion(self):
        # TODO: devuelve un texto como:  "Ana | EmpleadoPlanta | Medellin | base $3000000"
        #       Pista: self.nombre, type(self).__name__, self.ciudad, self.salario_base
        return (f"{self.nombre} | {type(self).__name__} | "
                f"{self.ciudad} | base ${self.salario_base}")


# 2) CLASES HIJAS (HERENCIA)
class EmpleadoPlanta(EmpleadoBase):
    def calcular_pago(self):
        # TODO (POLIMORFISMO): el empleado de planta recibe su salario + 30% de prestaciones
        return self.salario_base * 130 / 100


class EmpleadoContratista(EmpleadoBase):
    def calcular_pago(self):
        # TODO (POLIMORFISMO): el contratista recibe solo su salario base (sin prestaciones)
        return self.salario_base


# 3) Crear el objeto correcto segun el TIPO
def crear_empleado(nombre, tipo, salario_base, ciudad):
     #Fabrica: devuelve el objeto segun el tipo o lanza ValueError.
    if tipo == "PLANTA":
        return EmpleadoPlanta(nombre, salario_base, ciudad)
    if tipo == "CONTRATISTA":
        return EmpleadoContratista(nombre, salario_base, ciudad)
    raise ValueError(f"tipo desconocido '{tipo}'")
    # TODO: si tipo == "PLANTA"       -> return EmpleadoPlanta(nombre, salario_base, ciudad)
    #       si tipo == "CONTRATISTA"  -> return EmpleadoContratista(nombre, salario_base, ciudad)
    #       si no                     -> raise ValueError(f"tipo desconocido '{tipo}'")
    


# =====================================================================
# 4) LECTURA DEL EXCEL  --  ¡YA ESTA LISTA!  (no necesitas modificarla)
#    Es ROBUSTA: usa solo las columnas que necesita (aunque el Excel tenga
#    columnas de mas), ignora filas incompletas y salta las invalidas
#    (por ejemplo un salario negativo) sin detener el programa.
# =====================================================================
def leer_empleados_excel(nombre_archivo):
    """Lee empleados desde un Excel y devuelve una lista de objetos Empleado."""
    empleados = []
    df = pd.read_excel(nombre_archivo)

    # Normalizamos los nombres de columna (sin espacios y en minuscula)
    df.columns = [str(c).strip().lower() for c in df.columns]

    # Verificamos que existan las columnas minimas que necesitamos
    columnas_necesarias = {"nombre", "tipo", "salario_base"}
    if not columnas_necesarias.issubset(df.columns):
        faltan = columnas_necesarias - set(df.columns)
        print(f"  [Error] Al Excel le faltan columnas: {faltan}")
        return empleados

    for _, fila in df.iterrows():
        # Saltar filas incompletas (sin nombre, tipo o salario)
        if pd.isna(fila["nombre"]) or pd.isna(fila["tipo"]) or pd.isna(fila["salario_base"]):
            print("  [Aviso] Fila incompleta ignorada.")
            continue

        nombre = str(fila["nombre"]).strip()
        tipo = str(fila["tipo"]).strip().upper()
        salario = fila["salario_base"]
        # 'ciudad' es una columna extra: si no viene, usamos texto vacio
        ciudad = str(fila["ciudad"]).strip() if "ciudad" in df.columns and not pd.isna(fila["ciudad"]) else ""

        try:
            empleado = crear_empleado(nombre, tipo, salario, ciudad)
            if empleado is not None:  # (por si aun no completas crear_empleado)
                empleados.append(empleado)
        except ValueError as error:
            print(f"  [Aviso] Se ignoro {nombre}: {error}")

    return empleados


# =====================================================================
# 5) RETO EXTRA: ¡CREA TU PROPIA FUNCION!
#    Inventa una funcion util que trabaje con la lista de empleados.
#    Elige UNA de estas ideas (o propon la tuya) y programala aqui abajo:

#       * salario_promedio(empleados): promedio de salario_base
#       * empleados_por_ciudad(empleados, ciudad): cuantos hay en esa ciudad
#       * empleado_mejor_pagado(empleados): el de mayor calcular_pago()

#    Documentala con un docstring y luego llamala dentro de ejecutar_quiz().
# =====================================================================
def nomina_total(empleados):
    # calcula el total del valor de la nomina sumando el valor del pago de todos los empleados
    return sum(empleado.calcular_pago() for empleado in empleados)  # Funcion principal


# 6) Funcion principal

def ejecutar_quiz():
    empleados = leer_empleados_excel("empleados.xlsx")

    print("--- Nomina ---")
    for empleado in empleados:
        # POLIMORFISMO: la misma llamada, distinto resultado segun el tipo
        print(empleado.obtener_informacion(), "-> pago:", empleado.calcular_pago())
     # Resultado de mi propia funcion
    print("\nNomina total mensual:", nomina_total(empleados))

# Iniciar el programa
ejecutar_quiz()