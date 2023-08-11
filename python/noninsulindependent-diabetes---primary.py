# Anthony Mathews, Emily Herret, Antonio Gassparrini, Tjeerd Van Staa, Ben Goldacre, Liam Smeeth, Krishnan Bhaskaran, 2023.

import sys, csv, re

codes = [{"code":"66Ap.00","system":"readv2"},{"code":"66Ar.00","system":"readv2"},{"code":"66Aw.00","system":"readv2"},{"code":"C100011","system":"readv2"},{"code":"C100112","system":"readv2"},{"code":"C108.00","system":"readv2"},{"code":"C108.11","system":"readv2"},{"code":"C108600","system":"readv2"},{"code":"C108700","system":"readv2"},{"code":"C108800","system":"readv2"},{"code":"C108900","system":"readv2"},{"code":"C108D00","system":"readv2"},{"code":"C108E00","system":"readv2"},{"code":"C108H00","system":"readv2"},{"code":"C109.00","system":"readv2"},{"code":"C109500","system":"readv2"},{"code":"C109600","system":"readv2"},{"code":"C109700","system":"readv2"},{"code":"C109C00","system":"readv2"},{"code":"C109D00","system":"readv2"},{"code":"C109G00","system":"readv2"},{"code":"C10E.12","system":"readv2"},{"code":"C10E712","system":"readv2"},{"code":"C10E812","system":"readv2"},{"code":"C10E912","system":"readv2"},{"code":"C10ED12","system":"readv2"},{"code":"C10EE12","system":"readv2"},{"code":"ZRbH.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diabetes-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["noninsulindependent-diabetes---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["noninsulindependent-diabetes---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["noninsulindependent-diabetes---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)