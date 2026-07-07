from data import DATOS_BASE
from registry import RegistroPersonas

def main():
    # 1. Instanciar el procesador y cargar datos
    registro = RegistroPersonas()
    registro.cargar_datos(DATOS_BASE)
    print(f"Datos cargados exitosamente. ({len(registro._personas)} registros)\n")

    # 2. Formateo de registros
    print("1. Formateo de Registros")
    registros_formateados = registro.formatear_registros()
    for dni, datos in registros_formateados.items():
        print(f"DNI {dni}: {datos}")
    print()

    # 3. Obtener extremos de edad
    print("2. Extremos de Edad")
    mayor = registro.obtener_mayor_edad()
    menor = registro.obtener_menor_edad()
    print(f"Persona con mayor edad: {mayor.nombre} {mayor.apellido} ({mayor.edad} años)")
    print(f"Persona con menor edad: {menor.nombre} {menor.apellido} ({menor.edad} años)")
    print()

    # 4. Promedio de edad
    print("3. Promedio de Edad")
    promedio = registro.promedio_edad()
    print(f"Promedio de edad de los registros: {promedio:.2f} años\n")

    # 5. Segmentación de población
    print("4. Segmentación de Población (Umbral: 25)")
    segmentacion = registro.segmentar_por_edad(25)
    print("Menores o iguales a 25 años:")
    for p in segmentacion["menor_igual"]:
        print(f"  - {p.nombre} {p.apellido} ({p.edad})")
    
    print("Mayores de 25 años:")
    for p in segmentacion["mayor"]:
        print(f"  - {p.nombre} {p.apellido} ({p.edad})")
    print()

    # 6. Acceso Eficiente
    print("5. Acceso Eficiente (Consulta por DNI)")
    dni_consulta = '11111111'
    edad_consultada = registro.consultar_edad(dni_consulta)
    print(f"La edad asociada al DNI {dni_consulta} es: {edad_consultada} años\n")

if __name__ == "__main__":
    main()
