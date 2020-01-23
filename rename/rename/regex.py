import rename.rename.parser as parser
import re
import os


def regex_name(name, item, new_name):
    split = os.path.splitext(name)
    name, ext = split

    if ext == 'srt' and item.lower() != 'subtitles':
        raise ReferenceError

    anime = re.compile(r'ep(isode)?[-.(_\s]+?(\d+)', re.I).search(name)
    digits = re.compile(r'^\d+$').search(name)
    series = re.compile(r'([se]\d?\d[-.(_\s]?[se]\d?\d)', re.I).search(name)
    movie = re.compile(r'(.*?)[-.(_\s](?!1[0-7]\d{2}|\d{4}p)([12]\d{3})').search(name)

    # if it's a file, do (series, anime, digits, movie parsing)
    # if it's a folder, do (movie parsing)
    if anime and item.lower() in 'animes' and ext:
        return f'{parser.parse_episode(anime.group(2), new_name)}{ext}'
    elif digits and item.lower() == 'animes' and ext:
        return f'{parser.parse_episode(digits.group(), new_name)}{ext}'
    elif series and item.lower() == 'tv shows' and ext:
        return f'{parser.parse_series(series.group(), new_name)}{ext}'
    elif movie and item.lower() == 'movies':
        return f'{parser.parse_movie(movie.group(1), movie.group(2))}{ext}'
    else:
        # return f'{name}{ext}'
        raise ReferenceError