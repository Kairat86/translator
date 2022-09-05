from util import write_to_output, translate_text_from_input

(text, arr) = translate_text_from_input('kk')
write_to_output(text.translations, arr, False)
