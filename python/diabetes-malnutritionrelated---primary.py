# Anthony Mathews, Emily Herret, Antonio Gassparrini, Tjeerd Van Staa, Ben Goldacre, Liam Smeeth, Krishnan Bhaskaran, 2023.

import sys, csv, re

codes = [{"code":"2BBF.00","system":"readv2"},{"code":"2G51000","system":"readv2"},{"code":"2G5C.00","system":"readv2"},{"code":"C10A.00","system":"readv2"},{"code":"C10A000","system":"readv2"},{"code":"C10A100","system":"readv2"},{"code":"C10A500","system":"readv2"},{"code":"C10N100","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diabetes-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["diabetes-malnutritionrelated---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["diabetes-malnutritionrelated---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["diabetes-malnutritionrelated---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
