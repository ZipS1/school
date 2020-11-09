import matrices


class DiffError(Exception):
    pass

HEIGHT = 5
WIDTH = 4
matrix = matrices.genMx(WIDTH, HEIGHT, 0, 3, True)
matrices.printMx(matrix)

while True:
    try:
        points_coords = input("Enter coordinates of points (x1 y1 x2 y2): ").split()
        points_coords = [int(i) - 1 for i in points_coords]
        first_x, first_y, second_x, second_y = points_coords

        if matrix[first_y][first_x] != matrix[second_y][second_x]:
            raise DiffError
    except ValueError:
        print("\nEnter coordinates as FOUR NUMBERS x, y WITH SPACES between!\n")
    except DiffError:
        print("\nPoints with such coordinates are filled with different numbers\n")
    else:
        break

point = (first_x, first_y)
area = [point]
field = matrix[first_y][first_x]
path = []

while True:
    x, y = point
    if (x, y) == (second_x, second_y):
        print("There IS a path")
        quit()
    else:
        path.append((x, y))

    if x - 1 >= 0:
        if matrix[y][x - 1] == field and (x - 1, y) not in path:
            area.append((x - 1, y))
    if x + 1 <= (WIDTH - 1):
        if matrix[y][x + 1] == field and (x + 1, y) not in path:
            area.append((x + 1, y))
    if y - 1 >= 0:
        if matrix[y - 1][x] == field and (x, y - 1) not in path:
            area.append((x, y - 1))
    if y + 1 <= (HEIGHT - 1):
        if matrix[y + 1][x] == field and (x, y + 1) not in path:
            area.append((x, y + 1))
    area.remove(point)

    if area == []:
        print("There IS NOT a path")
        break
    else:
        point = area[0]
