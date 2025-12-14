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

echo "Input folder exists: $INPUT_DIR"

