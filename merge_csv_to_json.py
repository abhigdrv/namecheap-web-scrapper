import pandas as pd
import os
import json

csv_directory = 'C:/Users/user/Downloads/AAAAZZZZ'
output_file = './output.json'
merged_csv_path = './mergedRupee.csv'
merged_data = []
for filename in os.listdir(csv_directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(csv_directory, filename)
        data = pd.read_csv(file_path)
        merged_data.append(data)
merged_csv = pd.concat(merged_data)
merged_csv.to_csv(merged_csv_path, index=False)
# json_data = merged_csv.to_json(orient='records')
# with open(output_file, 'w') as outfile:
#     json.dump(json_data, outfile)
print("All data saved successfully")