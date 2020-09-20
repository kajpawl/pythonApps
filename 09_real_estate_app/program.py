import csv
import os


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    print(data)
    query_data(data)


def print_header():
    print('---------------------------------------')
    print('      REAL ESTATE DATA MINING APP')
    print('---------------------------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data',
                        'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as file_in:
        reader = csv.DictReader(file_in)
        for row in reader:
            print(type(row), row)
            print('Bed count: {}'.format(row['beds']))


# def load_file_basic(filename):
#     with open(filename, 'r', encoding='utf-8') as file_in:
#         header = file_in.readline()
#         print('found header: ' + header.strip())
#
#         lines = []
#         for line in file_in:
#             line_data = line.strip().split(',')
#             bed_count = line_data[4]
#             lines.append(line_data)
#
#         print(lines[:5])


def query_data(data):
    pass


if __name__ == '__main__':
    main()
