import rename.rename.sort as sort


def parse_episode(episode, new_name):
    episode = sort.sort_episode(episode)

    return f'{new_name} {episode}'


def parse_series(series, new_name):
    series = sort.sort_series(series)

    return f'{new_name} {series}'


def parse_movie(name, year):
    movie = sort.sort_movie_name(name)

    return f'{movie} ({year})'
