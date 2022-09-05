import re
from os import listdir

from util import translate_text_from_input, append_to_arb_file, PATH_l10n

nameArr = listdir(PATH_l10n)
filtered = list(filter(lambda n: bool(re.match(r'^app_(?!en)[a-z]{2}\.arb$', n)), nameArr))
for name in filtered:
    target = re.split('[_.]', name)[1]
    (text, arr) = translate_text_from_input(target)
    append_to_arb_file(text.translations, arr, PATH_l10n + name, False)
