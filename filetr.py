import os
import configparser
from translate.module1 import TransLate, LangDetect, CodeLang

def read_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config

def get_file_info(file_path):
    if not os.path.isfile(file_path):
        return None, f"File '{file_path}' not found."

    file_size = os.path.getsize(file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        char_count = len(text)
        word_count = len(text.split())
        sentence_count = len(text.split('.'))

    detected_lang = LangDetect(text, 'lang')
    return text, f"File '{file_path}', Size: {file_size} bytes, Characters: {char_count}, Words: {word_count}, Sentences: {sentence_count}, Language: {detected_lang}"

def get_text_chunk(text, max_chars, max_words, max_sentences):
    char_count = 0
    word_count = 0
    sentence_count = 0
    chunk = ''

    for sentence in text.split('.'):
        sentence = sentence.strip() + '.'
        new_char_count = char_count + len(sentence)
        new_word_count = word_count + len(sentence.split())
        new_sentence_count = sentence_count + 1

        if new_char_count > max_chars or new_word_count > max_words or new_sentence_count > max_sentences:
            break

        chunk += sentence
        char_count = new_char_count
        word_count = new_word_count
        sentence_count = new_sentence_count

    remaining_text = text[len(chunk):]
    return chunk, remaining_text

def translate_text(text, target_lang, output, config):
    src_lang = LangDetect(text, 'lang')
    translated_text = TransLate(text, src_lang, target_lang)

    if output == 'screen':
        print(f"Translation to {target_lang}:")
        print(translated_text)
    elif output == 'file':
        file_name, ext = os.path.splitext(config['General']['input_file'])
        target_file = f"{file_name}_{target_lang}{ext}"
        with open(target_file, 'w', encoding='utf-8') as file:
            file.write(translated_text)
        print("Ok")
    else:
        print("Invalid output option in config file.")

def main():
    config_file = 'config.ini'
    config = read_config(config_file)

    input_file = config['General']['input_file']
    target_lang = config['General']['target_lang']
    output = config['General']['output']
    max_chars = int(config['General']['max_chars'])
    max_words = int(config['General']['max_words'])
    max_sentences = int(config['General']['max_sentences'])

    text, file_info = get_file_info(input_file)
    if text is None:
        print(file_info)
        return

    print(file_info)

    while text:
        chunk, text = get_text_chunk(text, max_chars, max_words, max_sentences)
        translate_text(chunk, target_lang, output,config)

if __name__ == '__main__':
    main()