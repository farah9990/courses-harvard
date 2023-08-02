import csv
import sys


def main():

    db = sys.argv[1] 
    seq = sys.argv[2]
    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    # TODO: Read database file into a variable
    data = []
    with open(db, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    # TODO: Read DNA sequence file into a variable
    with open(seq, "r") as file:
        sequence = file.read()

    # TODO: Find longest match of each STR in DNA sequence
    subs = list(data[0].keys())[1:]
    result = {}
    for sub in subs:
        result[sub] = longest_match(sequence, sub)
    # TODO: Check database for matching profiles
    for person in data:
        match = 0
        for sub in subs:
            if int(person[sub]) == result[sub]:
                match += 1
        if match == len(subs):
            print(person["name"])
            sys.exit(0)
    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
