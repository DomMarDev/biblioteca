def buscar_libros_por_autor(biblioteca):
    control = True
    while control:
        autor=input('Dame el nombre del autor:').lower()
        if not autor:
            print('Ingrese el nombre de un autor')
        else:
            control = False
    libros_autor = [libro for libro in biblioteca if libro['autor'] == autor]

    # libros_autor =[]
    # for libro in biblioteca:
    #     if libro['autor'] == autor:
    #         libros_autor.append(libro)
    if libros_autor:
        print(f'Libros de {autor.title()}:')
        for libro in libros_autor:
            print(f'-Título: {libro['titulo'].capitalize()}, Año: {libro['año']}')
    else:
        print(f'No se han encontrado libros de {autor}.')