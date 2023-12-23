import csv
import json
import pickle
import xml.etree.ElementTree as ET

class FileProcessor:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = None

    def read(self):
        pass

    def save_to_pickle(self, pickle_file):
        with open(pickle_file, 'wb') as pkl_file:
            pickle.dump(self.data, pkl_file)

class CSVProcessor(FileProcessor):
    def read(self):
        data = []
        with open(self.file_name, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            headers = next(csv_reader)
            for row in csv_reader:
                data.append(row)
        self.data = {'headers': headers, 'data': data}

class JSONProcessor(FileProcessor):
    def read(self):
        with open(self.file_name, 'r') as json_file:
            self.data = json.load(json_file)


class XMLProcessor(FileProcessor):
    def read(self):
        tree = ET.parse(self.file_name)
        root = tree.getroot()
        data = []
        for item in root.findall('.//item'):
            item_data = {}
            for child in item:
                item_data[child.tag] = child.text
            data.append(item_data)
        self.data = data

file_name = 'sales.csv'

pickle_file = 'data.pickle'

if file_name.endswith('.csv'):
    processor = CSVProcessor(file_name)
elif file_name.endswith('.json'):
    processor = JSONProcessor(file_name)
elif file_name.endswith('.xml'):
    processor = XMLProcessor(file_name)
else:
    raise ValueError("Unsupported file format")

processor.read()

processor.save_to_pickle(pickle_file)

print(f"Data from '{file_name}' has been stored in '{pickle_file}' as a pickle file.")
