space = ' '
star = '*'


def print_triangle(r):
    line_size = 2*r - 1
    for x in range(r):
        space_count = line_size//2 - x
        print(space_count*space + (2*x+1)*'*' + space_count*space)


def print_triangle_reverse(r):
    row_size = 2*r - 1
    for x in range(r-1, -1, -1):
        space_count = row_size//2 - x
        print(space_count*space + (2*x+1)*'*' + space_count*space)


def print_diamond(r):
    print_triangle(r)
    print_triangle_reverse(r)


# print_diamond(9)


def print_star(r):
    if(r % 4 != 0):
        print("input isn't divisible by 4")
        exit()
    prints = []
    chunk = r//2+1
    row_size = 2*r - 1
    for x in range(chunk):
        if(x < chunk//2):
            space_count = row_size//2 - x
            s = space_count*space + (2*x+1)*'*' + space_count*space
            print(s)
            prints.append(s)
        elif(x == chunk//2):
            prints.append(row_size*star)
            print(row_size*star)
        else:
            space_count = x - chunk//2
            s = space_count*space + ((row_size//2-space_count)*2+1)*star
            print(s)
            prints.append(s)
    prints = reversed(prints)
    for s in prints:
        print(s)


print_star(16)
