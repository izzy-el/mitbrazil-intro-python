possible = ['up', 'right', 'down', 'left']


def grid_generator(size):
    return [[0 for row in range(size)] for column in range(size)]


def split_rules(rules):
    return [char for char in rules]


def turn(grid, position, rules):
    return rules[grid[position[0]][position[1]] % (len(grid))]


def update(grid, position, rules):
    grid[position[0]][position[1]] = (
        grid[position[0]][position[1]] + 1) % (len(rules))


def is_in_grid(size, position):
    return 0 <= position[0] < size and 0 <= position[1] < size


def update_facing(rotation, direction):
    if rotation == 'R':
        return possible[(possible.index(direction) + 1) % 4]
    else:  # in case it is Left 'L'
        return possible[(possible.index(direction) + 3) % 4]


def walk(position, direction):
    if direction == 'up':
        return ((position[0] - 1), position[1])
    elif direction == 'down':
        return ((position[0] + 1), position[1])
    elif direction == 'right':
        return (position[0], (position[1] + 1))
    elif direction == 'left':
        return (position[0], (position[1] - 1))


def run_langton(rules, size):
    possible_results = [(i, j) for i in range(size) for j in range(size)]

    grid = grid_generator(size)
    rules = split_rules(rules)
    position = (size // 2, size // 2)
    isgrid = is_in_grid(size, position)
    facing = 'up'
    count = 0

    while isgrid == True:
        try:
            update(grid, position, rules)
            position = walk(position, facing)
            count += 1
            isgrid = is_in_grid(size, position)
            facing = update_facing(turn(grid, position, rules), facing)
        except:
            break

    return (count, grid)


print(run_langton('RLRR', 301))
