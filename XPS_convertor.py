import os
import pandas as pd

def convert_csv_to_xlsx(directory):
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            csv_file_path = os.path.join(directory, filename)
            # Create the new filename by appending "_xlsx"
            xlsx_file_path = os.path.join(directory, filename.replace(".csv", "_xlsx.xlsx"))
            
            # Read the CSV file
            csv_data = pd.read_csv(csv_file_path)
            
            # Save the data to an XLSX file
            csv_data.to_excel(xlsx_file_path, index=False)
            
            # Optional: Remove the original CSV file
            os.remove(csv_file_path)
            
            print(f"Converted {filename} to {xlsx_file_path}")

# Replace '<Local Path>' with the actual path to your directory
convert_csv_to_xlsx('<Local Path>')
