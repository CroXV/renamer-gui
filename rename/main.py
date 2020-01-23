from rename.rename.database import NoNameError
from rename.rename.walk import walk_dir
# from rename.rename.path import get_path
from rename.rename import db
import os
import sys


def renamer(instance, rename_items):
    # print(files)
    file = None
    for item, files in rename_items.items():
        if files:
            file = True
            for old_filename, new_filename in files.items():
                os.rename(old_filename, new_filename)
    if file:
        instance.files = {}
        instance.text_browser_print('Done.\n')
    else:
        instance.text_browser_print('No Items to Rename.')
    # while True:
    #     confirm = input('> ').lower()
    #
    #     if confirm == 'q' or confirm == 'n':
    #         print('\nClosing script...')
    #         sys.exit()
    #     elif confirm == 'y':
    #         for k, v in db.database.items():
    #             os.rename(k, v)
    #         print('\nDone')
    #         break


def start_main(instance, rename_items):
    directory = instance.dir_line.text()

    instance.text_browser_print('\nRenaming:')
    try:
        files = {}
        for item in rename_items:
            # Write to text browser the item it is working on
            instance.text_browser_print(f'\t[{item}]')
            walk_dir(directory, item, rename_items[item])
            db.print_database(instance)
            files[item] = db.database   # add database to files
            db.database = {}    # make database empty
            instance.text_browser_print('')
        return files
    except NoNameError as err:
        pass


if __name__ == '__main__':
    start_main()
