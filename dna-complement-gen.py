from argparse import ArgumentParser
from src import transformer

def get_args():
    parser = ArgumentParser()

    parser.add_argument("dna")

    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()

    complement = transformer.invert_dna_string(args.dna)
    
    print(complement)