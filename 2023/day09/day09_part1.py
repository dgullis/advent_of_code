with open("2023/day09/day09_input.txt", "r") as f:
    code_lines = f.readlines()

code_lines = [[int(num) for num in line.strip().split()] for line in code_lines]


def get_next_line(line):
    next_line = []
    for idx, num in enumerate(line[:-1]):
        next_num = line[idx+1] - num
        next_line.append(next_num)
    return next_line

def get_pyramids_for_line(line):
        pyramid = [line]
        next_line = line
        while True:
            next_line = get_next_line(next_line)
            pyramid.append(next_line)
            if all(num==0 for num in next_line):
                break
        return pyramid

def get_sum_of_last_numbers_on_line(pyramid):
    sum = 0
    for row in pyramid:
        sum += row[-1]
    return sum

pyramids = [get_pyramids_for_line(line) for line in code_lines]
# print("pyramids", pyramid)
sums = [get_sum_of_last_numbers_on_line(pyramid) for pyramid in pyramids]

result = sum(sums)
print(result)


