import journal
# from journal import load, save
# from journal import *


def main():
    print_header()
    run_event_loop()


def print_header():
    print('-----------------------')
    print('      JOURNAL APP')
    print('-----------------------')
    print()


def run_event_loop():
    print('What do you want to do with your journal?')
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]dd an entry, [U]pdate an entry, [R]emove an entry, E[x]it... ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            print_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd == 'u':
            update_entry(journal_data)
        elif cmd == 'r':
            remove_entry(journal_data)
        elif cmd != 'x' and cmd:
            print('Sorry, we don\'t understand {}'.format(cmd))

        print()

    print('Done, goodbye.')
    journal.save(journal_name, journal_data)


def print_entries(data):
    # entries = reversed(data)
    if len(data) == 0:
        print('The journal contains no items.')
    else:
        for index, item in enumerate(data):
            print(f'{index + 1}. {item}')


def add_entry(data):
    new_item = input('Type new entry: ').strip()
    if len(new_item):
        journal.add_entry(data, new_item)
        print('Item \'{}\' added to journal.'.format(new_item))
    else:
        print('Please enter an item.')


def update_entry(data):
    if len(data) == 0:
        return print('No items to update.')
    updated_number = int(input(f'Which entry do you wish to update? [1 - {len(data)}] '))

    if updated_number < 1 or updated_number > len(data):
        return print(f'Number out of range: [1 - {len(data)}].')

    updated_entry = input('Enter updated task: ')
    journal.update_entry(data, updated_number - 1, updated_entry)
    print(f'Entry {updated_number} changed to \'{updated_entry}\'.')


def remove_entry(data):
    if len(data) == 0:
        return print('No items to remove.')
    deleted_number = int(input(f'Which entry do you want to remove? [1 - {len(data)}]  '))

    if deleted_number < 1 or deleted_number > len(data):
        return print(f'Number out of range: [1 - {len(data)}].')

    deleted_entry = journal.delete_entry(data, deleted_number - 1)
    print(f'Entry \'{deleted_entry}\' deleted.')


if __name__ == '__main__':
    main()
