p_d = 101
total_cells = p_d ** 2
square_inside = 0
square_grid = []

#this is solely for adding the tupples in the grid in a way to form the square
#only because I thought it would be cool to do so
for y in range(int((p_d * -1) / 2), int((p_d + 1) / 2)):
    for x in range(int((p_d * -1) / 2), int((p_d + 1) / 2)):
        square_grid.append((x, y * -1))

for i in square_grid:
    if (i[0] ** 2 + i[1] ** 2) ** 0.5 <= p_d/2:
        square_inside += 1

out = (square_inside / total_cells) * 4
print(out)
