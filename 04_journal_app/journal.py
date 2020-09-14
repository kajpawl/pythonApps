def load(name):
    # TODO: add loading from file
    return []


def save(name, data):
    # TODO: add saving to file
    pass


def add_entry(journal_data, text):
    journal_data.append(text)


def update_entry(journal_data, index, text):
    journal_data[index] = text


def delete_entry(journal_data, index):
    return journal_data.pop(index)
