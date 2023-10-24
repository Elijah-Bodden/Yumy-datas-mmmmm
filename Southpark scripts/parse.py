# Script courtesy of the ever-tasty chatgpt

import csv

# Define the input and output file names
input_file = "./southpark/All-seasons.csv"
output_file = "./southpark/out.txt"

# Open the input CSV file for reading and the output text file for writing
with open(input_file, 'r', newline='', encoding='utf-8') as csv_file, open(output_file, 'w', encoding='utf-8') as txt_file:
    # Create a CSV reader
    csv_reader = csv.reader(csv_file)

    # Iterate through the rows in the CSV file
    for row in csv_reader:
        character_name = row[-2].upper()  # Convert the character name to all caps
        line = row[-1]
        
        # Write the formatted line to the output text file
        txt_file.write(f"{character_name}: {line}\n")

# Close the files
csv_file.close()
txt_file.close()