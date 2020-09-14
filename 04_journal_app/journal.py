"""
This is a journal module.
"""
import os


def load(name):
    """
    This method creates and loads a new journal.

    :param name: This is a base name of a journal to load.
    :return: A new journal data structure populated with the file data.
    """
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as file_in:
            for entry in file_in.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    """
    This method is used to save a journal.

    :param name: This is a base name of a journal to save.
    :param journal_data: This is a list with the contents of the journal.
    """
    filename = get_full_pathname(name)
    print('...saving to: {}'.format(filename))

    with open(filename, 'w') as file_out:
        for entry in journal_data:
            file_out.write(entry + '\n')


def get_full_pathname(name):
    """
    This method gets full pathname used to load and save files.

    :param name: This is a name of the file to be saved.
    :return: Full path to the file that was saved or loaded.
    """
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.txt'))
    return filename


def add_entry(journal_data, text):
    """
    This method appends the journal data with the entry provided.

    :param journal_data: A list with all journal entries.
    :param text: New entry added to journal_data list
    """
    journal_data.append(text)


def update_entry(journal_data, index, text):
    """
    This method replaces a journal_entry at given index with the text provided as param.

    :param journal_data: A list with all journal entries.
    :param index: Index of an updated entry.
    :param text: String with a new value for an updated entry.
    """
    journal_data[index] = text


def delete_entry(journal_data, index):
    """
    This method deletes an entry at given index from journal_data list.

    :param journal_data: A list with all journal entries.
    :param index: Index of an entry to be removed.
    """
    return journal_data.pop(index)
