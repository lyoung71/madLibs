import re


def mad_libs(string):
    new_mad_lib = open('madlib.txt', 'w')
    adj_regex = re.compile(r'ADJECTIVE+')
    noun_regex = re.compile(r'NOUN+')
    verb_regex = re.compile(r'VERB+')

    split_string = string.split('. ')
    for sentence in split_string:
        sentence = adj_regex.sub(input("Enter an adjective: "), sentence)
        sentence = noun_regex.sub(input('Enter a noun: '), sentence)
        sentence = verb_regex.sub(input('Enter a verb: '), sentence)
        new_mad_lib.write(f'{sentence}. ')
    new_mad_lib.close()


string1 = "The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events."

mad_libs(string1)
