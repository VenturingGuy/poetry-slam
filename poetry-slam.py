import random as random
from random import shuffle


'''
get_file_lines receives a text file as an argument, creates and returns
a list of strings called lines_list using the lines from the filename that are
separated by a newline, or backslash n.
'''


def get_file_lines(filename):
    read_line = open(filename, "r")
    lines_list = [line.rstrip('\n') for line in read_line]
    read_line.close()
    return lines_list


'''
lines_printed_backwards receives a list of lines, expectedly the
lines_list returned from the get_file_lines function.
Additionally, a txt file is opened (or written if not already existing)
and saved to a variable called backwards_poem.
An enumerated list is created which keeps track of the number of each
line in the poem.
The function then iterates backwards through the enumerated list using
the built in reversed Python function.
Afterwards, each line separated by a newline is saved to the txt file
as each line number and line is printed.
'''


def lines_printed_backwards(lines_list):
    backwards_poem = open("backwardsPoem.txt", "w")
    enumerated_list = list(enumerate(lines_list, 1))
    for line, value in reversed(enumerated_list):
        backwards_poem.write(value + "\n")
        print(line, value)
    backwards_poem.close()


'''
Similarly to lines_printed_backwards, a txt file is opened/written.
A random_line variable is initialized and a random line is selected
from the list, and saved to the random_line variable.
For every line in the poem, a random line is saved to the txt file
and printed out.
'''


def lines_printed_random(lines_list):
    random_poem = open("randomPoem.txt", "w")
    random_line = ""
    for _ in range(len(lines_list)):
        random_line = random.choice(lines_list)
        random_poem.write(random_line + "\n")
        print(random_line)
    random_poem.close()


'''
Follows a similar convention as the previous 2 functions with respect
to the text files.
This function will print out every line with the 2 keyphrases used stored
in the defined corresponding variables.
Separated by newlines, stored, and printed for the user to see.
'''


def lines_printed_custom(lines_list):
    custom_poem = open("customPoem.txt", "w")
    key_phrase_1 = "Nevermore"
    key_phrase_2 = "nevermore"
    for line in lines_list:
        if (key_phrase_1 in line) or (key_phrase_2 in line):
            custom_poem.write(line + "\n")
            print(line)
    custom_poem.close()


'''
Similar text file convention.
Iterates through each line in lines_list, splits the line into words,
shuffles the order of words, rejoins the line into a joined_line variable.
Writes the joined line into a file, prints the joined lines.
'''


def lines_printed_scrambled(lines_list):
    scrambled_poem = open("scrambledPoem.txt", "w")
    for line in lines_list:
        split_line = line.split()
        shuffle(split_line)
        joined_line = (' '.join(split_line))
        scrambled_poem.write(joined_line)
        print(joined_line)
    scrambled_poem.close()


'''
The menu function of the program.
Initializes 2 input variables, 1 for handling the menu, the other for
receiving a filename. Note that this input, as is, may be prone to many
errors, making this worth looking into in the future.

Prints a message asking the user to input a text filename such as 'poem.txt'.

Then, prints a message asking the user to input which function to call.

Typing 5 will exit the program.
'''


def main_menu():
    menu_input = 0
    poem_input = ""

    print("""
    Welcome to the poetry slam!\n
    To get started, please input a text file name located in the
    directory.\n""")
    poem_input = input("Please enter a valid txt file name. ")
    poem = get_file_lines(poem_input)

    print("""
    Note: selecting any of the following will also write
    a poem in a txt file.\n
    To print it backwards, input 1.\n
    To print random lines from the poem, input 2.\n
    To print only lines that have the phrase "Nevermore" in them, input 3.\n
    To print a poem with the words in each line scrambled, input 4.\n
    To exit, input 5.\n""")

    while menu_input != 5:
        menu_input = int(input("Input your selection here: "))
        if menu_input == 1:
            lines_printed_backwards(poem)
        elif menu_input == 2:
            lines_printed_random(poem)
        elif menu_input == 3:
            lines_printed_custom(poem)
        elif menu_input == 4:
            lines_printed_scrambled(poem)
        elif menu_input == 5:
            break
        else:
            print("Invalid input. Please try again.")


main_menu()
