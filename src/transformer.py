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
        
    return output