import os
import pandas as pd

folder_path = 'C:/Users/user/Downloads/AAAAZZZZ'
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path, header=None)
        
        if not df.empty:
            new_filename = df.iloc[1, 0] + '-' + df.iloc[-1, 0] + '-' + str(len(df)) + '.csv'
            new_file_path = os.path.join(folder_path, new_filename)
            os.rename(file_path, new_file_path)