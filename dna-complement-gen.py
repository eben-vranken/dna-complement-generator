from argparse import ArgumentParser
from src import transformer

def get_args():
    parser = ArgumentParser()

    parser.add_argument("dna")

    parser.add_argument("-c", "--complement", action="store_true", help="Flag to enable complement generation of the DNA string")
    parser.add_argument("-r", "--reverse", action="store_true", help="Flag to enable reversing of the DNA string")

    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()

    output = args.dna

    if args.complement:
        output = transformer.invert_dna_string(output)
    if args.reverse:
        output = transformer.reverse_dna_string(output)

    print(output)