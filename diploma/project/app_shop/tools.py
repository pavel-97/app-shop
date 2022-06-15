from transliterate import translit, detect_language


def make_slug(title):
    language = detect_language(title)
    slug = title

    if language == 'ru':
        slug = translit(title, 'en')

    return '-'.join(slug.lower().replace('\'', '').replace('\"', '').split())


def get_dict_characteristics(other_characteristics):
    result = dict()
    for line in other_characteristics.split('\n'):
        key, value = line.split(':')
        result[key] = value
    return result