def part_1(input):
    origin = [0,0]
    pos = origin

    for line in input:
        command, distance = line
        if command == 'forward':
            pos[0] += distance
        elif command == 'up':
            pos[1] -= distance
        elif command == 'down':
            pos[1] += distance
        else:
            raise AssertionError(f'Command {command} not found')

    return pos[0] * pos[1]



TEST_INPUT = '''\
forward 5
down 5
forward 8
up 3
down 8
forward 2
'''


def part_2(input):
    origin = [0, 0, 0]
    pos = origin

    for line in input:
        command, distance = line
        if command == 'forward':
            pos[0] += distance
            pos[1] += pos[2] * distance
        elif command == 'up':
            pos[2] -= distance
        elif command == 'down':
            pos[2] += distance
        else:
            raise AssertionError(f'Command {command} not found')

    return pos[0] * pos[1]


if __name__ == '__main__':
    input = [(lines.split(' ')[0], int(lines.split(' ')[1])) for lines in open("input.txt").readlines()]
    # input = [(lines.split(' ')[0], int(lines.split(' ')[1])) for lines in TEST_INPUT.splitlines()]
    print("Part 1:")
    print(part_1(input))
    print("Part 2:")
    print(part_2(input))
