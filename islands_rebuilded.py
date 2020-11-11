import matrices

HEIGHT = 5
WIDTH = 4
matrix = matrices.genMx(WIDTH, HEIGHT, 0, 1, True)
matrices.printMx(matrix)

island_count = 0
color = 1
area = []
passed_pts = []

for ix in range(WIDTH):
    for iy in range(HEIGHT):
        if matrix[iy][ix] == 1 and (iy, ix) not in passed_pts:
            start_point = (iy, ix)
            passed_pts.append(start_point)
            area.append(start_point)
            while area != []:
                y, x = area[0]
                if x - 1 >= 0:
                    if matrix[y][x - 1] == color and (y, x - 1) not in passed_pts:
                        area.append((y, x - 1))
                        passed_pts.append((y, x - 1))
                if x + 1 <= (WIDTH - 1):
                    if matrix[y][x + 1] == color and (y, x + 1) not in passed_pts:
                        area.append((y, x + 1))
                        passed_pts.append((y, x + 1))
                if y - 1 >= 0:
                    if matrix[y - 1][x] == color and (y - 1, x) not in passed_pts:
                        area.append((y - 1, x))
                        passed_pts.append((y - 1, x))
                if y + 1 <= (HEIGHT - 1):
                    if matrix[y + 1][x] == color and (y + 1, x) not in passed_pts:
                        area.append((y + 1, x))
                        passed_pts.append((y + 1, x))
                area.pop(0)
            area = []
            island_count += 1

print("Островов:", island_count)
