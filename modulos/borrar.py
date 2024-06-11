def eliminar_libro(biblioteca):
    control = True
    while control:
        titulo = input('Introduce el título a eliminar').lower()
        if not titulo:
            print('Introduce un título, el cmapo no puede estar vacío.')
        else:
            control = False
    for libro in biblioteca:
        if libro['titulo'] == titulo:
            biblioteca.remove(libro)
            print('Libro eliminado con éxito.')
            return
        else:
            print('No se encontró el libro con el título especificado')