import csv
import os

try:
    import statistics
except:
    # error code instead
    import statistics_standin_for_py2 as statistics

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
    with open(filename, 'r') as file_in:
    # with open(filename, 'r', encoding='utf-8') as file_in:
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
    # prices = []
    # for purchase in data:
    #     prices.append(purchase.price)

    prices = (
        # (p.price, p.beds, p.city)  # projection or items
        p.price  # projection or items
        for p in data  # the set to process
    )

    average_price = statistics.mean(prices)
    print('The average home price is ${:,}'.format(int(average_price)))

    # average price of 2 bedroom houses
    # prices = []
    # for purchase in data:
    #     if purchase.beds == 2:
    #         prices.append(purchase.price)

    # prices = [
    #     p.price  # projection or items
    #     for p in data  # the set to process
    #     if p.beds == 2  # test/condition
    # ]

    two_bed_homes = (
        p  # projection or items                -> projection
        for p in data  # the set to process     -> source
        if p.beds == 2  # test/condition        -> filter
    )

    homes = []
    for h in two_bed_homes:
        if len(homes) > 5:
            break
        homes.append(h)

    average_price = statistics.mean((p.price for p in homes))
    average_baths = statistics.mean((p.baths for p in homes))
    average_sq_ft = statistics.mean((p.sq__ft for p in homes))
    print('The average price of a 2-bedroom home is ${:,}, baths: {}, sq ft: {}'.format(
        int(average_price), round(average_baths, 1), round(average_sq_ft, 1)))


if __name__ == '__main__':
    main()
