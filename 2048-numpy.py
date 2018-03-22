from random import randrange
import numpy as np

def addRandom(matrix):
    x = randrange(4)
    y = randrange(4)
    while(True):
        if (matrix[x, y] == 0):
            matrix[x, y] = 2 * randrange(1, 3)
            break
    else:
        x = randrange(4)
        y = randrange(4)
    return matrix

def moveNumbers(matrix):
    for i in range(4):
        for j in range(1, 4):
            if matrix[i, j] != 0:
                for k in range(j):
                    if matrix[i, k] == 0:
                        matrix[i, k], matrix[i, j] = matrix[i, j], matrix[i, k]
                        break
    return matrix

def addNumbers(matrix):
    for i in range(4):
        for j in range(3):
            if matrix[i, j] == matrix[i, j + 1]:
                matrix[i, j] += matrix[i, j + 1]
                matrix[i, j + 1] = 0
    return matrix

def izquierda(matrix):
    matrix = moveNumbers(matrix)
    matrix = addNumbers(matrix)
    return moveNumbers(matrix)

def arriba(matrix):
    matrix = np.rot90(matrix)
    matrix = moveNumbers(matrix)
    matrix = addNumbers(matrix)
    matrix = moveNumbers(matrix)
    return np.rot90(matrix, -1)

def derecha(matrix):
    matrix = np.rot90(matrix, 2)
    matrix = moveNumbers(matrix)
    matrix = addNumbers(matrix)
    matrix = moveNumbers(matrix)
    return np.rot90(matrix, -2)

def abajo(matrix):
    matrix = np.rot90(matrix, -1)
    matrix = moveNumbers(matrix)
    matrix = addNumbers(matrix)
    matrix = moveNumbers(matrix)
    return np.rot90(matrix, 1)

def iniciarTabla(n):
    return np.zeros((n, n))

def tablaLlena(matrix):
    for i in range(4):
        for j in range(4):
            if matrix[i, j] == 0:
                return False
    return True

def validarJuego(matrix):
    if tablaLlena(matrix):
        for i in range(3):
            for j in range(3):
                if matrix[i, j] == matrix[i + 1, j]:
                    return True
                if matrix[i, j] == matrix[i, j + 1]:
                    return True

        for i in range(3):
            if matrix[i, 3] == matrix[i + 1, 3]:
                return True
            if matrix[3, i] == matrix[3, i + 1]:
                return True
        return False
    return True

board = iniciarTabla(4)
board = addRandom(board)
board = addRandom(board)
print("*************************")
print("*          w:▲          *")
print("*      a:◄ s:▼ d:►      *")
print("*************************")
print(board)

while(True):
    print("Direction: ")
    direction = input()
    lastBoard = board.copy()
    agregarNumero = 1

    if direction == "a":
        print("Your direction was {}".format(direction))
        board = izquierda(board)
    elif direction == "s":
        print("Your direction was {}".format(direction))
        board = abajo(board)
    elif direction == "w":
        print("Your direction was {}".format(direction))
        board = arriba(board)
    elif direction == "d":
        print("Your direction was {}".format(direction))
        board = derecha(board)
    else:
        agregarNumero = 0

    if np.array_equal(board, lastBoard):
        print("Movimiento no valido")
        agregarNumero = 0

    if agregarNumero == 1:  
        board = addRandom(board)
        print(board)

    if not validarJuego(board):
        print("The game has finished")
        print("Want to play again (y/n)?:")
        answer = input()

        while answer not in ["y","n"]:
            print("The game has finished")
            print("Want to play again (y/n)?:")
            answer = input()

        if answer == "y":
            board = iniciarTabla(4)
            board = addRandom(board)
            board = addRandom(board)
            print(board)
        elif answer == "n":
            print("ADIOS")
            break
