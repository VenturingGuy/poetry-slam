import random
'''
get_file_lines receives a text file as an argument, creates and returns
a list of strings called lineList using the lines from the filename that are
separated by a newline, or backslash n.
'''


def get_file_lines(filename):
    lineList = [line.rstrip('\n') for line in open(filename)]
    return lineList


'''
lines_printed_backwards receives a list of lines, expectedly the
lineList returned from the get_file_lines function, and uses the
built in reversed() function to print each line from the list
starting from the last line.
'''


def lines_printed_backwards(lineList):
    for line in reversed(lineList):
        print(line)


def lines_printed_random(lineList):
    for _ in range(len(lineList)):
        print(random.choice(lineList))


poem = get_file_lines("poem.txt")
lines_printed_backwards(poem)
poem = get_file_lines("poem.txt")
lines_printed_random(poem)
