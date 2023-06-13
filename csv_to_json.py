import pandas as pd

def csv_to_json(csv_file, json_file):
    df = pd.read_csv(csv_file)
    df.to_json(json_file, orient='records', indent=4)

# Specify the file paths for the CSV input and JSON output
csv_file = 'mergedRupeeRem.csv'
json_file = 'final.json'

# Call the function to convert CSV to JSON
csv_to_json(csv_file, json_file)

print("Converted Successfully")