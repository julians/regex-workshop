#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import csv
from operator import itemgetter

def main (argv):
    with open("Daten/stage_times.csv") as input_file:
        rows = csv.DictReader(input_file, delimiter=',')

        year_and_stage = re.compile(r"^Tour de France (\d{4}).*Stage\s*(\d{1,2}[ab]*)")

        stages = []
        for row in rows:
            if len(row["Speed"]) and len(row["Distance"]):
                results = year_and_stage.search(row["Stage"])
                if results:
                    stages.append({
                        "year": results.group(1),
                        "stage": results.group(2),
                        "speed": row["Speed"].replace(",", "."),
                        "distance": row["Distance"].replace(",", "."),
                        "kind": row["Event"]
                    })

    with open("stages.csv", "wb") as output_file:
        csv_writer = csv.DictWriter(output_file, stages[0].keys(), delimiter=",")
        csv_writer.writeheader()
        csv_writer.writerows(sorted(stages, key=itemgetter("year", "stage")))
        
if __name__ == "__main__":
    main(sys.argv[1:])