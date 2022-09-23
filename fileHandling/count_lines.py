def count_lines(filename, by = lambda line: True):
    with open(filename, 'r') as f:
        count = 0
        for line in f:
            if by(line):
                count += 1
        print(count)
