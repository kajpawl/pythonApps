import os


def load(name):
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as file_in:
            for entry in file_in.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    filename = get_full_pathname(name)
    print('...saving to: {}'.format(filename))

    with open(filename, 'w') as file_out:
        for entry in journal_data:
            file_out.write(entry + '\n')


def get_full_pathname(name):
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.txt'))
    return filename


def add_entry(journal_data, text):
    journal_data.append(text)


def update_entry(journal_data, index, text):
    journal_data[index] = text


def delete_entry(journal_data, index):
    return journal_data.pop(index)
