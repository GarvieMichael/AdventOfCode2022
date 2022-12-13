import pprint as pp
import numpy as np
text_file = open("Day6/Day6.txt")
signals = text_file.readlines()
signal_count = 0
signal_length = len(signals[0])


def find_first_four_unique_characters(text_string, sig_length):
    for i in range(0, sig_length-4, 1):
        segment = text_string[i:i+4]
        if (len(set(segment)) == len(segment)):
            return i+4 
        # print(text_string)
        # print(segment)

def find_first_14_unique_characters(text_string, sig_length):
    for i in range(0, sig_length-14, 1):
        segment = text_string[i:i+14]
        if (len(set(segment)) == len(segment)):
            return i+14 
        # print(text_string)
        # print(segment)


    # print(text_string)
    # print(count)
    # print(sig_length) 

    # pp.pprint(text_string)

# signal_count = find_first_four_unique_characters(signals[0], signal_length)
signal_count = find_first_14_unique_characters(signals[0], signal_length)


pp.pprint(signal_count)