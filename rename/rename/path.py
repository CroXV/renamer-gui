from rename.rename import config
import os
import sys


def get_path():
    path = config.get('dir')
    if path:
        print(f'\nIs your directory: {path}\nPress (Y/N) to continue...')
        while True:
            directory = input('> ').lower()

            if directory == 'y':
                break
            elif directory == 'n':
                path = set_directory()
                break
            elif directory == 'q':
                sys.exit()
    else:
        path = set_directory()

    return path


def set_directory():
    print('\nEnter directory:')

    while True:
        path = input('> ')
        if os.path.isdir(path) and path != '\\' and path != '/':
            break
        elif path.lower() == 'q':
            config.del_value('dir')
            config.update()
            sys.exit()
        else:
            print(f'{path} is not a directory.\n')

    config.set('dir', path)
    config.update()

    return path
