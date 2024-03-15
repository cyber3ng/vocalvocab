import csv


def process_csv(csv_file_path):
    entries = []
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            entries.append(row)
    return entries # a list of dicts (each row)
