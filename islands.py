import matrices

HEIGHT = 5
WIDTH = 4
matrix = matrices.genMx(WIDTH, HEIGHT, 0, 1, True)
matrices.printMx(matrix)

color = 1

area = []
passed_pts = []
island_count = 0


for ix in range(WIDTH):
    for iy in range(HEIGHT):
        if matrix[iy][ix] == 1 and (iy, ix) not in passed_pts:
            area = [(iy, ix)] 
            while area != []:
                point = area[0]   # !!!! ВОТ ОНА ПОГАНКА (↓) !!!! Цикл перебирал только точки вокруг стартовой
                # point = (iy, ix)
                y = point[0]
                x = point[1]
                # !!! И ЕЩЕ ОДНА !!! Проверка начальной точки была проведена выше, надобности проверять нет
                # if (y, x) in passed_pts: 
                #     continue


                # А вот проверка точек которые мы в массив добавляем (↓) критически необходима
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
            island_count += 1
            # Это тоже лишнее, т.к условием выхода из цикла уже является пустой список
            # area = []
            
print("Островов:", island_count)

