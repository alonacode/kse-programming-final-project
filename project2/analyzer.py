"""
DNA Sequence Analyzer
Project 2 - Programming Fundamentals
"""


def count_nucleotides(sequence):
    """
    Count how many A, T, G, C are in a DNA sequence.
    :param sequence:
    :return dict:
    """
    counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}

    for letter in sequence:
        if letter in counts:
            counts[letter] += 1

    return counts


def calculate_gc_content(sequence):
    """
    Calculate what percentage of the sequence is G or C.
    :param sequence:
    :return float:
    """
    counts = count_nucleotides(sequence)
    gc_count = counts['G'] + counts['C']
    total_length = len(sequence)

    if total_length == 0:
        return 0.0

    return (gc_count / total_length) * 100


def find_complement(sequence):
    """
    Find the complement of a DNA sequence.
    A ↔ T, G ↔ C
    :param sequence:
    :return str:
    """
    complement = ""

    for letter in sequence:
        if letter == 'A':
            complement += 'T'
        elif letter == 'T':
            complement += 'A'
        elif letter == 'G':
            complement += 'C'
        elif letter == 'C':
            complement += 'G'

    return complement


def is_valid_dna(sequence):
    """
    Check if a sequence contains only A, T, G, C.
    :param sequence:
    :return bool:
    """
    for letter in sequence:
        if letter not in ['A', 'T', 'G', 'C']:
            return False
    return True


def read_sequences_from_file(filename):
    """
    Read DNA sequences from a file.
    Format: Each line is one sequence
    :param filename:
    :return list:
    """
    sequences = []

    with open(filename, 'r') as file:
        for line in file:
            sequence = line.strip()
            if sequence != "":
                sequences.append(sequence)

    return sequences


def find_longest_sequence(sequences):
    """
    Return the longest sequence from a list
    :param sequences:
    :return str:
    """
    longest = ""

    for seq in sequences:
        if len(seq) > len(longest):
            longest = seq

    return longest


def main():
    # 1. Ask user for filename
    filename = input("Enter filename: ")

    # 2. Read all sequences from file
    sequences = read_sequences_from_file(filename)

    # 3. Check if file had any sequences
    if len(sequences) == 0:
        print("Error: No sequences found in file!")
        return

    # 4. Analyze each sequence
    print(f"\nAnalyzing {len(sequences)} sequences...\n")

    for i, sequence in enumerate(sequences, 1):
        print(f"Sequence {i}: {sequence}")

        # Check if valid
        if not is_valid_dna(sequence):
            print("  ERROR: Invalid DNA sequence!")
            continue

        # Calculate statistics
        counts = count_nucleotides(sequence)
        gc = calculate_gc_content(sequence)
        complement = find_complement(sequence)

        # Print results
        print(f"  Length: {len(sequence)}")
        print(f"  A: {counts['A']}, T: {counts['T']}, G: {counts['G']}, C: {counts['C']}")
        print(f"  GC content: {gc:.1f}%")
        print(f"  Complement: {complement}")
        print()

    # 5. Calculate summary statistics
    total_sequences = len(sequences)
    avg_length = sum(len(seq) for seq in sequences) / total_sequences

    print("=" * 50)
    print("SUMMARY")
    print("=" * 50)
    print(f"Total sequences: {total_sequences}")
    print(f"Average length: {avg_length:.1f}")

    longest = find_longest_sequence(sequences)
    print(f"Longest sequence length: {len(longest)}")

    # 6. Save results to file
    with open("results.txt", "w") as f:
        f.write("DNA Sequence Analysis Results\n")
        f.write("=" * 50 + "\n")
        f.write(f"Total sequences analyzed: {total_sequences}\n")
        f.write(f"Average length: {avg_length:.1f}\n")
        f.write(f"Longest sequence length: {len(longest)}\n")


if __name__ == "__main__":
    main()
