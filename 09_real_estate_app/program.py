import csv
import os

from data_types import Purchase


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
        purchases = []

        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        return purchases


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


# def get_price(p):
#     return p.price


def query_data(data):
    # if data was sorted by price:
    # data.sort(key=get_price)
    data.sort(key=lambda p: p.price)

    # most expensive house?
    high_purchase = data[-1]
    print('The most expensive house is ${:,} with {} beds and {} baths'.format(
        high_purchase.price, high_purchase.beds, high_purchase.baths))

    # least expensive house?
    low_purchase = data[0]
    print('The least expensive house is ${:,} with {} beds and {} baths'.format(
        low_purchase.price, low_purchase.beds, low_purchase.baths))

    # average price house?
    # average price of 2 bedroom houses
    pass


if __name__ == '__main__':
    main()
