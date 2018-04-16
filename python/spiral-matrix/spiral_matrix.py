#!/usr/bin/env python
#encoding=utf8


def get_next_location(direction, location):
    if direction == "right":
        return location[0], location[1] + 1
    elif direction == "down":
        return location[0] + 1, location[1]
    elif direction == "left":
        return location[0], location[1] - 1
    else:
        return location[0] - 1, location[1]


def fill(array, number, location, direction):
    rotate = {'right': 'down', 'down': 'left', 'left': 'up', 'up': 'right'}
    array[location[0]][location[1]] = number
    next_location = get_next_location(direction, location)

    try:
        next_point = array[next_location[0]][next_location[1]]
        if next_point is not None:
            raise IndexError
    except IndexError:
        direction = rotate[direction]
        return get_next_location(direction, location), direction

    return next_location, direction


def spiral(size):
    numbers = list(range(1, size ** 2 + 1))
    array = [[None for i in range(size)] for i in range(size)]
    location = (0, 0)
    direction = "right"
    for number in numbers:
        location, direction = fill(array, number, location, direction)
    return array


#spiral(5)
