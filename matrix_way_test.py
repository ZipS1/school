import matrices                                  #TODO: check if dest point in area

HEIGHT = 5
WIDTH = 4
matrix = matrices.genMx(WIDTH, HEIGHT, 0, 3, True)
matrices.printMx(matrix)

while True:
    try:
        points = input("Enter starting points (x1 y1 x2 y2): ").split()
        points = [int(i) - 1 for i in points]
        start_x, start_y, dest_x, dest_y = points
    except ValueError:
        raise
    else:
        break

c_point = (start_y, start_x)

area = [c_point]

while True:
    y = c_point[0]
    x = c_point[1]

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
