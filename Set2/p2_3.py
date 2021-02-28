def ndoors(num_of_doors):
    open_doors = []
    counter = 2

    for i in range(1, num_of_doors + 1):
        open_doors.append(i)

    while counter <= num_of_doors:
        for i in range(counter, num_of_doors + 1, counter):
            if i in open_doors:
                open_doors.remove(i)
            else:
                open_doors.append(i)
        counter +=1

    return open_doors
