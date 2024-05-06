from deep_translator import GoogleTranslator
from langdetect import detect
import pandas as pd

def TransLate(text: str, src: str, dest: str) -> str:
    translator = GoogleTranslator(source=src, target=dest)
    translated = translator.translate(text)
    return translated

def LangDetect(text: str, mode: str) -> str:
    try:
        if mode == 'lang':
            return detect(text)
        elif mode == 'confidence':
            return str(detect(text))
        else:
            raise ValueError("Invalid mode. Choose 'lang' or 'confidence'.")
    except Exception as e:
        return f"Language detection error: {str(e)}"

def CodeLang(lang: str) -> str:
    translator = GoogleTranslator()
    languages = translator.get_supported_languages(as_dict=True)
    lang_lower = lang.lower()

    for code, name in languages.items():
        if name.lower() == lang_lower:
            return code

    return "unknown"

def LanguageList(out: str = "screen", text: str = None) -> str:
    translator = GoogleTranslator()
    languages = translator.get_supported_languages(as_dict=True)

    data = []
    for code, name in languages.items():
        language_info = {'N': len(data) + 1, 'Language': name, 'ISO-639 code': code}
        if text:
            try:
                translation = GoogleTranslator(source='auto', target=code).translate(text)
                language_info['Text'] = translation
            except Exception as e:
                language_info['Text'] = f"Translation error: {str(e)}"
        data.append(language_info)

    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Determine the output destination
    if out == 'screen':
        # Output the table to the screen
        print(df.to_string(index=False))
        return "Ok"
    elif out == 'file':
        # Output the table to a file (CSV format)
        file_name = 'language_table.csv'
        df.to_csv(file_name, index=False)
        print(f"Table exported to '{file_name}'")
        return "Ok"
    else:
        return "Invalid output format. Please use 'screen' or 'file'."