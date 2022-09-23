def count_words(filename, by = lambda word: True):
    with open(filename, 'r') as f:
        count = 0
        for line in f:
            for word in line.split():
                if by(word):
                    count += 1
        print(count)
