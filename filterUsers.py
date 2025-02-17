import csv

input_file = 'appUserExport.csv'
output_file = 'filteredUsers.csv'

with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for row in reader:
        if int(row['numberOfConversations']) > 1: # can be changed to another header
            writer.writerow(row)