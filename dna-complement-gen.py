from argparse import ArgumentParser

def get_args():
    parser = ArgumentParser()

    parser.add_argument("dna")

    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()

    print(args.dna)