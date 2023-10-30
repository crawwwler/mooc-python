layers = int(input("Layers: "))
letters = [chr(64+layers-i) for i in range(layers)]

grid = [[letters[-1] for j in range(layers*2-1)] for i in range(layers*2-1)]

for i in range(layers):
    for j in range(i, layers*2-1-i):
        grid[i][j] = letters[i]
        grid[j][i] = letters[i]
        grid[layers*2-2-i][j] = letters[i]
        grid[j][layers*2-2-i] = letters[i]

for row in grid:
        print("".join(row))

