import matrices

HEIGHT = 5
WIDTH = 4
matrix = matrices.genMx(WIDTH, HEIGHT, 0, 3, True)
matrices.printMx(matrix)

# input: two nums x,y with space between
start_point = input("Enter starting point (x y): ").split()
start_point = [int(i) - 1 for i in start_point]
start_x, start_y = start_point

color = matrix[start_y][start_x]
new_color = int(input("Enter your color (0-3): "))  # input: int 0-3

point = (start_y, start_x)
area = [point]

<<<<<<< HEAD
while area != []:
    y, x = area[0]
=======
area = [c_point]

while area != []:
    c_point = area[0]
    y = c_point[0]
    x = c_point[1]
>>>>>>> 6355ccbbaea212f4513067f67ad867702c6ac0e8
    matrix[y][x] = new_color

    if x - 1 >= 0:
        if matrix[y][x - 1] == color:
            area.append((y, x - 1))
    if x + 1 <= (WIDTH - 1):
        if matrix[y][x + 1] == color:
            area.append((y, x + 1))
    if y - 1 >= 0:
        if matrix[y - 1][x] == color:
            area.append((y - 1, x))
    if y + 1 <= (HEIGHT - 1):
        if matrix[y + 1][x] == color:
            area.append((y + 1, x))
    area.pop(0)

matrices.printMx(matrix)
