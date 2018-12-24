"""humanized_bit_repr is python script that finds the bits that has value of 1 and prints them more humanized way.
    Eg.
        if you give 0x00003000 as an input the n it will print.
            > bits<12...13> is 1
        if you give
            > bit<20...20> is 1

Usage:
    humanized_bit_repr.py <value>
    humanized_bit_repr.py --version
    humanized_bit_repr.py --help
    humanized_bit_repr.py -h

Options:
    -h --help               Shows this screen
    --version               Shows version.
"""
from docopt import docopt

def humanize(val):
    start_i, end_i = -1, -1
    i = 0
    while val:
        if (val & 0x1) == 0:
            if end_i == -1 and start_i != -1:
                end_i = i
                print(f"bit{'s' if end_i - start_i > 1 else ''}<{start_i}...{end_i - 1}> is 1")
                start_i, end_i = -1, -1
        else:
            if start_i == -1:
                start_i = i
        i += 1
        val >>= 1

    if start_i != -1 and end_i == -1:
        print(f"bit{'s' if i - start_i > 1 else ''}<{start_i}...{i - 1}> is 1")

if __name__ == '__main__':
    arguments = docopt(__doc__, version="===humanized_bit_repr===\n   Version 1.0")

    try:
        VALUE = int(arguments["<value>"], 0)
    except:
        VALUE = None

    if VALUE:
        humanize(VALUE)
    else:
        print("Given value must be int.")
