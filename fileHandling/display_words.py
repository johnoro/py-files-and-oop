def display_words(filename, by = lambda word: True):
    with open(filename, 'r') as f:
        for line in f:
            for word in line.split():
                if by(word):
                    print(word)
