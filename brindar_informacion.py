#Brinda informacion sobre series y peliculas
consulta = input("Ingrese el artista, serie o pelicula: ").lower()

match consulta:
    case "inception":
        info = "Pelicula de ciencia ficcion dirigida por Christopher Nolan"
    case "beatles":
        info = "Banda de rock britanica formada en 1960"
    case "rick and morty":
        info = "Serie animada de comedia y ciencia ficcion"
    case "stranger things":
        info = "Serie de terror y ciencia ficcion de Netflix"
    case "avengers":
        info = "Pelicula de superheroes del MCU"
    case _:
        info = "No se encontro informacion"

print("Informacion: ", info)
