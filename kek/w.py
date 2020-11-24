n, m = map(int, input().split())
island = []

for i in range(n):
    island.append(input())

count = 0

for iy in range(n):
    for ix in range(m):
        if island[iy][ix] == "E":
            can_run = True
            for i in range(ix + 1, m):
                if island[iy][i] == "W":
                    can_run = False
                if can_run == True:
                    count += 1

        if island[iy][ix] == "W":
            can_run = True
            for i in range(ix):
                if island[iy][i] == "E":
                    can_run = False
                if can_run == True:
                    count += 1

        if island[iy][ix] == "S":
            can_run = True
            for i in range(iy + 1, n):
                if island[iy][i] == "N":
                    can_run = False
                if can_run == True:
                    count += 1

        if island[iy][ix] == "E":
            can_run = True
            for i in range(iy + 1, ):
                if island[iy][i] == "S":
                    can_run = False
                if can_run == True:
                    count += 1
