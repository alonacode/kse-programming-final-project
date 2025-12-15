# Bioinformatics Programming – Final Project

## Project 1: DNA Sequence File Organizer (BASH)

### How to run
```bash
chmod +x organize_sequences.sh
./organize_sequences.sh data
```
The script processes FASTA .txt files from the data/ folder, counts sequences
(lines starting with >), and organizes files into small, medium, and large
folders. A summary.txt file is created with total counts.

The test_output/ folder contains a copy of the results after running the script
on the provided sample files.


## Project 2: DNA Sequence Analyzer (Python)
### How to run
```bash
python3  project2/analyzer.py
```
Enter the name of a test file when prompted (e.g. test_sequences.txt).

The program analyzes DNA sequences, prints statistics to the terminal,
and saves summary results to results.txt.
An additional feature is implemented to find the longest sequence.


