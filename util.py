import html
import os
import re
from os import environ

from google.cloud import translate

PATH_l10n = '/path/to/your/project/lib/translations folder'

environ.setdefault('GOOGLE_APPLICATION_CREDENTIALS', 'dat/key.json')

client = translate.TranslationServiceClient()
project_id = 'your-project-id-from-gcp'
parent = f"projects/{project_id}"
data = open('dat/input.txt').read()
arr = data.split(',\n')


def translate_text_from_input(target):
    """
    Translates data int dat/input.txt file
    :param target: Language to translate into
    :return: A tuple of translated text and array of strings from dat/input.txt
    """
    content = [re.split(': *', e)[1][1:-1] for e in arr]
    return (client.translate_text(contents=content,
                                  target_language_code=target,
                                  source_language_code='en', parent=parent), arr)


def write_to_output(translations, array, capitalize):
    """
    Writes translations to dat/output.txt file
    :param translations: Array of translation objects
    :param array: Array of strings from dat/input.txt
    :param capitalize: Set True if you want to capitalize each word of translated string
    """
    out = open('dat/output.txt', mode='w')
    stop = len(translations)
    for i in range(stop):
        line = array[i]
        k = re.split(': *', line)[0]
        translated_text = translations[i].translated_text
        if capitalize:
            if ' ' in translated_text:
                str_arr = translated_text.split(' ')
                translated_text = ''
                end = len(str_arr)
                for j in range(end):
                    s = str_arr[j]
                    translated_text += s.capitalize() + (' ' if j < end - 1 else '')
            else:
                translated_text = translated_text.capitalize()

        out.write(k + ':"' + html.unescape(translated_text) + '"' + (',\n' if i < stop - 1 else ''))


def append_to_arb_file(translations, array, path, capitalize):
    """
    Appends translations to each of app_*.arb file of a Flutter project.
    :param translations: Array of translation objects
    :param array: Array of strings from dat/input.txt
    :param path: A path of a file to append to.
    :param capitalize: Set True if you want to capitalize each word of translated string
    """
    out = open(path, mode='a+')
    out.seek(0, os.SEEK_END)
    pos = out.tell() - 1
    while pos > 0 and out.read(1) != '\n':
        pos -= 1
        out.seek(pos, os.SEEK_SET)
    if pos > 0:
        out.seek(pos, os.SEEK_SET)
        out.truncate()
    out.write(',\n')
    stop = len(translations)
    for i in range(stop):
        line = array[i]
        k = re.split(': *', line)[0]
        translated_text = translations[i].translated_text
        if capitalize:
            if ' ' in translated_text:
                str_arr = translated_text.split(' ')
                translated_text = ''
                end = len(str_arr)
                for j in range(end):
                    s = str_arr[j]
                    translated_text += s.capitalize() + (' ' if j < end - 1 else '')
            else:
                translated_text = translated_text.capitalize()

        out.write(k + ':"' + html.unescape(translated_text) + '"' + (',\n' if i < stop - 1 else '\n}'))
