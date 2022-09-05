# Flutter project strings translator

This utility allows you to translate Flutter strings into any Google Translate API supported language.

## Setup
You must set up a project on GCP, enable translate API and get your key.json. 
See [Google Codelab](https://codelabs.developers.google.com/codelabs/cloud-translation-python3)

## translate_from_input_to_output.py
This script translates data in input.txt and puts it in output.txt. Input data format:

```text
"hello":"Hello World!", // each line must end with a comma
"flutter": "Flutter is wonderful" //no comma in the end of the last line
```


## translate_and_append_from_input.py
This script translates data in input.txt and appends it to app_*.arb files.
