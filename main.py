from ui import initApp

# Importar módulos necesarios
import sys  # Módulo para interactuar con el sistema
import os   # Módulo para operaciones del sistema operativo

# Definición de funciones
def main():
    """
    Función principal del programa.
    Aquí es donde se ejecuta la lógica principal.
    """
    initApp()

    # Aquí puedes agregar más lógica
    # Por ejemplo, leer argumentos de la línea de comandos
    if len(sys.argv) > 1:
        print(f"Argumentos recibidos: {sys.argv[1:]}")
    else:
        print("No se recibieron argumentos.")

def helper_function():
    """
    Función de ayuda que puede ser utilizada en el programa.
    """
    pass  # Implementa la lógica de la función aquí

# Comprobación de si el script se está ejecutando directamente
if __name__ == "__main__":
    main()  # Llamar a la función principal
