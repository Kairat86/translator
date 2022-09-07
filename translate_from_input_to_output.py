from util import write_to_output, translate_text_from_input

text = translate_text_from_input('sq')
write_to_output(text.translations, False)
