import os


def load(name):
    # TODO: add loading from file
    return []


def save(name, journal_data):
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.txt'))
    # filename = os.path.join('.', 'journals', name + '.txt')
    print('...saving to: {}'.format(filename))

    # file_out = open(filename, 'w')
    with open(filename, 'w') as file_out:

        for entry in journal_data:
            file_out.write(entry + '\n')

    # file_out.close()


def add_entry(journal_data, text):
    journal_data.append(text)


def update_entry(journal_data, index, text):
    journal_data[index] = text


def delete_entry(journal_data, index):
    return journal_data.pop(index)
