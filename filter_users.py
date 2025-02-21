import csv
import sys
import argparse

parser = argparse.ArgumentParser(description='Filter users based on number of conversations.')
parser.add_argument('--row', type=str, required=True, help='numberOfConversations')
parser.add_argument('--input', type=str, required=True, help='appUsers.csv')
parser.add_argument('--output', type=str, required=True, help='filteredUsers.csv')
args = parser.parse_args()

row_to_filter = args.row
input_file = args.input
output_file = args.output

with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for row in reader:
        if int(row[row_to_filter]) > 1: # can be changed to another header
            writer.writerow(row)