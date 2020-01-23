from rename.rename import db
from rename.rename import config
from rename.rename.regex import regex_name
from rename.rename.settings.app_descriptor import EmptyStringError
import os


def walk_dir(directory, item, new_name):
    """Go through all files in folder and store them in database with a new name."""
    # if walk:
    #     for foldername, subfolders, files in os.walk(directory):
    #         # save current folder name to database
    #         db.set('foldername', foldername)
    #
    #         try:
    #             for file in files:
    #                 name = regex_name(file)
    #                 filename = os.path.join(foldername, file)
    #                 new_filename = os.path.join(foldername, name)
    #
    #                 db.add(filename, new_filename)
    #             config.del_value('name')
    #         except (TypeError, EmptyStringError):
    #             config.del_value('name')
    #
    #         for subfolder in subfolders:
    #             name = regex_name(subfolder)
    #             subfolder = os.path.join(foldername, subfolder)
    #             new_subfolder = os.path.join(foldername, name)
    #
    #             db.set('foldername', subfolder)
    #             db.add(subfolder, new_subfolder)
    for file in os.listdir(directory):
        db.set('foldername', directory)

        filename = os.path.join(directory, file)
        if os.path.isfile(filename):
            try:
                name = regex_name(file, item, new_name)
                new_filename = os.path.join(directory, name)
                db.add(filename, new_filename)
            except ReferenceError:
                pass

    db.del_value('foldername')
    db.update()