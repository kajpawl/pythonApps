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
    cmd = None
    journal_data = []

    while cmd != 'x':
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
        elif cmd != 'x':
            print('Sorry, we don\'t understand {}'.format(cmd))

    print('Done, goodbye.')


def print_entries(data):
    if len(data) == 0:
        print('The journal contains no items.')
    else:
        for index, item in enumerate(data):
            print(f'{index + 1}. {item}')


def add_entry(data):
    new_item = input('Type new entry: ')
    data.append(new_item)
    print('Item \'{}\' added to journal.'.format(new_item))


def update_entry(data):
    updated_number = int(input(f'Which entry do you wish to update? [1 - {len(data)}] '))
    updated_entry = input('Enter updated task: ')
    data[updated_number - 1] = updated_entry
    print(f'Entry {updated_number} updated.')


def remove_entry(data):
    deleted_number = int(input(f'Which entry do you want to remove? [1 - {len(data)}]  '))
    data.pop(deleted_number - 1)
    print(f'Entry {deleted_number} deleted.')


main()
