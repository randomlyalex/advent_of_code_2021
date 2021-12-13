def part_1(input):

    count = 0
    previous = input[0]
    for number in input:
        if number > previous:
            count += 1
        previous = number
    return count


TEST_INPUT = '''\
199
200
208
210
200
207
240
269
260
263
'''


def part_2(input):
    count = 0

    for number in range(3, len(input)):
        if input[number] > input[number - 3]:
            count += 1
    return count


if __name__ == '__main__':
    input = [int(lines) for lines in open("input.txt").readlines()]
    # input = [int(line) for lines in TEST_INPUT.splitlines()]
    print("Part 1:")
    print(part_1(input))
    print("Part 2:")
    print(part_2(input))
