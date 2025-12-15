#!/bin/bash

# Check if input folder was provided
if [ $# -eq 0 ]; then
    echo "Error: Please provide input folder"
    echo "Usage: ./organize_sequences.sh input_folder/"
    exit 1
fi

INPUT_DIR="$1"

# Check if folder exists
if [ ! -d "$INPUT_DIR" ]; then
    echo "Error: Folder $INPUT_DIR does not exist"
    exit 1
fi

# Create output folders
mkdir -p "$INPUT_DIR/small" "$INPUT_DIR/medium" "$INPUT_DIR/large"

# Initialize counters
total_files=0
small_count=0
medium_count=0
large_count=0
total_sequences=0

# Loop through all .txt files
for file in "$INPUT_DIR"/*.txt; do
    # Count sequences (lines starting with '>')
    seq_count=$(grep -c "^>" "$file")
    # Get filename without path
    filename=$(basename "$file")
    # Print file info
    echo "$filename: $seq_count sequences"

    # Update total counters
    total_files=$((total_files + 1))
    total_sequences=$((total_sequences + seq_count))

    # Determine which folder to use and move the file
    if [ "$seq_count" -ge 1 ] && [ "$seq_count" -le 5 ]; then
        mv "$file" "$INPUT_DIR/small/"
        small_count=$((small_count + 1))

    elif [ "$seq_count" -ge 6 ] && [ "$seq_count" -le 10 ]; then
        mv "$file" "$INPUT_DIR/medium/"
        medium_count=$((medium_count + 1))

    else
        mv "$file" "$INPUT_DIR/large/"
        large_count=$((large_count + 1))
    fi

done

# Create summary file
summary_file="$INPUT_DIR/summary.txt"

echo "Total files processed: $total_files" > "$summary_file"
echo "Small category (1-5 sequences): $small_count files" >> "$summary_file"
echo "Medium category (6-10 sequences): $medium_count files" >> "$summary_file"
echo "Large category (>10 sequences): $large_count files" >> "$summary_file"
echo "Total sequences across all files: $total_sequences" >> "$summary_file"

echo "Input folder exists: $INPUT_DIR"

