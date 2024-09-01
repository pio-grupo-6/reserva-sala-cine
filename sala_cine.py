import os
import pickle

# Configuración inicial
ARCHIVO_SALAS = 'salas.pkl'
ARCHIVO_SALAS_TEXTO = 'salas_convertido.txt'

def guardar_datos(salas):
    with open(ARCHIVO_SALAS, 'wb') as file:
        pickle.dump(salas, file)

def cargar_datos():
    if os.path.exists(ARCHIVO_SALAS):
        with open(ARCHIVO_SALAS, 'rb') as file:
            return pickle.load(file)
    return {}

def carga_sala_adicional():
    if not os.path.exists(ARCHIVO_SALAS_EXTERNO):
        print(f"No se encontró el archivo '{ARCHIVO_SALAS_EXTERNO}'.")
        return None
    
    try:
        with open(ARCHIVO_SALAS_EXTERNO, 'r') as file:
            # Leer líneas del archivo
            lines = file.readlines()

        if not lines:
            print("El archivo está vacío.")
            return None
        
        # Construir la sala a partir de las líneas leídas
        sala = [line.strip().split() for line in lines]
        
        return sala
    
    except Exception as e:
        print(f"Error al cargar la sala desde el archivo: {e}")
        return None

def crear_sala():
    salas = cargar_datos()
    nombre_sala = input("Ingrese el nombre de la sala: ")
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    
    # Crear una matriz para la sala con números secuenciales
    numero_asiento = 1
    sala = []
    for _ in range(filas):
        fila = []
        for _ in range(columnas):
            fila.append(str(numero_asiento).zfill(3))  # Asientos numerados, relleno con ceros
            numero_asiento += 1
        sala.append(fila)
    
    salas[nombre_sala] = sala
    guardar_datos(salas)
    print(f"Sala '{nombre_sala}' creada exitosamente.")

def ver_sala():
    salas = cargar_datos()
    nombre_sala = input("Ingrese el nombre de la sala que desea ver: ")
    
    if nombre_sala in salas:
        sala = salas[nombre_sala]
        # Determinar el ancho máximo para cada columna
        max_len = max(len(str(asiento)) for fila in sala for asiento in fila)
        for fila in sala:
            print(' '.join(f"{asiento:>{max_len}}" for asiento in fila))
    else:
        print("Sala no encontrada.")

def asignar_puesto():
    salas = cargar_datos()
    nombre_sala = input("Ingrese el nombre de la sala: ")

    if nombre_sala in salas:
        sala = salas[nombre_sala]
        numero_asiento = input("Ingrese el número de asiento que desea reservar: ").zfill(3)

        reservado = False
        for fila in sala:
            for i in range(len(fila)):
                if fila[i] == numero_asiento:
                    fila[i] = 'XXX'
                    reservado = True
                    break
            if reservado:
                break

        if reservado:
            guardar_datos(salas)
            print(f"Puesto {numero_asiento} reservado exitosamente.")
        else:
            print("El puesto no está disponible o ya ha sido reservado.")
    else:
        print("Sala no encontrada.")

def guardar_datos_en_texto():
    salas = cargar_datos()
    try:
        with open(ARCHIVO_SALAS_TEXTO, 'w') as file:
            for nombre_sala, sala in salas.items():
                file.write(f"Sala: {nombre_sala}\n")
                for fila in sala:
                    file.write(' '.join(f"{asiento}" for asiento in fila) + '\n')
                file.write('\n')
        print(f"Datos guardados en '{ARCHIVO_SALAS_TEXTO}' exitosamente.")
    except Exception as e:
        print(f"Error al guardar los datos en el archivo de texto: {e}")

def cargar_sala():
    guardar_datos_en_texto()  # Guarda los datos en el archivo de texto
    if not os.path.exists(ARCHIVO_SALAS_TEXTO):
        print("No hay salas cargadas.")
        return
    
    try:
        with open(ARCHIVO_SALAS_TEXTO, 'r') as file:
            print("Contenido del archivo de texto:")
            print(file.read())
    except Exception as e:
        print(f"Error al leer el archivo de texto: {e}")

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Menú principal')
    print('1. Crear sala')
    print('2. Ver sala')
    print('3. Asignar puesto')
    print('4. Cargar sala')
    print('5. Salir')

def main():
    while True:
        menu()
        opcion = int(input('Escoja la opción: '))
        
        match opcion:
            case 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                crear_sala()
                input('\nPresione <ENTER> para continuar')
            case 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                ver_sala()
                input('\nPresione <ENTER> para continuar')
            case 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                asignar_puesto()
                input('\nPresione <ENTER> para continuar')
            case 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                cargar_sala()
                input('\nPresione <ENTER> para continuar')
            case 5:
                print("Saliendo del programa...")
                break
            case _:
                print('Opción incorrecta, intente de nuevo')
                input('\nPresione <ENTER> para continuar')

if __name__ == "__main__":
    main()
