import argparse
from datetime import datetime
import csv
import sys
from collections import defaultdict

# Helper function to parse args
def parse_args():
    parser = argparse.ArgumentParser(
        description="Process borough complaints data within specified date range."
    )

    parser.add_argument("-i", "--input", required=True, type=str, help="Path to input csv file")
    parser.add_argument("-s", "--startdate", required=True, type=str, help="Start date (MM/DD/YYYY)")
    parser.add_argument("-e", "--enddate", required=True, type=str, help="End date (MM/DD/YYYY)")
    parser.add_argument("-o", "--output", type=str, help="Path to output csv file (optional)")
    return parser.parse_args()

# Helper function to parse date format
def parse_date(date_str):
    if not date_str:
        return None
    return datetime.strptime(date_str, "%m/%d/%Y %I:%M:%S %p").date()

def main():
    args = parse_args()
    input_path = args.input
    start_date = datetime.strptime(args.startdate, "%m/%d/%Y").date()
    end_date = datetime.strptime(args.enddate, "%m/%d/%Y").date()

    counts = defaultdict(int) # (complaint_type, borough) -> count

    with open(input_path, 'r', newline="", encoding="utf-8") as csvfile:
        dict_reader = csv.DictReader(csvfile) # Dict
        for line in dict_reader:
            created_date = parse_date(line.get("Created Date"))
            borough = line.get("Borough").strip()
            complaint_type = line.get("Complaint Type").strip()

            if not created_date or not borough or not complaint_type:
                continue

            if start_date <= created_date <= end_date:
                key = (complaint_type, borough) 
                counts[key] += 1

    output_lines = ["complaint type, borough, count\n"]
    for (complaint_type, borough), count in sorted(counts.items()):
        output_lines.append(f"{complaint_type}, {borough}, {count}\n")

    if args.output:
        with open(args.output, 'w', newline="", encoding="utf-8") as outfile: # Output csv file
            outfile.writelines(output_lines)
    else:
        sys.stdout.writelines(output_lines) # Write to terminal

if __name__ == "__main__":
    main()