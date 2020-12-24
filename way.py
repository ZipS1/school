import matrices

HEIGHT = 5
WIDTH = 4
matrix = matrices.gen_mx(WIDTH, HEIGHT, 0, 3, True)
matrices.print_mx(matrix)

# input: two nums x,y with space between
startpoint = input("Enter starting point (x y): ").split()
endpoint = input("Enter final point (x y): ").split()
startpoint = [int(i) - 1 for i in startpoint]
endpoint = [int(i) - 1 for i in endpoint]
start_x, start_y = startpoint
end_x, end_y = endpoint

color = matrix[start_y][start_x]
point = (start_y, start_x)
area = [point]
passed_pts = []

while area != []:
    y, x = area[0]
    if (y, x) == (end_y, end_x):
        print("There IS a way")
        quit()

    if x - 1 >= 0:
        if matrix[y][x - 1] == color and (y, x - 1) not in passed_pts:
            area.append((y, x - 1))
            passed_pts.append((y, x - 1))
    if x + 1 <= (WIDTH - 1) :
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
print("There IS NOT a way")
