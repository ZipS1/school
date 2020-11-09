import matrices

HEIGHT = 5
WIDTH = 4
matrix = matrices.genMx(WIDTH, HEIGHT, 0, 3, True)

matrices.printMx(matrix)

while True:
    try:
        start_point = input("Enter starting point (x, y): ").split()
        start_point = [int(i) - 1 for i in start_point]
        start_x, start_y = start_point
    except ValueError:
        print("\nEnter coordinates as a TWO NUMBERS x, y WITH SPACE between!\n")
    else:
        break

color = matrix[start_y][start_x]
new_color = int(input("Enter your color (0-3): "))
if color == new_color:
    matrices.printMx(matrix)

c_point = (start_y, start_x)

area = [c_point]

while True:
    y = c_point[0]
    x = c_point[1]
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
    area.remove(c_point)

    if area == []:
        matrices.printMx(matrix)
        quit()
    else:
        c_point = area[0]
