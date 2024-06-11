def anadir_libro(biblioteca):
        
    while True:
        titulo = input('Ingrese el título del libro').lower()
        if not titulo:
            print('El campo titulo no puede estar vacío')
        else:
            break

    while True:
        autor = input('Ingrese el autor del libro').lower()
        if not autor:
            print('EL campo no puede estar vacio')
        else:
            break
        
    while True:
        try:
            anyo = int(input('Ingrese el año del libro'))
            break
        
        except ValueError:
            print('Inserte un año válido')
        
    biblioteca.append({'titulo' : titulo, 'autor' : autor, 'año' : anyo})

    print('Libro introducido con éxito')

    return biblioteca