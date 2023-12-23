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

    @staticmethod
    def detect_file_type(file_name):
        if '.csv' in file_name:
            return 'csv'
        elif '.json' in file_name:
            return 'json'
        elif '.xml' in file_name:
            return 'xml'
        elif '.txt' in file_name:
            return 'txt'
        elif '.bin' in file_name:
            return 'bin'
        else:
            raise ValueError("Unsupported file format")

    @staticmethod
    def process_file(file_type, file_name):
        processors = {
            'csv': CSVProcessor,
            'json': JSONProcessor,
            'xml': XMLProcessor,
            'txt': TXTProcessor,
            'bin': BinaryProcessor,
        }

        processor_class = processors.get(file_type)
        if processor_class:
            processor = processor_class(file_name)
            processor.read()
            return processor
        else:
            raise ValueError("Unsupported file type")            

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

class TXTProcessor(FileProcessor):
    def read(self):
        with open(self.file_name, 'r') as txt_file:
            data = txt_file.read()
            self.data = {'text_data': data}

class BinaryProcessor(FileProcessor):
    def read(self):
        with open(self.file_name, 'rb') as bin_file:
            data = bin_file.read()
            self.data = {'binary_data': data}        


def get_file_input():
    file_path = input("Enter the file path: ")
    return file_path

def main():
    file_path = get_file_input()

    try:
        file_type = FileProcessor.detect_file_type(file_path)
        processor = FileProcessor.process_file(file_type, file_path)
        pickle_file = 'data.pickle'
        processor.save_to_pickle(pickle_file)
        print(f"Data from '{file_path}' has been stored in '{pickle_file}' as a pickle file.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
