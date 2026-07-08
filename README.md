<h1 align="center">🧬 DNA Complement Generator</h1>

<p align="center">
    A lightweight command-line tool to generate the complement or reverse complement of a DNA sequence.
</p>

<p align="center">
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License"></a>
</p>

A small, zero-dependency Python CLI that takes a raw DNA string and applies standard base-pairing rules (A↔T, C↔G) to produce its complement, its reverse, or its reverse complement.

## Install

Clone the repository directly:
```bash
git clone https://github.com/eben-vranken/dna-complement-generator.git
cd dna-complement-generator
```

## Usage

Pass a DNA sequence as a positional argument, with flags to control the transformation:

```bash
python dna-complement-gen.py CCGATTC -c
```

### Reverse Complement

Combine `-c` and `-r` to get the true reverse complement (the biologically real opposite strand):

```bash
python dna-complement-gen.py CCGATTC -c -r
```

## Configuration Matrix

| Argument | Option / Choices | Default | Description |
| --- | --- | --- | --- |
| `dna` | *Positional sequence string* | *Required* | The raw DNA sequence to transform. |
| `-c`, `--complement` | *Flag* | `False` | Swaps each base for its pair (A↔T, C↔G). |
| `-r`, `--reverse` | *Flag* | `False` | Reverses the string. Combine with `-c` for reverse complement. |

## Feature Set

* **Standard Base Pairing:** Applies the A↔T, C↔G complement rule to any input sequence.
* **Case Insensitive:** Automatically uppercases input before processing.
* **Composable Flags:** `-c` and `-r` can be used independently or together, in the order applied.

## License

MIT