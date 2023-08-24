import random, csv

def lookup_itsm_csat(case_number):
    print("making API call to IT Service Management System for case {}".format(str(case_number)))
    print("Gathering CSAT Score")
    return random.randint(0, 5)

def build_csv_report(case_numbers, csat_list, region, year, quarter):
    csv_file = "csat_report_fy{}q{}_{}.csv".format(str(year), str(quarter), region)
    try:
        with open(csv_file, "w") as csv_file:
            writer = csv.DictWriter(
                csv_file, fieldnames=["case_number", "csat"]
            )
            writer.writeheader()
            # this could be written in a loop, but writing this way for simplicity
            writer.writerow({'case_number': case_numbers[0], 'csat': csat_list[0]})
            writer.writerow({'case_number': case_numbers[1], 'csat': csat_list[1]})
            writer.writerow({'case_number': case_numbers[2], 'csat': csat_list[2]})
            writer.writerow({'case_number': case_numbers[3], 'csat': csat_list[3]})
    except IOError:
        print("I/O error")