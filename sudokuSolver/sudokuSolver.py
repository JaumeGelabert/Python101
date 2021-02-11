# Hay que tener en cuenta que el sudoku 'tradicional' es un 9x9, por lo que las celdas, tienen 'row' y 'col', ambas con índices del 0 al 8.

def find_next_empty(puzzle):
    # Encuntra las celdas del sudoku que estan vacias. --> '-1'
    # Cuando se de que no haya más celdas vacias, el juego se ha acabado.

    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1:
                return row, col
    return None, None  # Si no hay espacios en blanco, devolvemos None, None


def is_valid(puzzle, guess, row, col):
    # Esta funcion comprueba si la respuesta que hemos colocado en una celda es válida o no. Si es correcta, devolvemos True. Si no lo es, False.

    # Rows
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # Cols
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # Celda 3x3 interior a la de 9x9
    # Primero debemos calcular donde empieza esta celda 3x3
    row_start = (row//3) * 3
    col_start = (col//3) * 3

    for row in range(row_start, row_start + 3):
        for col in range(col_start, col_start + 3):
            if puzzle[row][col] == guess:
                return False
    return True


def solve_sudoku(puzzle):
    # Usaremos 'backtracking' para resolver el sudoku. Es decir, en la primera celda vacia, pondremos un número que sea válido. Luego, pasamos a la siguiente celda.
    # En el momento en que en una celda no se pueda poner un numero válido, retrocedemos a la celda anterior y modificamos el numero. Cuando encontremos un número
    # valido en esa celda anterior, volvemos con el proceso. Este proceso se repite a lo largo de todo el ejercicio.

    # Paso 1: Elegir por donde empezamos
    row, col = find_next_empty(puzzle)

    # Paso 1.1: Si no hay espacios en blanco, hemos terminado.
    if row is None:
        return True

    # Paso 2:  Si hay una celda vacia, debemos rellenarla
    for guess in range(1, 10):
        # Paso 3: Comprobar si la respuesta es valida
        if is_valid(puzzle, guess, row, col):
            # Paso 3.1: Si es valido, queremos colocar el numero en la celda
            puzzle[row][col] = guess
            # Paso 4: Seguir llamando la funcion hasta resolver el puzzle
            if solve_sudoku(puzzle):
                return True
        # Paso 5: si no es válido o no hemos resuelto el sudoku, necesitamos hacer 'backtracking' y probar un numero nuevo
        puzzle[row][col] = -1  # Reseteamos el número en que hacemos guess

    # Paso 6: Si ningun numero funciona, el sudoku no tiene solucion
    return False


if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)
