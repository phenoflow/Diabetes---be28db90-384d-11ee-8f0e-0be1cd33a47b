# Anthony Mathews, Emily Herret, Antonio Gassparrini, Tjeerd Van Staa, Ben Goldacre, Liam Smeeth, Krishnan Bhaskaran, 2023.

import sys, csv, re

codes = [{"code":"C100.00","system":"readv2"},{"code":"C100000","system":"readv2"},{"code":"C100100","system":"readv2"},{"code":"C100z00","system":"readv2"},{"code":"C104y00","system":"readv2"},{"code":"C105y00","system":"readv2"},{"code":"C106y00","system":"readv2"},{"code":"C108000","system":"readv2"},{"code":"C108011","system":"readv2"},{"code":"C108012","system":"readv2"},{"code":"C108100","system":"readv2"},{"code":"C108112","system":"readv2"},{"code":"C108200","system":"readv2"},{"code":"C108211","system":"readv2"},{"code":"C108212","system":"readv2"},{"code":"C108300","system":"readv2"},{"code":"C108A00","system":"readv2"},{"code":"C108A11","system":"readv2"},{"code":"C108y00","system":"readv2"},{"code":"C108z00","system":"readv2"},{"code":"C109000","system":"readv2"},{"code":"C109011","system":"readv2"},{"code":"C109012","system":"readv2"},{"code":"C109100","system":"readv2"},{"code":"C109111","system":"readv2"},{"code":"C109112","system":"readv2"},{"code":"C109200","system":"readv2"},{"code":"C109211","system":"readv2"},{"code":"C109212","system":"readv2"},{"code":"C109300","system":"readv2"},{"code":"C109900","system":"readv2"},{"code":"C10E000","system":"readv2"},{"code":"C10E012","system":"readv2"},{"code":"C10E100","system":"readv2"},{"code":"C10E111","system":"readv2"},{"code":"C10E112","system":"readv2"},{"code":"C10E200","system":"readv2"},{"code":"C10E212","system":"readv2"},{"code":"C10E300","system":"readv2"},{"code":"C10E311","system":"readv2"},{"code":"C10E312","system":"readv2"},{"code":"C10EA00","system":"readv2"},{"code":"C10EA11","system":"readv2"},{"code":"C10EA12","system":"readv2"},{"code":"C10F000","system":"readv2"},{"code":"C10F011","system":"readv2"},{"code":"C10F100","system":"readv2"},{"code":"C10F111","system":"readv2"},{"code":"C10F200","system":"readv2"},{"code":"C10F211","system":"readv2"},{"code":"C10F300","system":"readv2"},{"code":"C10F311","system":"readv2"},{"code":"C10F900","system":"readv2"},{"code":"C10F911","system":"readv2"},{"code":"C10N000","system":"readv2"},{"code":"C10yy00","system":"readv2"},{"code":"C10z.00","system":"readv2"},{"code":"C10z000","system":"readv2"},{"code":"C10z100","system":"readv2"},{"code":"C10zy00","system":"readv2"},{"code":"C10zz00","system":"readv2"},{"code":"Cyu2300","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diabetes-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["diabetes-complicatn---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["diabetes-complicatn---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["diabetes-complicatn---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
