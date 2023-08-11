# Anthony Mathews, Emily Herret, Antonio Gassparrini, Tjeerd Van Staa, Ben Goldacre, Liam Smeeth, Krishnan Bhaskaran, 2023.

import sys, csv, re

codes = [{"code":"2G5H.00","system":"readv2"},{"code":"2G5L.00","system":"readv2"},{"code":"2G5V.00","system":"readv2"},{"code":"2G5W.00","system":"readv2"},{"code":"C108500","system":"readv2"},{"code":"C108511","system":"readv2"},{"code":"C108512","system":"readv2"},{"code":"C109400","system":"readv2"},{"code":"C109411","system":"readv2"},{"code":"C109412","system":"readv2"},{"code":"C10E500","system":"readv2"},{"code":"C10E511","system":"readv2"},{"code":"C10E512","system":"readv2"},{"code":"C10F400","system":"readv2"},{"code":"C10F411","system":"readv2"},{"code":"M271000","system":"readv2"},{"code":"M271100","system":"readv2"},{"code":"M271200","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diabetes-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["diabetes-ulcerated---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["diabetes-ulcerated---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["diabetes-ulcerated---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
