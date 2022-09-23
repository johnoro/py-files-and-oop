def display_lines(filename, by = lambda line: True):
    with open(filename, 'r') as f:
        for line in f:
            print(line)
