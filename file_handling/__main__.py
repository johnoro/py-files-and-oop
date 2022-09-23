# File Handling

from .count_lines import count_lines
from .count_words import count_words
from .display_lines import display_lines
from .display_words import display_words

def main():
    path = './file_handling/'
    print('=====================')

    print('Displaying lines...\n')
    # 1. Write a function in python to read the content from a text file "poem.txt" line by line and display the same on screen.
    display_lines(path + 'poem.txt')

    print('=====================')

    print("Counting lines that don't start with 'T'...\n")
    # 2. Write a function in python to count the number of lines from a text file "story.txt" which is not starting with an alphabet "T". 
    count_lines(path + 'story.txt', lambda line: not line.startswith('T')) # 3

    print('=====================')

    print('Counting words...\n')
    # 3. Write a function in Python to count and display the total number of words in a text file.
    count_words(path + 'poem.txt')

    print('=====================')

    print("Counting the word 'the'...\n")
    # 4. Write a function in Python to read lines from a text file "notes.txt". Your function should find and display the occurrence of the word "the".
    count_words(path + 'notes.txt', lambda word: word == 'the') # 5

    print('=====================')

    print("Displaying words that are shorter than 4 characters...\n")
    # 5. Write a function display_words() in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters.
    display_words(path + 'story.txt', lambda word: len(word) < 4)

    print('=====================')

    print("Counting words 'this' and 'these'...\n")
    # 6. Write a function in Python to count the words "this" and "these" present in a text file "article.txt".
    count_words(path + 'article.txt', lambda word: word == 'this' or word == 'these')

    print('=====================')

    print("Counting words that end with 'e'...\n")
    # 7. Write a function in Python to count words in a text file those are ending with alphabet "e". 
    count_words(path + 'poem.txt', lambda word: word.endswith('e'))

    print('=====================')

    print("Counting words that are entirely uppercase...\n")
    # 8. Write a function in Python to count uppercase character in a text file.
    count_words(path + 'poem.txt', lambda word: word.isupper())
