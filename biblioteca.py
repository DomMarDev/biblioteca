from modulos.screen import clear_screen, pause_screen
from modulos.anadir import anadir_libro
from modulos.buscar import buscar_libros_por_autor
from modulos.borrar import eliminar_libro
from modulos.mostrar import mostrar_libros

# Programa Principal

def gestionar_biblioteca(biblioteca):
    while True:
        clear_screen()
        print('''
        Menú de Opciones:
            1) Añadir
            2) Mostrar
            3) Buscar
            4) Eliminar
            5) Terminar
    ''')
        opcion = input('Seleccione una opción:')

        if opcion == '1':
            # pass
            clear_screen()
            anadir_libro(biblioteca)
            pause_screen()
        elif opcion == '2':
            clear_screen()
            mostrar_libros(biblioteca)
            pause_screen()
        elif opcion == '3':
            clear_screen()
            buscar_libros_por_autor(biblioteca)
            pause_screen()
        elif opcion == '4':
            clear_screen()
            eliminar_libro(biblioteca)
            pause_screen()
        elif opcion == '5':
            print('Terminando el programa')
            break
        else:
            print('Opción no contemplada')
            pause_screen()

# Así nos aseguramos que se ejecuta desde el programa principal y sólo desde este.
if __name__ == '__main__':
    biblioteca = []
    gestionar_biblioteca(biblioteca)


