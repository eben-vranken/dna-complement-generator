def invert_dna_string(dna_string):
    output = ""
    
    for c in dna_string.upper():
        match c:
            case "A":
                output += "T"
            case "T":
                output += "A"
            case "C":
                output += "G"
            case "G":
                output += "C"
            case _:
                raise ValueError(f"Invalid base: {c}")

    return output

def reverse_dna_string(dna_string):
    return dna_string[::-1]