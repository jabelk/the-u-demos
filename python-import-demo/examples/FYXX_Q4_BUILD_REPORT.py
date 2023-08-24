#!/usr/bin/python3
from shared_resources import lookup_itsm_csat, build_csv_report

if __name__ == "__main__":
    csat_list = []
    case_numbers = [1241, 1234, 6453, 3453]
    print("building report")
    print("looking up CSAT scores using API for case numbers in IT Service Management System")
    for case_num in case_numbers:
        # add csat to dictionary for case number 
        csat = lookup_itsm_csat(case_num)
        csat_list.append(csat)
        print("csat for {} is {}".format(str(case_num), str(csat)))
    build_csv_report(case_numbers=case_numbers, csat_list=csat_list, region="emea", year="2023", quarter="4")
